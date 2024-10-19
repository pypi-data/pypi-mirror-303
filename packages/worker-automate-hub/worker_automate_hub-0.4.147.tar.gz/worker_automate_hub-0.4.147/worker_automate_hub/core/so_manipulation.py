import json
import os
import re
import subprocess
import zipfile

import toml
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from pathlib3x import Path
from playwright.async_api import async_playwright
from rich.console import Console

from worker_automate_hub.api.client import sync_get_config_by_name
from worker_automate_hub.config.settings import (
    get_package_version,
    load_env_config,
)
from worker_automate_hub.utils.get_creds_gworkspace import GetCredsGworkspace
from worker_automate_hub.utils.logger import logger

console = Console()


def write_env_config(env_dict: dict, google_credentials: dict):
    try:
        current_dir = Path.cwd()
        assets_path = current_dir / "assets"
        logs_path = current_dir / "logs"
        assets_path.mkdir(exist_ok=True)
        logs_path.mkdir(exist_ok=True)

        config_file_path = current_dir / "settings.toml"
        config_data = {
            "name": "WORKER",
            "params": {
                "api_base_url": env_dict["API_BASE_URL"],
                "api_auth": env_dict["API_AUTHORIZATION"],
                "notify_alive_interval": env_dict["NOTIFY_ALIVE_INTERVAL"],
                "version": get_package_version("worker-automate-hub"),
                "log_level": env_dict["LOG_LEVEL"],
                "drive_url": env_dict["DRIVE_URL"],
                "xml_default_folder": env_dict["XML_DEFAULT_FOLDER"],
            },
            "google_credentials": google_credentials["content"],
        }

        with open(config_file_path, "w") as config_file:
            toml.dump(config_data, config_file)

        log_msg = f"Arquivo de configuração do ambiente criado em {config_file_path}"
        logger.info(log_msg)
        console.print(f"\n{log_msg}\n", style="green")

        return {
            "Message": log_msg,
            "Status": True,
        }
    except Exception as e:
        err_msg = f"Erro ao criar o arquivo de configuração do ambiente. Comando retornou: {e}"
        logger.error(err_msg)
        return {
            "Message": err_msg,
            "Status": False,
        }


def add_worker_config(worker):
    try:
        current_dir = Path.cwd()
        config_file_path = current_dir / "settings.toml"

        if not config_file_path.exists():
            raise FileNotFoundError(
                f"O arquivo de configuração não foi encontrado em: {config_file_path}"
            )

        with open(config_file_path, "r") as config_file:
            config_data = toml.load(config_file)

        config_data["id"] = {
            "worker_uuid": worker["uuidRobo"],
            "worker_name": worker["nomRobo"],
        }

        with open(config_file_path, "w") as config_file:
            toml.dump(config_data, config_file)

        log_msg = f"Informações do worker adicionadas ao arquivo de configuração em {config_file_path}"
        console.print(f"\n{log_msg}\n", style="green")
        return {
            "Message": log_msg,
            "Status": True,
        }
    except Exception as e:
        err_msg = f"Erro ao adicionar informações do worker ao arquivo de configuração.\n Comando retornou: {e}"
        console.print(f"\n{err_msg}\n", style="bold red")
        return {
            "Message": err_msg,
            "Status": False,
        }


async def install_playwright():
    try:
        result1 = subprocess.run(
            ["pipx", "install", "playwright"],
            check=True,
            capture_output=True,
            text=True,
        )
        logger.info(result1.stdout)
        result2 = subprocess.run(
            ["playwright", "install"], check=True, capture_output=True, text=True
        )
        logger.info("Playwright instalado com sucesso!")
        logger.info(result2.stdout)
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro ao instalar Playwright: {e}")


def extract_zip(zip_path, extract_to):
    """
    Extrai um arquivo ZIP para um diretório especificado.

    :param zip_path: Caminho para o arquivo ZIP.
    :param extract_to: Diretório onde os arquivos serão extraídos.
    """
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
        console.print(f"\nArquivos extraídos para {extract_to}\n", style="green")


def extract_drive_folder_id(url: str) -> str:
    """
    Extrai o ID da pasta do Google Drive a partir de uma URL.

    Args:
        url (str): URL da pasta no Google Drive.

    Returns:
        str: O ID da pasta ou uma exceção ValueError se o ID não for encontrado.
    """
    match = re.search(r"folders/([a-zA-Z0-9-_]+)", url)
    if match:
        return match.group(1)
    else:
        raise ValueError("ID da pasta não encontrado na URL.")


async def update_assets():
    """
    Baixa todos os arquivos e pastas do Google Drive para o diretório local, mantendo a estrutura de pastas.
    """
    console.print("\nAtualizando os assets...\n", style="bold blue")
    try:
        # Obtendo tokens e credenciais do GCP
        get_gcp_token = sync_get_config_by_name("GCP_SERVICE_ACCOUNT")
        get_gcp_credentials = sync_get_config_by_name("GCP_CREDENTIALS")
    except Exception as e:
        console.print(
            f"Erro ao obter as configurações para execução do processo, erro: {e}...\n"
        )
        raise Exception(
            f"Erro ao obter as configurações para execução do processo, erro: {e}"
        )

    try:
        # Obter credenciais da Google Workspace
        gcp_credencial = GetCredsGworkspace(
            token_dict=get_gcp_token["conConfiguracao"],
            credentials_dict=get_gcp_credentials["conConfiguracao"],
        )
        creds = gcp_credencial.get_creds_gworkspace()
        env_config, _ = load_env_config()
        assets_drive_folder_id = extract_drive_folder_id(env_config["DRIVE_URL"])

        # Inicializar o serviço do Google Drive
        drive_service = build("drive", "v3", credentials=creds)

        def create_local_folder(path: str) -> None:
            """
            Cria um diretório local com a estrutura de pastas recebida.

            Args:
                path (str): O caminho do diretório a ser criado.

            Returns:
                None
            """
            os.makedirs(path, exist_ok=True)

        # Função recursiva para baixar arquivos e pastas mantendo a estrutura
        def download_folder(folder_id: str, parent_path: str) -> None:
            """
            Baixa todos os arquivos e pastas contidos na pasta com o ID fornecido e os salva no diretório local, mantendo a estrutura de pastas.

            Args:
                folder_id (str): O ID da pasta do Google Drive a ser baixada.
                parent_path (str): O caminho do diretório local onde os arquivos serão salvos.

            Returns:
                None
            """
            query = f"'{folder_id}' in parents"
            results = (
                drive_service.files()
                .list(
                    q=query,
                    pageSize=100,
                    supportsAllDrives=True,
                    includeItemsFromAllDrives=True,
                    fields="files(id, name, mimeType)",
                )
                .execute()
            )
            items = results.get("files", [])

            if not items:
                console.print(f"Nenhum arquivo encontrado na pasta {folder_id}.")
                return

            # Processar cada item na pasta
            for item in items:
                file_id = item["id"]
                file_name = item["name"]
                mime_type = item["mimeType"]

                # Caminho completo do item no sistema local
                local_path = os.path.join(parent_path, file_name)

                if mime_type == "application/vnd.google-apps.folder":
                    # Se for uma pasta, criar a pasta localmente e fazer chamada recursiva
                    console.print(f"\nCriando pasta {file_name}", style="bold")
                    create_local_folder(local_path)
                    download_folder(file_id, local_path)
                else:
                    # Se for um arquivo, baixar o arquivo no local apropriado
                    console.print(
                        f"\nBaixando arquivo {file_name} para {local_path}",
                        style="blue",
                    )

                    if mime_type in [
                        "application/vnd.google-apps.document",
                        "application/vnd.google-apps.spreadsheet",
                        "application/vnd.google-apps.presentation",
                    ]:
                        # Exportar Google Docs, Sheets ou Slides para PDF
                        request = drive_service.files().export_media(
                            fileId=file_id, mimeType="application/pdf"
                        )
                        local_path = (
                            local_path.replace(".gdoc", ".pdf")
                            .replace(".gsheet", ".pdf")
                            .replace(".gslides", ".pdf")
                        )
                    else:
                        # Baixar arquivos binários normais
                        request = drive_service.files().get_media(fileId=file_id)

                    with open(local_path, "wb") as fh:
                        downloader = MediaIoBaseDownload(fh, request)
                        done = False
                        while not done:
                            status, done = downloader.next_chunk()
                            console.print(
                                f"Baixando {file_name}: {int(status.progress() * 100)}% concluído.",
                                style="bold green",
                            )

        # Criar a pasta raiz 'assets' no diretório local se não existir
        root_path = "assets"
        create_local_folder(root_path)

        # Baixar a estrutura completa de pastas e arquivos
        download_folder(assets_drive_folder_id, root_path)

        console.print(
            "\nTodos os arquivos e pastas foram baixados e salvos na pasta 'assets' com sucesso.\n",
            style="bold green",
        )

    except Exception as e:
        console.print(f"\nErro ao atualizar os assets: {e}...\n", style="bold red")


async def install_tesseract(setup_path: Path):
    try:
        # Comando para executar com elevação
        command = f'start-process "{setup_path}" -Verb runAs'

        # Executar o comando usando PowerShell
        result = subprocess.run(
            ["powershell", "-Command", command], capture_output=True
        )
        logger.info(result.stdout)
        logger.info("Tesseract instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro ao instalar Tesseract: {e}")


async def download_tesseract():
    # Diretório de execução atual
    current_dir = Path.cwd()
    output_folder = current_dir / "temp"
    destination_path = output_folder / "tesseract.exe"

    folder_url = "https://github.com/UB-Mannheim/tesseract/wiki"
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True
        )  # Defina headless=True se não quiser ver o navegador
        context = await browser.new_context()

        # Abrir uma nova página
        page = await context.new_page()

        # Navegar para a URL do arquivo no Google Drive
        await page.goto(folder_url)

        # Aguarde o carregamento da página e clique no botão de download
        await page.wait_for_selector(
            "#wiki-body > div > ul:nth-child(7) > li > a",
            timeout=60000,
        )
        await page.click("#wiki-body > div > ul:nth-child(7) > li > a")

        # Aguarde o download começar
        download = await page.wait_for_event("download")

        # Salve o arquivo no destino especificado
        await download.save_as(destination_path)

        await browser.close()

    await install_tesseract(destination_path)
