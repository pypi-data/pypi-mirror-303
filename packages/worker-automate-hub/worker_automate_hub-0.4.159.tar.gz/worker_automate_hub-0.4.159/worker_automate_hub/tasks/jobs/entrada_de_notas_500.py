import warnings

import pyautogui
from pywinauto.application import Application
from rich.console import Console

from worker_automate_hub.api.client import (
    get_config_by_name,
)
from worker_automate_hub.models.dto.rpa_historico_request_dto import (
    RpaHistoricoStatusEnum,
    RpaRetornoProcessoDTO,
)
from worker_automate_hub.models.dto.rpa_processo_entrada_dto import (
    RpaProcessoEntradaDTO,
)
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import (
    check_pagamento_transferencia_cd,
    import_nfe,
    importar_notas_outras_empresas,
    incluir_registro,
    kill_process,
    login_emsys,
    preencher_valor_restante,
    select_model_capa,
    set_variable,
    type_text_into_field,
    worker_sleep,
)

pyautogui.PAUSE = 0.5
console = Console()


async def entrada_de_notas_500(task: RpaProcessoEntradaDTO) -> RpaRetornoProcessoDTO:
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

        # Abre um novo emsys
        await kill_process("EMSys")
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
            await worker_sleep(1)
            pyautogui.press("enter")
            console.print(
                f"\nPesquisa: 'Nota Fiscal de Entrada' realizada com sucesso",
                style="bold green",
            )
        else:
            logger.info(f"\nError Message: {return_login.retorno}")
            console.print(f"\nError Message: {return_login.retorno}", style="bold red")
            return return_login

        await worker_sleep(10)
        # Procura campo documento
        model = select_model_capa()
        if model.sucesso == True:
            console.log(model.retorno, style="bold green")
        else:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=model.retorno,
                status=RpaHistoricoStatusEnum.Falha,
            )

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

        # Clica em Notas de Outras Empresas
        pyautogui.click(824, 547)
        await worker_sleep(2)

        # Clica em  'OK' para selecionar
        pyautogui.click(975, 674)
        await worker_sleep(2)

        importar_notas_outras_empresas(nota.get("dataEmissao"), nota.get("numeroNota"))

        # Verifica se as configs de pagamento estao ok
        check_pagamento_transferencia_cd()

        # Preenche valor restante
        preencher_valor_restante(nota.get("valorNota"))

        # Inclui registro
        await incluir_registro()

        # Sem retorno positivo ou não finalizado?

    except Exception as ex:
        observacao = f"Erro Processo Entrada de Notas: {str(ex)}"
        logger.error(observacao)
        console.print(observacao, style="bold red")
        return RpaRetornoProcessoDTO(
            sucesso=False,
            retorno=observacao,
            status=RpaHistoricoStatusEnum.Falha,
        )
