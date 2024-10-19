import threading

import aiohttp
from aiohttp import ClientSession
import requests
from rich.console import Console

from worker_automate_hub.api.helpers.api_helpers import handle_api_response
from worker_automate_hub.config.settings import load_env_config
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import get_new_task_info, get_system_info

console = Console()


async def get_new_task(stop_event: threading.Event):
    env_config, _ = load_env_config()
    try: 
        headers_basic = {"Authorization": f"Basic {env_config["API_AUTHORIZATION"]}"}
        data = await get_new_task_info()

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.post(
                f"{env_config["API_BASE_URL"]}/robo/new-job",
                data=data,
                headers=headers_basic,
            ) as response:
                return await handle_api_response(response, stop_event)

    except Exception as e:
        err_msg = f"Erro ao obter nova tarefa: {e}"
        logger.error(err_msg)
        console.print(
            f"{err_msg}\n",
            style="bold red",
        )
        return None

async def burnQueue(id_fila: str):
    env_config, _ = load_env_config()
    try:       

        headers_basic = {"Authorization": f"Basic {env_config["API_AUTHORIZATION"]}"}
        

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.delete(
                f"{env_config["API_BASE_URL"]}/fila/burn-queue/{id_fila}",
                headers=headers_basic,
            ) as response:
                if response.status == 200:
                    logger.info("Fila excluida com sucesso.")
                    console.print("\nFila excluida com sucesso.\n", style="bold green")    
                else:
                    logger.error(f"Erro ao excluir a fila: {response.content}") 
                    console.print(f"Erro ao excluir a fila: {response.content}", style="bold red")          

    except Exception as e:
        err_msg = f"Erro remover registro da fila: {e}"
        logger.error(err_msg)
        console.print(
            f"{err_msg}\n",
            style="bold red",
        )
        return None
    
async def notify_is_alive(stop_event: threading.Event):
    env_config, _ = load_env_config()
    try:       

        headers_basic = {"Authorization": f"Basic {env_config["API_AUTHORIZATION"]}"}
        data = await get_system_info()

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.put(
                f"{env_config["API_BASE_URL"]}/robo/last-alive",
                data=data,
                headers=headers_basic,
            ) as response:
                return await handle_api_response(response, stop_event, last_alive=True)

    except Exception as e:
        err_msg = f"Erro ao informar is alive: {e}"
        logger.error(err_msg)
        console.print(
            f"{err_msg}\n",
            style="bold red",
        )
        return None
    
async def get_processo(uuidProcesso: str):
    env_config, _ = load_env_config()
    try:      
        headers_basic = {"Authorization": f"Basic {env_config["API_AUTHORIZATION"]}"}       
        

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.get(
                f"{env_config["API_BASE_URL"]}/processo/{uuidProcesso}",                
                headers=headers_basic,
            ) as response:
                return await response.json()

    except Exception as e:
        err_msg = f"Erro ao obter o processo: {e}"
        logger.error(err_msg)
        console.print(
            f"{err_msg}\n",
            style="bold red",
        )
        return None


async def get_workers():
    env_config, _ = load_env_config()
    try:
        

        headers_basic = {"Authorization": f"Basic {env_config["API_AUTHORIZATION"]}"}

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.get(
                f"{env_config["API_BASE_URL"]}/robo/workers",
                headers=headers_basic,
            ) as response:
                return await response.json()

    except Exception as e:
        err_msg = f"Erro ao obter a lista de workers: {e}"
        logger.error(err_msg)
        console.print(
            f"{err_msg}\n",
            style="bold red",
        )
        return None

async def get_config_by_name(name: str):
    env_config, _ = load_env_config()
    try:        

        headers_basic = {"Authorization": f"Basic {env_config["API_AUTHORIZATION"]}"}

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.get(
                f"{env_config["API_BASE_URL"]}/configuracao/{name}",
                headers=headers_basic,
            ) as response:
                return await response.json()

    except Exception as e:
        err_msg = f"Erro ao obter a configuração: {e}"
        logger.error(err_msg)
        console.print(
            f"{err_msg}\n",
            style="bold red",
        )
        return None
    
def sync_get_config_by_name(name: str):
    env_config, _ = load_env_config()
    
    try:
        headers_basic = {"Authorization": f"Basic {env_config['API_AUTHORIZATION']}"}

        response = requests.get(
            f"{env_config['API_BASE_URL']}/configuracao/{name}",
            headers=headers_basic,
            verify=False  # Desativa a verificação SSL
        )

        response.raise_for_status()
        
        return response.json()

    except requests.RequestException as e:
        err_msg = f"Erro ao obter a configuração: {e}"
        logger.error(err_msg)
        console.print(err_msg, style="red")
        return None
    
async def send_gchat_message(message: str):
    env_config, _ = load_env_config()
    try:       

        headers_basic = {"Authorization": f"Basic {env_config["API_AUTHORIZATION"]}"}        

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.post(
                f"{env_config["API_BASE_URL"]}/google-chat",
                data={"message": message},
                headers=headers_basic,
            ) as response:
                data = await response.text()
                console.print(f"Retorno de enviar msg no chat: {data}")
                # return await response.json()

    except Exception as e:
        err_msg = f"Erro ao enviar mensagem ao Google Chat: {e}"
        logger.error(err_msg)
        console.print(
            f"{err_msg}\n",
            style="bold red",
        )
        return None
    
async def unlock_queue(id: str):
    env_config, _ = load_env_config()
    try:      
        headers_basic = {"Authorization": f"Basic {env_config["API_AUTHORIZATION"]}"}       
        

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.get(
                f"{env_config["API_BASE_URL"]}/fila/unlock-queue/{id}",                
                headers=headers_basic,
            ) as response:
                return await response.text()

    except Exception as e:
        err_msg = f"Erro ao desbloquear a fila: {e}"
        logger.error(err_msg)
        console.print(
            f"{err_msg}\n",
            style="bold red",
        )
        return None


def read_secret(path: str, vault_token: str):
    

    url = f"https://aspirina.simtech.solutions/{path}"
    headers = {"X-Vault-Token": vault_token, "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result["data"]["data"]
    elif response.status_code == 403:
        err_msg = "403 - Token inválido!"
        logger.error(err_msg)
        console.print(f"\n{err_msg}\n", style="bold red")
    else:
        response.raise_for_status()


def load_environments(env: str, vault_token: str):

    environments = {}   
    credentials = {}

    environments[env] = read_secret(path=f"v1/{env}-sim/data/worker-automate-hub/env", vault_token=vault_token)
    credentials[env] = read_secret(path=f"v1/{env}-sim/data/worker-automate-hub/credentials.json", vault_token=vault_token)

    return environments[env], credentials[env]


async def get_index_modelo_emsys(filial, descricao_documento):
    env_config, _ = load_env_config()
    
    body = {
        "codigoEmpresa":{filial},
        "descricaoDocumento": {descricao_documento}
        }
    headers_basic = {"Authorization": f"Basic {env_config["API_AUTHORIZATION"]}"} 

    try:
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(verify_ssl=False)
        ) as session:
            async with session.post(f"{env_config['API_BASE_URL']}/emsys/buscar-index-documento-fiscal", data=body, 
                                    headers=headers_basic) as response:
                data = await response.json()
                log_msg = f"\nSucesso ao procurar {data}.\n"
                console.print(
                    log_msg,
                    style="bold green",
                )
                logger.info(log_msg)
                return data

    except Exception as e:
        err_msg = f"Erro ao comunicar com endpoint do Simplifica: {e}"
        console.print(f"\n{err_msg}\n", style="bold green")
        logger.info(err_msg)

# Função para enviar arquivo de imagem a api
async def send_file(uuidRelacao: str, desArquivo: str, tipo: str, file: bytes) -> None:
    """
    Função assíncrona para enviar um arquivo de imagem para uma API.

    Args:
        uuidRelacao (str): UUID da relação associada ao arquivo.
        desArquivo (str): Descrição do arquivo.
        tipo (str): Tipo de arquivo.
        file (bytes): Conteúdo binário do arquivo.
    """
    try:
        # Carrega as configurações de ambiente
        env_config, _ = load_env_config()

        # Criação do corpo da requisição multipart
        body = aiohttp.FormData()
        body.add_field('uuidRelacao', uuidRelacao)
        body.add_field('desArquivo', desArquivo)
        body.add_field('tipo', tipo)
        body.add_field('file', file, filename="file.jpg", content_type="image/jpeg")

        headers_basic = {
            "Authorization": f"Basic {env_config['API_AUTHORIZATION']}"
        }

        # Enviando requisição para a API
        async with ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post(f"{env_config['API_BASE_URL']}/arquivo/send-file", data=body, headers=headers_basic) as response:
                response.raise_for_status()  # Levanta exceção se o status não for 2xx
                log_msg = f"\nSucesso ao enviar arquivo: {uuidRelacao}.\n"
                console.print(log_msg, style="bold green")
                logger.info(log_msg)

    except aiohttp.ClientResponseError as e:
        err_msg = f"Erro na resposta da API: {e.status} - {e.message}"
        console.print(f"\n{err_msg}\n", style="bold red")
        logger.error(err_msg)

    except Exception as e:
        err_msg = f"Erro ao enviar arquivo: {str(e)}"
        console.print(f"\n{err_msg}\n", style="bold red")
        logger.error(err_msg)