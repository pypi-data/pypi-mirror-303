import asyncio
import os
import time
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from playwright.async_api import async_playwright

import pyautogui
from bs4 import BeautifulSoup
from rich.console import Console

from worker_automate_hub.api.client import get_config_by_name
from worker_automate_hub.utils.logger import logger


pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False
console = Console()


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


async def ecac_estadual_sc(task):
    """
    Processo que realiza a consulta de caixa postal do ECAC Estadual de SC.

    """
    try:
        # Obtém a resolução da tela
        screen_width, screen_height = pyautogui.size()
        console.print(f"Resolução da tela: Width: {screen_width} - Height{screen_height}...\n")
        console.print(f"Task:{task}")

        console.print("Realizando as validações inicias para execução do processo\n")
        console.print("Obtendo configuração para execução do processo ...\n")
        try:
            config = await get_config_by_name("Ecac_Estadual_SC")
            emails_to = config['conConfiguracao']['emails']
            user = config['conConfiguracao']['Usuario']
            password = config['conConfiguracao']['Senha']

            console.print("Obtendo configuração de email para execução do processo ...\n")
            smtp_config = await get_config_by_name("SMTP")

            smtp_server = smtp_config['conConfiguracao']['server']
            smtp_user = smtp_config['conConfiguracao']['user']
            smtp_pass = smtp_config['conConfiguracao']['password']
            smtp_port =  smtp_config['conConfiguracao']['port']

        except Exception as e:
            console.print(f'Erro ao obter as configurações para execução do processo, erro: {e}...\n')
            return {"sucesso": False, "retorno": f"Erro ao obter as configurações para execução do processo, erro: {e}"}
        

        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=False)
            
            console.print("Iniciando o browser\n")
            context = await browser.new_context(accept_downloads=True)
            page = await context.new_page()

            await asyncio.sleep(3)

            console.print("Navegando até o site SAT... \n")
            await page.goto("https://sat.sef.sc.gov.br/tax.NET/Login.aspx?ReturnUrl=%2ftax.NET%2fsat.dtec.web%2fSATautenticacao.aspx")
            console.print("Realizando login... \n")
            await asyncio.sleep(3)
            await page.get_by_placeholder("Usuário").fill(user)
            await page.get_by_placeholder("Senha").fill(password)
            await page.get_by_role("link", name="Entrar", exact=True).click()
            await asyncio.sleep(3)
            console.print("Sucesso ao realizar o login... \n")
            await page.get_by_role("link", name="person").click()
            await asyncio.sleep(3)
            console.print("Navegando até caixa de entrada... \n")
            await page.get_by_role("link", name=" Caixa de entrada").click()

            console.print("Extraindo mensagens... \n")
            await page.wait_for_selector('//*[@id="ext-gen47"]')
            time.sleep(3)

            div_content = await page.locator('//*[@id="ext-gen47"]').inner_html()

            console.print("Formatando saida de dados... \n")
            soup = BeautifulSoup(div_content, 'html.parser')

            rows = soup.select('tr')
            formatted_output = ''
            corpo_email = ''
            for row in rows:
                try:
                    id_mensagem = row.select_one('.x-grid3-col-0').text.strip()
                    status_lida = row.select_one('.x-grid3-col-1 img')['alt'].strip()
                    remetente = row.select_one('.x-grid3-col-2').text.strip()
                    tipo_mensagem = row.select_one('.x-grid3-col-3').text.strip()
                    data_envio = row.select_one('.x-grid3-col-4').text.strip()
                    assunto = row.select_one('.x-grid3-col-ASSUNTO').text.strip()

                    if status_lida == 'Não Lida':
                        formatted_output += (f"ID Mensagem: {id_mensagem}\n"
                                    f"Status: {status_lida}\n"
                                    f"Remetente: {remetente}\n"
                                    f"Tipo de Mensagem: {tipo_mensagem}\n"
                                    f"Data de Envio: {data_envio}\n"
                                    f"Assunto: {assunto}\n")
                except:
                    pass

            
            console.print("Enviando email para area de negócio \n")
            if formatted_output != '':
                corpo_email = f''' Caros(as), \nEspero que este e-mail o encontre bem! \n\n Abaixo, segue um resumo baseado na consulta à caixa postal referente ao estado de SC.
                \n Resultado da consulta: \n {formatted_output} \n '''
            else:
                corpo_email = f''' Caros(as), \nEspero que este e-mail o encontre bem! \n\n O processo foi executado para coleta de mensagens na caixa postal referente ao estado de SC, porém não foi encontrado nenhuma nova mensagem.'''

            try:
                await context.close()
                await browser.close()
            except Exception as e:
                console.print('Erro ao encerrar o browser... \n', e)

            try:
                send_email(smtp_server, smtp_port, smtp_user, smtp_pass, corpo_email, "Consulta ECAC_Estadual - SC", emails_to)
                log_msg = f"Processo concluído e e-mail disparado para área de negócio"
                console.print(log_msg)
                return {"sucesso": True, "retorno": log_msg}
            except Exception as e:
                log_msg = f"Processo concluído com sucesso, porém houve falha no envio do e-mail para área de negócio"
                console.print(log_msg)
                return {"sucesso": False, "retorno": log_msg}
            
    except Exception as e:
        log_msg = f"Erro Processo do Ecac Estadual SC: {e}"
        logger.error(log_msg)
        console.print(log_msg, style="bold red")
        return {"sucesso": False, "retorno": log_msg}