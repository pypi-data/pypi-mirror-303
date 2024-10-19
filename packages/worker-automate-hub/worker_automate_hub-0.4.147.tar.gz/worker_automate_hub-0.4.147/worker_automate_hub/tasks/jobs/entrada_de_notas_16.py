import asyncio
import warnings

import pyautogui
from pywinauto.application import Application
from pywinauto_recorder.player import (
    set_combobox,
)
from rich.console import Console
from worker_automate_hub.api.client import sync_get_config_by_name

from worker_automate_hub.api.client import get_config_by_name
from worker_automate_hub.config.settings import load_env_config
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import (
    import_nfe,
    kill_process,
    login_emsys,
    type_text_into_field,
    set_variable,
    worker_sleep,
    is_window_open,
    is_window_open_by_class,
    itens_not_found_supplier,
    warnings_after_xml_imported,
)
from worker_automate_hub.utils.utils_nfe_entrada import EMSys

pyautogui.PAUSE = 0.5
console = Console()

emsys = EMSys()

async def entrada_de_notas_16(task):
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
        console.print('Navegando pela Janela de Nota Fiscal de Entrada...\n')
        app = Application().connect(title="Nota Fiscal de Entrada")
        main_window = app["Nota Fiscal de Entrada"]

        console.print("Controles encontrados na janela 'Nota Fiscal de Entrada, navegando entre eles...\n")
        panel_TNotebook = main_window.child_window(class_name="TNotebook", found_index=0)
        panel_TPage = panel_TNotebook.child_window(class_name="TPage", found_index=0)
        panel_TPageControl = panel_TPage.child_window(class_name="TPageControl", found_index=0)
        panel_TTabSheet = panel_TPageControl.child_window(class_name="TTabSheet", found_index=0)
        combo_box_tipo_documento = panel_TTabSheet.child_window(class_name="TDBIComboBox", found_index=1)
        combo_box_tipo_documento.click()
        console.print("Clique select box, Tipo de documento realizado com sucesso, selecionando o tipo de documento...\n")

        await worker_sleep(2)

        set_combobox("||List", "NOTA FISCAL DE ENTRADA ELETRONICA - DANFE")
        console.print("Tipo de documento 'NOTA FISCAL DE ENTRADA ELETRONICA - DANFE', selecionado com sucesso...\n")

        await worker_sleep(4)

        #Clica em 'Importar-Nfe'
        imported_nfe  = await import_nfe()
        if imported_nfe['sucesso'] == True:
            console.log(imported_nfe['retorno'], style='bold green')
        else:
            return {"sucesso": False, "retorno": f"{import_nfe['retorno']}"}

        await worker_sleep(10)

        # Download XML
        get_gcp_token = sync_get_config_by_name("GCP_SERVICE_ACCOUNT")
        get_gcp_credentials = sync_get_config_by_name("GCP_CREDENTIALS")
        env_config, _ = load_env_config()

        await emsys.download_xml(env_config["XML_DEFAULT_FOLDER"], get_gcp_token, get_gcp_credentials, nota["nfe"])

         # Permanece 'XML'
        #Clica em  'OK' para selecionar
        pyautogui.click(970, 666)
        await worker_sleep(3)

        # Click Downloads
        await emsys.get_xml(nota["nfe"])
        await worker_sleep(30)

        warning_pop_up = await is_window_open("Warning")
        if warning_pop_up['IsOpened'] == True:
            warning_work = await warnings_after_xml_imported()
            if warning_work['sucesso'] == True:
                console.log(warning_work['retorno'], style='bold green')
            else:
                return {"sucesso": False, "retorno": f"{warning_work['retorno']}"}

        # Deleta o xml
        await emsys.delete_xml(nota["nfe"])
        await worker_sleep(5)

        app = Application().connect(title="Informações para importação da Nota Fiscal Eletrônica")
        main_window = app["Informações para importação da Nota Fiscal Eletrônica"]

        if nota["cfop"]:
            console.print(f"Inserindo a informação da CFOP, caso se aplique {nota["cfop"]} ...\n")
            if nota["cfop"] != "5910":
                combo_box_natureza_operacao = main_window.child_window(class_name="TDBIComboBox", found_index=0)
                combo_box_natureza_operacao.click()
                await worker_sleep(3)
                set_combobox("||List", "1403 - COMPRA DE MERCADORIAS- 1.403")
                await worker_sleep(3)
            else:
                combo_box_natureza_operacao = main_window.child_window(class_name="TDBIComboBox", found_index=0)
                combo_box_natureza_operacao.click()
                await worker_sleep(3)
                set_combobox("||List", "1910 - ENTRADA DE BONIFICACAO- COM ESTOQUE- 1910")
                await worker_sleep(3)

        #INTERAGINDO COM O CAMPO ALMOXARIFADO
        filial_empresa_origem = nota["filialEmpresaOrigem"]
        valor_almoxarifado = filial_empresa_origem + "50"
        pyautogui.press('tab')
        pyautogui.write(valor_almoxarifado)
        await worker_sleep(2)
        pyautogui.press('tab')

        await worker_sleep(3)
        #INTERAGINDO COM CHECKBOX Utilizar unidade de agrupamento dos itens
        fornecedor = nota["nomeFornecedor"]
        console.print(f"Fornecedor: {fornecedor} ...\n")
        console.print(f"Sim, nota emitida para: {fornecedor}, marcando o agrupar por unidade de medida...\n")
        checkbox = main_window.child_window(
            title="Utilizar unidade de agrupamento dos itens",
            class_name="TCheckBox",
            # control_type="TCheckBox",
        )
        if not checkbox.is_checked():
            checkbox.check()
            console.print("Realizado o agrupamento por unidade de medida... \n")

        await worker_sleep(5)
        console.print("Clicando em OK... \n")
        
        max_attempts = 3
        i = 0
        while i < max_attempts:
            console.print('Clicando no botão de OK...\n')
            try:
                try:
                    btn_ok = main_window.child_window(title="Ok")
                    btn_ok.click()
                except:
                    btn_ok = main_window.child_window(title="&Ok")
                    btn_ok.click()
            except:
                console.print("Não foi possivel clicar no Botão OK... \n")

            await worker_sleep(3)

            console.print("Verificando a existencia da tela Informações para importação da Nota Fiscal Eletrônica...\n")

            try:
                informacao_nf_eletronica = await is_window_open("Informações para importação da Nota Fiscal Eletrônica")
                if informacao_nf_eletronica['IsOpened'] == False:
                    console.print("Tela Informações para importação da Nota Fiscal Eletrônica fechada, seguindo com o processo")
                    break
            except Exception as e:
                console.print(f"Tela Informações para importação da Nota Fiscal Eletrônica encontrada. Tentativa {i + 1}/{max_attempts}.")

            i += 1
        
        if i == max_attempts:
            return {"sucesso": False, "retorno": f"Número máximo de tentativas atingido, Não foi possivel finalizar os trabalhos na tela de Informações para importação da Nota Fiscal Eletrônica"}

        await worker_sleep(6)

        console.print("Verificando a existencia de POP-UP de Itens não localizados ou NCM ...\n")
        itens_by_supplier = await is_window_open_by_class("TFrmAguarde", "TMessageForm")
        if itens_by_supplier['IsOpened'] == True:
            itens_by_supplier_work = await itens_not_found_supplier(nota["nfe"])
            if itens_by_supplier_work['window'] == "NCM":
                console.log(itens_by_supplier_work['retorno'], style='bold green')
            else:
                return {"sucesso": False, "retorno": f"{itens_by_supplier_work['retorno']}"}

        await worker_sleep(3)
        console.print('Navegando pela Janela de Nota Fiscal de Entrada...\n')
        app = Application().connect(class_name="TFrmNotaFiscalEntrada")
        main_window = app["TFrmNotaFiscalEntrada"]

        main_window.set_focus()

        await emsys.verify_warning_and_error("Information", "&No")

        await worker_sleep(10)
        await emsys.percorrer_grid()
        await emsys.select_tipo_cobranca()
        await emsys.inserir_vencimento_e_valor(nota["dataVencimento"], nota["valorNota"])
        await worker_sleep(5)
        await emsys.incluir_registro()
        await worker_sleep(5)
        await emsys.verify_warning_and_error("Warning", "OK")
        await emsys.verify_warning_and_error("Aviso", "OK")
        await worker_sleep(5)
        resultado = await emsys.verify_max_vatiation()

        if resultado["sucesso"] and resultado["sucesso"] == False:
            return resultado
        
        await emsys.incluir_registro()

    except Exception as ex:
        observacao = f"Erro Processo Entrada de Notas: {str(ex)}"
        logger.error(observacao)
        console.print(observacao, style="bold red")
        return {"sucesso": False, "retorno": observacao}
