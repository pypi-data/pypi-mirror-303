import subprocess
import pyautogui
import asyncio
import os
from rich.console import Console
from worker_automate_hub.utils.logger import logger
import time
import pygetwindow as gw

console = Console()

def tirar_screenshot(nome_etapa):
    caminho_screenshot = f"{nome_etapa}_{int(time.time())}.png"
    pyautogui.screenshot(caminho_screenshot)
    console.print(f"Screenshot tirada: {caminho_screenshot}")
    return caminho_screenshot

def deletar_screenshots(caminhos_screenshots):
    for caminho in caminhos_screenshots:
        try:
            os.remove(caminho)
            console.print(f"Screenshot deletada: {caminho}")
        except OSError as e:
            console.print(f"Erro ao deletar screenshot {caminho}: {e}")

def fechar_janelas_rdp_sem_ip():
    janelas_rdp = [win for win in gw.getAllTitles() if "Conexão de Área de Trabalho Remota" in win or "Remote Desktop Connection" in win]
    for titulo in janelas_rdp:
        if not any(char.isdigit() for char in titulo):
            console.print(f"Fechando pop-up de conexão sem IP: {titulo}")
            janela = gw.getWindowsWithTitle(titulo)[0]
            janela.close()
            time.sleep(2)

def fechar_janela_existente(ip):
    try:
        janelas_encontradas = gw.getAllTitles()
        for titulo in janelas_encontradas:
            if ip in titulo:
                janela = gw.getWindowsWithTitle(titulo)[0]
                console.print(f"Fechando janela existente: {titulo}")
                janela.activate()
                pyautogui.hotkey('alt', 'f4')
                time.sleep(2)
                break
        else:
            console.print(f"Nenhuma janela encontrada com o IP: {ip}")

        fechar_janelas_rdp_sem_ip()

    except Exception as e:
        console.print(f"Erro ao tentar fechar a janela: {e}", style="bold red")

def restaurar_janelas_rdp():
    janelas_rdp = [win for win in gw.getAllTitles() if "Conexão de Área de Trabalho Remota" in win or "Remote Desktop Connection" in win]
    
    offset_x = 0
    offset_y = 0
    step_x = 30
    step_y = 30

    for titulo in janelas_rdp:
        janela = gw.getWindowsWithTitle(titulo)[0]
        console.print(f"Processando janela: {titulo}")
        if janela.isMinimized:
            janela.restore()
            console.print(f"Janela restaurada: {titulo}")
        else:
            console.print(f"Janela já está aberta: {titulo}")

        janela.moveTo(offset_x, offset_y)

        offset_x += step_x
        offset_y += step_y

        janela.activate()
        time.sleep(2)

def redimensionar_janela_rdp(largura, altura):
    janelas_rdp = [win for win in gw.getAllTitles() if "Conexão de Área de Trabalho Remota" in win or "Remote Desktop Connection" in win]
    
    if janelas_rdp:
        janela_rdp = gw.getWindowsWithTitle(janelas_rdp[0])[0]
        janela_rdp.resizeTo(largura, altura)
        janela_rdp.moveTo(20, 20)
        console.print(f"Janela redimensionada para {largura}x{altura}.")

        janela_rdp.activate()
        janela_rdp.restore()
        time.sleep(1)
    else:
        console.print("Não foi possível encontrar a janela RDP para redimensionar.")

async def conexao_rdp(task):
    caminhos_screenshots = []
    try:
        ip = task["configEntrada"].get("ip", "")
        user = task["configEntrada"].get("user", "")
        password = task["configEntrada"].get("password", "")

        pyautogui.hotkey('win', 'd')
        console.print("1 - Minimizando todas as telas...")
        await asyncio.sleep(2)

        fechar_janela_existente(ip)

        subprocess.Popen('mstsc')
        console.print("2 - Abrindo conexão de trabalho remota...")
        await asyncio.sleep(2)

        redimensionar_janela_rdp(500, 500)

        await asyncio.sleep(2)

        janelas_rdp = [win for win in gw.getAllTitles() if "Conexão de Área de Trabalho Remota" in win or "Remote Desktop Connection" in win]
        if janelas_rdp:
            janela_rdp = gw.getWindowsWithTitle(janelas_rdp[0])[0]
            janela_rdp.activate()
            janela_rdp.restore()
            await asyncio.sleep(1)

        caminhos_screenshots.append(tirar_screenshot("antes_de_inserir_ip"))
        console.print("3 - Inserindo o IP...")
        pyautogui.write(ip)
        await asyncio.sleep(10)
        caminhos_screenshots.append(tirar_screenshot("depois_de_inserir_ip"))
        pyautogui.press('enter')
        await asyncio.sleep(5)
        caminhos_screenshots.append(tirar_screenshot("depois_de_inserir_usuario"))
        await asyncio.sleep(5)

        console.print("5 - Inserindo a Senha...")
        pyautogui.write(password)
        pyautogui.press('enter')
        await asyncio.sleep(10)
        caminhos_screenshots.append(tirar_screenshot("depois_de_inserir_senha"))

        console.print("6 - Apertando left...")
        pyautogui.press('left')
        await asyncio.sleep(2)
        console.print("7 - Apertando Enter...")
        pyautogui.press('enter')
        await asyncio.sleep(20)
        caminhos_screenshots.append(tirar_screenshot("depois_do_certificado"))

        console.print("8 - Minimizando todas as telas no final...")
        pyautogui.hotkey('win', 'd')
        await asyncio.sleep(2)
        caminhos_screenshots.append(tirar_screenshot("depois_de_minimizar_todas"))

        restaurar_janelas_rdp()
        caminhos_screenshots.append(tirar_screenshot("depois_de_restaurar_janelas"))

        deletar_screenshots(caminhos_screenshots)

        return {"sucesso": True, "retorno": "Processo de conexão ao RDP executado com sucesso."}

    except Exception as ex:
        err_msg = f"Erro ao executar conexao_rdp: {ex}"
        logger.error(err_msg)
        console.print(err_msg, style="bold red")
        caminhos_screenshots.append(tirar_screenshot("erro"))
        deletar_screenshots(caminhos_screenshots)
        return {"sucesso": False, "retorno": err_msg}
