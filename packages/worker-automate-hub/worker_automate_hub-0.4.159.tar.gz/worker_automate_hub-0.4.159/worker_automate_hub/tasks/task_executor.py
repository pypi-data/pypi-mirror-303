from datetime import datetime

from pytz import timezone
from rich.console import Console

from worker_automate_hub.api.client import get_processo, unlock_queue
from worker_automate_hub.api.rpa_historico_service import store, update
from worker_automate_hub.models.dao.rpa_historico import RpaHistorico
from worker_automate_hub.models.dao.rpa_processo import RpaProcesso
from worker_automate_hub.models.dto.rpa_historico_request_dto import (
    RpaHistoricoRequestDTO,
    RpaHistoricoStatusEnum,
    RpaRetornoProcessoDTO,
)
from worker_automate_hub.models.dto.rpa_processo_entrada_dto import (
    RpaProcessoEntradaDTO,
)
from worker_automate_hub.tasks.task_definitions import task_definitions
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import capture_and_send_screenshot

console = Console()


async def perform_task(task: RpaProcessoEntradaDTO):
    log_msg = f"Processo a ser executado: {task.nomProcesso}"
    console.print(f"\n{log_msg}\n", style="green")
    logger.info(log_msg)
    task_uuid = task.uuidProcesso
    processo: RpaProcesso = await get_processo(task_uuid)
    registrar_historico = True
    if registrar_historico:
        historico: RpaHistorico = await _store_historico(task, processo)
    try:
        if task_uuid in task_definitions:
            # Executar a task
            result: RpaRetornoProcessoDTO = await task_definitions[task_uuid](task)
            if registrar_historico:
                await _update_historico(
                    historico_uuid=historico.uuidHistorico,
                    task=task,
                    retorno_processo=result,
                    processo=processo,
                )

            if result.sucesso == False:
                await capture_and_send_screenshot(
                    uuidRelacao=historico.uuidHistorico, desArquivo=result.retorno
                )
            return result
        else:
            err_msg = f"Processo não encontrado: {task_uuid}"
            console.print(err_msg, style="yellow")
            logger.error(err_msg)
            if registrar_historico:
                await _update_historico(
                    historico_uuid=historico.uuidHistorico,
                    task=task,
                    retorno_processo=RpaRetornoProcessoDTO(
                        sucesso=False,
                        retorno=err_msg,
                        status=RpaHistoricoStatusEnum.Falha,
                    ),
                    processo=processo,
                )
            await unlock_queue(task.uuidFila)
            return None
    except Exception as e:
        err_msg = f"Erro ao performar o processo: {e}"
        console.print(f"\n{err_msg}\n", style="red")
        logger.error(err_msg)
        if registrar_historico:
            await _update_historico(
                historico_uuid=historico.uuidHistorico,
                task=task,
                retorno_processo=RpaRetornoProcessoDTO(
                    sucesso=False, retorno=err_msg, status=RpaHistoricoStatusEnum.Falha
                ),
                processo=processo,
            )
        await capture_and_send_screenshot(
            uuidRelacao=historico.uuidHistorico, desArquivo=err_msg
        )


async def _store_historico(
    task: RpaProcessoEntradaDTO, processo: RpaProcesso
) -> RpaHistorico:
    """
    Salva o histórico de um processo com status Processando.

    Recebe um RpaProcessoEntradaDTO e um RpaProcesso como parâmetro e salva o
    histórico com status Processando. Retorna um dicionário com o uuid do
    histórico salvo.

    Args:
        task (RpaProcessoEntradaDTO): O processo a ser salvo.
        processo (RpaProcesso): O processo que está sendo executado.

    Returns:
        RpaHistorico: Dicionário com o uuid do histórico salvo.
    """
    try:
        from worker_automate_hub.config.settings import load_worker_config

        worker_config = load_worker_config()
        tz = timezone("America/Sao_Paulo")
        start_time = datetime.now(tz).isoformat()

        # Armazenar início da operação no histórico
        start_data = RpaHistoricoRequestDTO(
            uuidProcesso=task.uuidProcesso,
            uuidRobo=worker_config["UUID_ROBO"],
            prioridade=processo.prioridade,
            desStatus=RpaHistoricoStatusEnum.Processando,
            configEntrada=task.configEntrada,
            datInicioExecucao=start_time,
            datEntradaFila=task.datEntradaFila,
            identificador=task.configEntrada.get("nfe", ""),
        )

        store_response: RpaHistorico = await store(start_data)
        console.print(
            f"\nHistorico salvo com o uuid: {store_response.uuidHistorico}\n",
            style="green",
        )
        return store_response
    except Exception as e:
        err_msg = f"Erro ao salvar o registro no histórico: {e}"
        console.print(f"\n{err_msg}\n", style="red")
        logger.error(f"{err_msg}")


async def _update_historico(
    historico_uuid: str,
    task: RpaProcessoEntradaDTO,
    retorno_processo: RpaRetornoProcessoDTO,
    processo: RpaProcesso,
):
    """
    Atualiza o histórico de um processo com o status de sucesso ou falha.

    Recebe o uuid do histórico, o RpaProcessoEntradaDTO do processo, um booleano
    indicando se o processo foi um sucesso ou não, o RpaRetornoProcessoDTO do
    processo e o RpaProcesso do processo como parâmetro e atualiza o histórico
    com o status de sucesso ou falha. Retorna um dicionário com o uuid do
    histórico atualizado.

    Args:
        historico_uuid (str): O uuid do histórico.
        task (RpaProcessoEntradaDTO): O RpaProcessoEntradaDTO do processo.
        sucesso (bool): Um booleano indicando se o processo foi um sucesso ou não.
        retorno_processo (RpaRetornoProcessoDTO): O RpaRetornoProcessoDTO do processo.
        processo (RpaProcesso): O RpaProcesso do processo.

    Returns:
        RpaHistorico: Dicionário com o uuid do histórico atualizado.
    """

    try:
        from worker_automate_hub.config.settings import load_worker_config

        worker_config = load_worker_config()
        tz = timezone("America/Sao_Paulo")
        des_status: RpaHistoricoStatusEnum = retorno_processo.status
        end_time = datetime.now(tz).isoformat()

        # Armazenar fim da operação no histórico
        end_data = RpaHistoricoRequestDTO(
            uuidHistorico=historico_uuid,
            uuidProcesso=task.uuidProcesso,
            uuidRobo=worker_config["UUID_ROBO"],
            prioridade=processo.prioridade,
            desStatus=des_status,
            configEntrada=task.configEntrada,
            retorno=retorno_processo,
            datFimExecucao=end_time,
            identificador=task.configEntrada.get("nfe", ""),
        )

        update_response: RpaHistorico = await update(end_data)
        console.print(
            f"\nHistorico atualizado com o uuid: {update_response.uuidHistorico}\n",
            style="green",
        )
        return update_response

    except Exception as e:
        err_msg = f"Erro ao atualizar o histórico do processo: {e}"
        console.print(f"\n{err_msg}\n", style="red")
        logger.error(err_msg)
