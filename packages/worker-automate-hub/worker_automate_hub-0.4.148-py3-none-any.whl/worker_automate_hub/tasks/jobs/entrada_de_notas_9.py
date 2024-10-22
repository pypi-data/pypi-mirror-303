import asyncio
import warnings

import pyautogui
from pywinauto.application import Application
from rich.console import Console
from worker_automate_hub.api.client import sync_get_config_by_name

from worker_automate_hub.api.client import get_config_by_name
from worker_automate_hub.config.settings import load_env_config
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import (
    check_pagamento,
    check_itens_nota,
    finalizar_importacao,
    import_nfe,
    kill_process,
    login_emsys,
    select_model_capa,
    type_text_into_field,
    get_xml,
    download_xml,
    config_natureza,
    config_almoxarifado,
    delete_xml,
    set_variable,
    get_variable,
    worker_sleep,
)

pyautogui.PAUSE = 0.5
console = Console()


async def entrada_de_notas_9(task):
    """
    Processo que relazia entrada de notas no ERP EMSys(Linx).

    """
    try:
        #Get config from BOF
        config = await get_config_by_name("login_emsys")
        console.print(task)
       
        #Seta config entrada na var nota para melhor entendimento
        nota = task['configEntrada']
        multiplicador_timeout = int(float(task["sistemas"][0]["timeout"]))
        set_variable("timeout_multiplicador", multiplicador_timeout)

        #Abre um novo emsys
        await kill_process("EMSys")
        app = Application(backend='win32').start("C:\\Rezende\\EMSys3\\EMSys3.exe")
        warnings.filterwarnings("ignore", category=UserWarning, message="32-bit application should be automated using 32-bit Python")
        console.print("\nEMSys iniciando...", style="bold green")
        return_login = await login_emsys(config['conConfiguracao'], app, task)

        if return_login['sucesso'] == True:
            type_text_into_field('Nota Fiscal de Entrada', app['TFrmMenuPrincipal']['Edit'], True, '50')
            pyautogui.press('enter')
            await worker_sleep(1)
            pyautogui.press('enter')
            console.print(f"\nPesquisa: 'Nota Fiscal de Entrada' realizada com sucesso", style="bold green")
        else:
            logger.info(f"\nError Message: {return_login["retorno"]}")
            console.print(f"\nError Message: {return_login["retorno"]}", style="bold red")
            return return_login
        
        await worker_sleep(10)
        #Procura campo documento
        model  = select_model_capa()
        if model['sucesso'] == True:
            console.log(model['retorno'], style='bold green')
        else:
            return {"sucesso": False, "retorno": f"{model['retorno']}"}

        #Clica em 'Importar-Nfe'
        imported_nfe  = import_nfe()
        if imported_nfe['sucesso'] == True:
            console.log(imported_nfe['retorno'], style='bold green')
        else:
            return {"sucesso": False, "retorno": f"{import_nfe['retorno']}"}

        await worker_sleep(10)

        # Download XML
        get_gcp_token = sync_get_config_by_name("GCP_SERVICE_ACCOUNT")
        get_gcp_credentials = sync_get_config_by_name("GCP_CREDENTIALS")
        env_config, _ = load_env_config()

        download_xml(env_config["XML_DEFAULT_FOLDER"], get_gcp_token, get_gcp_credentials, nota["nfe"])

        # Permanece 'XML'
        #Clica em  'OK' para selecionar
        pyautogui.click(970, 666)
        await worker_sleep(3)

        # Click Downloads
        get_xml(nota["nfe"])

        # Deleta o xml
        delete_xml(nota["nfe"])

        # Configura a natureza
        config_natureza()

        # Configura o almoxarifado
        config_almoxarifado(nota["observacoes"].split(" ")[0])

        # Verifica os itens na nota
        check_itens_nota()

        # Verifica se as configs de pagamento estao ok
        check_pagamento()

        # Finaliza a importacao
        finalizar_importacao()

    except Exception as ex:
        observacao = f"Erro Processo Entrada de Notas: {str(ex)}"
        logger.error(observacao)
        console.print(observacao, style="bold red")
        return {"sucesso": False, "retorno": observacao}
