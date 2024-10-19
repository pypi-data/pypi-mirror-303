import asyncio
from pathlib import Path
import io
import shutil
import os
import time
import uuid
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from playwright.async_api import async_playwright

import pyautogui
from rich.console import Console

from worker_automate_hub.api.client import sync_get_config_by_name
from worker_automate_hub.api.client import get_config_by_name
from worker_automate_hub.utils.logger import logger

from worker_automate_hub.utils.get_creds_gworkspace import GetCredsGworkspace
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build


pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False
console = Console()


def find_and_click(image_path, description, confidence=0.8, write_text=None, wait_time=2):
    element = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    if element:
        pyautogui.click(element)
        console.print(f"[green]'{description}' encontrado e clicado.[/green]")
        if write_text:
            pyautogui.write(write_text, interval=0.05)
            console.print(f"[green]Texto '{write_text}' inserido em '{description}'.[/green]")
        time.sleep(wait_time)
    else:
        raise Exception(f"[red]Elemento '{description}' não encontrado![/red]")


def send_email(smtp_server, smtp_port, smtp_user, smtp_password, message_text, subject, to):
    message = create_message_with_attachment(smtp_user, to, subject, message_text)
    send_message(smtp_server, smtp_port, smtp_user, smtp_password, smtp_user, to, message)


def create_message_with_attachment(sender, to, subject, message_text, file):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    if file:
        content_type, encoding = mimetypes.guess_type(file)

        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'

        main_type, sub_type = content_type.split('/', 1)
        with open(file, 'rb') as f:
            attachment = MIMEBase(main_type, sub_type)
            attachment.set_payload(f.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            attachment.add_header('Content-Transfer-Encoding', 'base64')
            message.attach(attachment)

    return message.as_string()


def send_message(smtp_server, smtp_port, smtp_user, smtp_password, sender, recipient, message):
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender, recipient, message)
            logger.info('Mensagem enviada com sucesso')
    except smtplib.SMTPAuthenticationError:
        console.print(f'Erro de autenticação. Verifique seu nome de usuário e senha.\n')
        logger.error('Erro de autenticação. Verifique seu nome de usuário e senha.')
    except smtplib.SMTPConnectError:
        console.print(f'Não foi possível conectar ao servidor SMTP. Verifique o endereço e a porta.\n')
        logger.error('Não foi possível conectar ao servidor SMTP. Verifique o endereço e a porta.')
    except smtplib.SMTPRecipientsRefused:
        console.print(f'O destinatário foi rejeitado. Verifique o endereço do destinatário.\n')
        logger.error('O destinatário foi rejeitado. Verifique o endereço do destinatário.')
    except smtplib.SMTPSenderRefused:
        console.print(f'O remetente foi rejeitado. Verifique o endereço do remetente..\n')
        logger.error('O remetente foi rejeitado. Verifique o endereço do remetente.')
    except smtplib.SMTPDataError as e:
        console.print(f'Erro ao enviar dados: {e}\n')
        logger.error(f'Erro ao enviar dados: {e}')
    except Exception as error:
        console.print(f'Ocorreu um erro ao enviar a mensagem: {error} \n')
        logger.error('Ocorreu um erro ao enviar a mensagem: %s' % error)


async def ecac_estadual_go(task):
    """
    Processo que realiza a consulta de caixa postal do ECAC Estadual de Goais para o certificado SIM DISTRIBUIDORA.

    """
    try:
        # Obtém a resolução da tela
        screen_width, screen_height = pyautogui.size()
        console.print(f"Resolução da tela: Width: {screen_width} - Height{screen_height}...\n")
        console.print(f"Task:{task}")

        console.print("Realizando as validações inicias para execução do processo\n")
        console.print("Criando o diretório temporario ...\n")

        cd = Path.cwd()
        temp_dir = f"{cd}\\temp_certificates\\{str(uuid.uuid4())}"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        console.print("Obtendo configuração para execução do processo ...\n")
        try:
            config = await get_config_by_name("Ecac_Estadual_GO")
            emails_to = config['conConfiguracao']['emails']
            certificado_path = config['conConfiguracao']['CertificadoPath']
            certificado_file = config['conConfiguracao']['CertificadoFile']
            certificado_pwd = config['conConfiguracao']['Pwd']

            console.print("Obtendo configuração de email para execução do processo ...\n")
            smtp_config = await get_config_by_name("SMTP")

            smtp_server = smtp_config['conConfiguracao']['server']
            smtp_user = smtp_config['conConfiguracao']['user']
            smtp_pass = smtp_config['conConfiguracao']['password']
            smtp_port =  smtp_config['conConfiguracao']['port']

            get_gcp_token = sync_get_config_by_name("GCP_SERVICE_ACCOUNT")
            get_gcp_credentials = sync_get_config_by_name("GCP_CREDENTIALS")
        except Exception as e:
            console.print(f'Erro ao obter as configurações para execução do processo, erro: {e}...\n')
            return {"sucesso": False, "retorno": f"Erro ao obter as configurações para execução do processo, erro: {e}"}

        console.print("Verificando a existência do diretório com locators...\n")
        if os.path.exists("assets/ecac_federal"):
            console.print('Diretório existe..\n')
        else:
            console.print('Diretório não existe..\n')
            return {"sucesso": False, "retorno": f"Não foi possivel encontrar o diretório com os locators para continuidade do processo, diretório: 'assets/ecac_federal'"}

        try:
            gcp_credencial = GetCredsGworkspace(token_dict=get_gcp_token['conConfiguracao'], credentials_dict=get_gcp_credentials['conConfiguracao'])
            creds = gcp_credencial.get_creds_gworkspace()

            console.print(f'Procurando certificado: {certificado_file} ...\n')
            drive_service = build("drive", "v3", credentials=creds)
            query = f"'{certificado_path}' in parents and name='{certificado_file}'"
            results = drive_service.files().list(
                q=query,
                pageSize=1000,
                supportsAllDrives=True,  # Habilita suporte para Shared Drives
                includeItemsFromAllDrives=True,  # Inclui itens de todos os drives
                fields="files(id, name)"
            ).execute()

            items = results.get('files', [])

            if items:
                console.print(f'Certificado: {certificado_file} encontrado...\n')
                file_id = items[0]['id']
                console.print(f'Iniciando download...\n')

                file_path = os.path.join(temp_dir, certificado_file)

                request = drive_service.files().get_media(fileId=file_id)

                fh = io.FileIO(file_path, 'wb')
                downloader = MediaIoBaseDownload(fh, request)

                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    console.print(f"Download {int(status.progress() * 100)}%.")

                console.print(f"Certificado {certificado_file} baixado com sucesso.\n")

                fh.close()
            
            else:
                console.print(f'Certificado não encontrado para realização do download, {certificado_file}...\n')
                return {"sucesso": False, "retorno": f"Certificado não encontrado para realização do download, {certificado_file}"}
        except Exception as e:
            console.print(f'Erro ao realizar download do certificado: {e}...\n')
            return {"sucesso": False, "retorno": f"Erro ao realizar download do certificado: {e}"}
                
        
        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=False)
            
            console.print("Iniciando o browser")
            context = await browser.new_context(accept_downloads=True)
            page = await context.new_page()

            await asyncio.sleep(3)

            await page.goto('about:preferences#privacy')

            locator_path = "assets/ecac_federal"

            element_find_settings_image = f'{locator_path}/FindInSettings.PNG' 
            element_view_certificates = f'{locator_path}/ViewCertificates.PNG'
            element_your_certificates = f'{locator_path}/YourCertificates.PNG'
            element_import_certificates = f'{locator_path}/ImportCertificate.PNG'
            element_insert_path_certificates = f'{locator_path}/InsertPathCertificate.PNG'
            element_open_certificates = f'{locator_path}/OpenCertificate.PNG'
            element_pwd_certificates = f'{locator_path}/EnterPasswordCertificate.PNG'
            element_sign_in_certificates = f'{locator_path}/SignCertificate.PNG'
            element_confirm_certificates = f'{locator_path}/Confirm.PNG'
            element_sign_in_certificates = f'{locator_path}/SignCertificate.PNG'
            element_popup_certificate = f'{locator_path}/ImportCertificate_popup.PNG'

            console.print("Importando o certificado no browser (playwright) ")
            # Configurações
            find_and_click(element_find_settings_image, "Configurações")
            pyautogui.write('Cert', interval=0.05)
            await asyncio.sleep(1)

            # Certificados
            find_and_click(element_view_certificates, "Certificados")
            await asyncio.sleep(1)

            # Meus Certificados
            find_and_click(element_your_certificates, "Meus Certificados")
            await asyncio.sleep(1)

            # Importar Certificado
            find_and_click(element_import_certificates, "Importar Certificado")
            await asyncio.sleep(2)

            # Inserir Caminho do Certificado e escrever o caminho do arquivo
            find_and_click(element_insert_path_certificates, "Inserir Caminho do Certificado", write_text=file_path)
            await asyncio.sleep(2)

            # Abrir Certificado
            find_and_click(element_open_certificates, "Abrir Certificado")
            await asyncio.sleep(2)

            # Inserir Senha do Certificado
            find_and_click(element_pwd_certificates, "Inserir Senha do Certificado", write_text=certificado_pwd)
            await asyncio.sleep(2)

            # Assinar Certificado
            find_and_click(element_sign_in_certificates, "Assinar Certificado")
            await asyncio.sleep(2)

            # Confirmar Importação
            find_and_click(element_confirm_certificates, "Confirmar Importação")
            await asyncio.sleep(2)

            element_popup_certificate = False
            try:
                element_popup_certificate = pyautogui.locateCenterOnScreen(element_popup_certificate, confidence=0.8)
                element_popup_certificate = True
            except:
                pass

            if not element_popup_certificate:
                await asyncio.sleep(3)

                await page.goto("https://dte.sefaz.go.gov.br/dte/web/https/painelControle.jsf")
                await asyncio.sleep(3)
                await page.keyboard.press("Enter")

                parte1 = await page.locator("/html/body/div[3]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/span[1]").text_content()
                parte2 = await page.locator("/html/body/div[3]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/b[1]/span").text_content()
                parte3 = await page.locator("/html/body/div[3]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/span[2]").text_content()
                parte4 = await page.locator("/html/body/div[3]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/b[2]/span").text_content()
                parte5 = await page.locator("/html/body/div[3]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/span[4]").text_content()

                frase_completa = f"{parte1} {parte2} {parte3} {parte4} {parte5}"

                corpo_email = f''' Caros(as), \nEspero que este e-mail o encontre bem! \n\n Abaixo, segue um resumo baseado na consulta à caixa postal referente ao estado de GO.
                \n Resultado da consulta: \n {frase_completa} \n '''

                try:
                    await context.close()
                    await browser.close()
                except Exception as e:
                    console.print('Erro ao encerrar o browser... \n', e)

                try:
                    send_email(smtp_server, smtp_port, smtp_user, smtp_pass, corpo_email, "Consulta ECAC_Estadual - GO", emails_to)
                    log_msg = f"Processo concluído e e-mail disparado para área de negócio"
                    console.print(log_msg)
                    return {"sucesso": True, "retorno": log_msg}
                except Exception as e:
                    log_msg = f"Processo concluído com sucesso, porém houve falha no envio do e-mail para área de negócio"
                    console.print(log_msg)
                    return {"sucesso": False, "retorno": log_msg}

                         
    except Exception as e:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        log_msg = f"Erro Processo do Ecac Estadual GO: {e}"
        logger.error(log_msg)
        console.print(log_msg, style="bold red")
        return {"sucesso": False, "retorno": log_msg}