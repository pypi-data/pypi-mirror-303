import warnings

import pyautogui
from pywinauto.application import Application
from pywinauto_recorder.player import set_combobox
from rich.console import Console

from worker_automate_hub.api.client import (
    get_config_by_name,
    sync_get_config_by_name,
)
from worker_automate_hub.config.settings import load_env_config
from worker_automate_hub.models.dto.rpa_historico_request_dto import (
    RpaHistoricoStatusEnum,
    RpaRetornoProcessoDTO,
)
from worker_automate_hub.models.dto.rpa_processo_entrada_dto import (
    RpaProcessoEntradaDTO,
)
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import (
    delete_xml,
    download_xml,
    error_after_xml_imported,
    get_xml,
    import_nfe,
    incluir_registro,
    is_window_open,
    is_window_open_by_class,
    itens_not_found_supplier,
    kill_process,
    login_emsys,
    select_documento_type,
    set_variable,
    type_text_into_field,
    verify_nf_incuded,
    warnings_after_xml_imported,
    worker_sleep,
)

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False
console = Console()


async def entrada_de_notas_505(task: RpaProcessoEntradaDTO) -> RpaRetornoProcessoDTO:
    """
    Processo que relazia entrada de notas no ERP EMSys(Linx).

    """
    try:
        # Get config from BOF
        config = await get_config_by_name("login_emsys")
        console.print(task)

        # Seta config entrada na var nota para melhor entendimento
        nota = task.configEntrada
        multiplicador_timeout = int(float(task.sistemas[0].timeout))
        set_variable("timeout_multiplicador", multiplicador_timeout)

        # Fecha a instancia do emsys - caso esteja aberta
        await kill_process("EMSys")

        # Download XML
        get_gcp_token = sync_get_config_by_name("GCP_SERVICE_ACCOUNT")
        get_gcp_credentials = sync_get_config_by_name("GCP_CREDENTIALS")
        env_config, _ = load_env_config()

        console.log("Verificando a existência do Arquivo XML...\n")
        download_result = await download_xml(
            env_config["XML_DEFAULT_FOLDER"],
            get_gcp_token,
            get_gcp_credentials,
            nota.get("nfe"),
        )
        if download_result.sucesso == True:
            console.log("Download do XML realizado com sucesso", style="bold green")
        else:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=download_result.retorno,
                status=RpaHistoricoStatusEnum.Falha,
            )

        app = Application(backend="win32").start("C:\\Rezende\\EMSys3\\EMSys3.exe")
        warnings.filterwarnings(
            "ignore",
            category=UserWarning,
            message="32-bit application should be automated using 32-bit Python",
        )
        console.print("\nEMSys iniciando...", style="bold green")
        return_login = await login_emsys(config.conConfiguracao, app, task)

        if return_login.sucesso == True:
            type_text_into_field(
                "Nota Fiscal de Entrada", app["TFrmMenuPrincipal"]["Edit"], True, "50"
            )
            pyautogui.press("enter")
            await worker_sleep(2)
            pyautogui.press("enter")
            console.print(
                f"\nPesquisa: 'Nota Fiscal de Entrada' realizada com sucesso",
                style="bold green",
            )
        else:
            logger.info(f"\nError Message: {return_login.retorno}")
            console.print(f"\nError Message: {return_login.retorno}", style="bold red")
            return return_login

        await worker_sleep(6)
        # Procura campo documento
        console.print("Navegando pela Janela de Nota Fiscal de Entrada...\n")
        document_type = await select_documento_type(
            "NOTA FISCAL DE ENTRADA ELETRONICA - DANFE"
        )
        if document_type.sucesso == True:
            console.log(document_type.retorno, style="bold green")
        else:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=document_type.retorno,
                status=RpaHistoricoStatusEnum.Falha,
            )

        await worker_sleep(4)

        # Clica em 'Importar-Nfe'
        imported_nfe = await import_nfe()
        if imported_nfe.sucesso == True:
            console.log(imported_nfe.retorno, style="bold green")
        else:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=imported_nfe.retorno,
                status=RpaHistoricoStatusEnum.Falha,
            )

        await worker_sleep(5)

        await get_xml(nota.get("nfe"))
        await worker_sleep(3)

        # VERIFICANDO A EXISTENCIA DE WARNINGS
        await worker_sleep(4)

        warning_pop_up = await is_window_open("Warning")
        if warning_pop_up["IsOpened"] == True:
            warning_work = await warnings_after_xml_imported()
            if warning_work.sucesso == True:
                console.log(warning_work.retorno, style="bold green")
            else:
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=warning_work.retorno,
                    status=RpaHistoricoStatusEnum.Falha,
                )

        # VERIFICANDO A EXISTENCIA DE ERRO
        erro_pop_up = await is_window_open("Erro")
        if erro_pop_up["IsOpened"] == True:
            error_work = await error_after_xml_imported()
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=error_work.retorno,
                status=RpaHistoricoStatusEnum.Falha,
            )

        app = Application().connect(
            title="Informações para importação da Nota Fiscal Eletrônica"
        )
        main_window = app["Informações para importação da Nota Fiscal Eletrônica"]

        # INTERAGINDO COM A NATUREZA DA OPERACAO
        cfop = int(nota.get("cfop"))
        console.print(f"Inserindo a informação da CFOP, caso se aplique {cfop} ...\n")
        if cfop == 5104 or str(cfop).startswith("51"):
            combo_box_natureza_operacao = main_window.child_window(
                class_name="TDBIComboBox", found_index=0
            )
            combo_box_natureza_operacao.click()

            await worker_sleep(3)
            set_combobox("||List", "1102-COMPRA DE MERCADORIA ADQ. TERCEIROS - 1.102")
            await worker_sleep(3)
        elif cfop == 6102 or str(cfop).startswith("61"):
            combo_box_natureza_operacao = main_window.child_window(
                class_name="TDBIComboBox", found_index=0
            )
            combo_box_natureza_operacao.click()

            await worker_sleep(3)
            set_combobox("||List", "2102-COMPRA DE MERCADORIAS SEM DIFAL - 2.102")
            await worker_sleep(3)
        else:
            console.print(
                "Erro mapeado, CFOP diferente de 6102 ou 5104/51, necessario ação manual ou ajuste no robo...\n"
            )
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno="Erro mapeado, CFOP diferente de 5655 ou 56, necessario ação manual ou ajuste no robo",
                status=RpaHistoricoStatusEnum.Falha,
            )

        # INTERAGINDO COM O CAMPO ALMOXARIFADO
        filialEmpresaOrigem = nota.get("filialEmpresaOrigem")
        console.print(
            f"Inserindo a informação do Almoxarifado {filialEmpresaOrigem} ...\n"
        )
        # task_bar_toast("Teste toast bar", f"Inserindo a informação do Almoxarifado {filialEmpresaOrigem} ...", 'Worker', 10)
        # show_toast("Teste toast", f"Inserindo a informação do Almoxarifado {filialEmpresaOrigem} ...")
        try:
            new_app = Application(backend="uia").connect(
                title="Informações para importação da Nota Fiscal Eletrônica"
            )
            window = new_app["Informações para importação da Nota Fiscal Eletrônica"]
            edit = window.child_window(
                class_name="TDBIEditCode", found_index=3, control_type="Edit"
            )
            valor_almoxarifado = filialEmpresaOrigem + "50"
            edit.set_edit_text(valor_almoxarifado)
            edit.type_keys("{TAB}")
        except Exception as e:
            console.print(f"Erro ao iterar itens de almoxarifado: {e}")
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=f"Erro ao iterar itens de almoxarifado: {e}",
                status=RpaHistoricoStatusEnum.Falha,
            )

        await worker_sleep(2)
        console.print("Clicando em OK... \n")
        try:
            btn_ok = main_window.child_window(title="Ok")
            btn_ok.click()
        except:
            btn_ok = main_window.child_window(title="&Ok")
            btn_ok.click()
        await worker_sleep(6)

        max_attempts = 3
        i = 0
        while i < max_attempts:
            console.print("Clicando no botão de OK...\n")
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

            console.print(
                "Verificando a existencia da tela Informações para importação da Nota Fiscal Eletrônica...\n"
            )

            try:
                informacao_nf_eletronica = await is_window_open(
                    "Informações para importação da Nota Fiscal Eletrônica"
                )
                if informacao_nf_eletronica["IsOpened"] == False:
                    console.print(
                        "Tela Informações para importação da Nota Fiscal Eletrônica fechada, seguindo com o processo"
                    )
                    break
            except Exception as e:
                console.print(
                    f"Tela Informações para importação da Nota Fiscal Eletrônica encontrada. Tentativa {i + 1}/{max_attempts}."
                )

            i += 1

        if i == max_attempts:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=f"Número máximo de tentativas atingido, Não foi possivel finalizar os trabalhos na tela de Informações para importação da Nota Fiscal Eletrônica",
                status=RpaHistoricoStatusEnum.Falha,
            )

        console.print(
            "Verificando a existencia de POP-UP de Itens não localizados ou NCM ...\n"
        )
        itens_by_supplier = await is_window_open_by_class("TFrmAguarde", "TMessageForm")
        if itens_by_supplier["IsOpened"] == True:
            itens_by_supplier_work = await itens_not_found_supplier(nota.get("nfe"))
            if itens_by_supplier_work.get("window") == "NCM":
                console.log(itens_by_supplier_work["retorno"], style="bold green")
            else:
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=itens_by_supplier_work["retorno"],
                    status=RpaHistoricoStatusEnum.Falha,
                )

        await worker_sleep(6)

        max_attempts = 7
        i = 0
        while i < max_attempts:
            await worker_sleep(2)
            aguarde_aberta = False
            from pywinauto import Desktop

            for window in Desktop(backend="uia").windows():
                if "Aguarde" in window.window_text():
                    aguarde_aberta = True
                    console.print("A janela 'Aguarde' está aberta. Aguardando...\n")
                    break

            i += 1

            if not aguarde_aberta:
                console.print(
                    "A janela 'Aguarde' foi fechada. Continuando para encerramento do processo...\n"
                )
                break

        if i == max_attempts:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno="Número máximo de tentativas atingido. A tela para Aguarde não foi encerrada.",
                status=RpaHistoricoStatusEnum.Falha,
            )

        # Inclui registro
        console.print(f"Incluindo registro...\n")
        await worker_sleep(6)
        try:
            ASSETS_PATH = "assets"
            inserir_registro = pyautogui.locateOnScreen(
                ASSETS_PATH + "\\entrada_notas\\IncluirRegistro.png", confidence=0.8
            )
            pyautogui.click(inserir_registro)
        except Exception as e:
            console.print(
                f"Não foi possivel incluir o registro utilizando reconhecimento de imagem, Error: {e}...\n tentando inserir via posição...\n"
            )
            await incluir_registro()

        await worker_sleep(6)
        retorno = False
        try:
            app = Application().connect(class_name="TFrmNotaFiscalEntrada")
            main_window = app["Information"]

            main_window.set_focus()

            console.print(f"Tentando clicar no Botão OK...\n")
            btn_ok = main_window.child_window(class_name="TButton")

            if btn_ok.exists():
                btn_ok.click()
                retorno = True
            else:
                console.print(f" botão OK Não enontrado")
                retorno = await verify_nf_incuded()

        except Exception as e:
            console.print(f"Erro ao conectar à janela Information: {e}\n")
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=f"Erro em obter o retorno, Nota inserida com sucesso, erro {e}",
                status=RpaHistoricoStatusEnum.Falha,
            )

        if retorno:
            console.print("\nNota lançada com sucesso...", style="bold green")
            await worker_sleep(6)
            return RpaRetornoProcessoDTO(
                sucesso=True,
                retorno="Nota Lançada com sucesso!",
                status=RpaHistoricoStatusEnum.Sucesso,
            )

        else:
            console.print("Erro ao lançar nota", style="bold red")
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno="Erro ao lançar nota",
                status=RpaHistoricoStatusEnum.Falha,
            )

    except Exception as ex:
        observacao = f"Erro Processo Entrada de Notas: {str(ex)}"
        logger.error(observacao)
        console.print(observacao, style="bold red")
        return RpaRetornoProcessoDTO(
            sucesso=False,
            retorno=observacao,
            status=RpaHistoricoStatusEnum.Falha,
        )

    finally:
        await kill_process("EMSys")
        # Deleta o xml - caso ja tenha baixado
        await delete_xml(nota.get("nfe"))
