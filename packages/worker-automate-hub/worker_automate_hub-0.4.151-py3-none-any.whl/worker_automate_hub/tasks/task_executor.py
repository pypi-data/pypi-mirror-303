from datetime import datetime

from pytz import timezone
from rich.console import Console

from worker_automate_hub.api.client import get_processo, unlock_queue
from worker_automate_hub.api.rpa_historico_service import store, update
from worker_automate_hub.models.dto.rpa_hitorico_dto import (
    RpaHistoricoDTO,
    RpaHistoricoStatusEnum,
)
from worker_automate_hub.tasks.task_definitions import task_definitions
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import capture_and_send_screenshot

console = Console()


async def perform_task(task):
    log_msg = f"Processo a ser executado: {task['nomProcesso']}"
    console.print(f"\n{log_msg}\n", style="green")
    logger.info(log_msg)
    task_uuid = task["uuidProcesso"]
    processo = await get_processo(task_uuid)
    historico = await _store_historico(task, processo)
    try:
        if task_uuid in task_definitions:
            result = await task_definitions[task_uuid](task)
            await _update_historico(
                historico["success"]["uuidHistorico"],
                task,
                result["sucesso"],
                result,
                processo,
            )
            if result["sucesso"] == False:
                await capture_and_send_screenshot(uuidRelacao=historico["success"]["uuidHistorico"], desArquivo=result["retorno"])
            return result
        else:
            err_msg = f"Processo não encontrado: {task_uuid}"
            console.print(err_msg, style="yellow")
            logger.error(err_msg)
            await _update_historico(
                historico["success"]["uuidHistorico"],
                task,
                False,
                {"sucesso": False, "retorno": err_msg},
                processo,
            )
            await unlock_queue(task["uuidFila"])
            return None
    except Exception as e:
        err_msg = f"Erro ao performar o processo: {e}"
        console.print(f"\n{err_msg}\n", style="red")
        logger.error(err_msg)

        await _update_historico(
            historico["success"]["uuidHistorico"],
            task,
            False,
            {"sucesso": False, "retorno": err_msg},
            processo,
        )
        await capture_and_send_screenshot(uuidRelacao=historico["success"]["uuidHistorico"], desArquivo=err_msg)


async def _store_historico(task: dict, processo: dict):
    try:
        from worker_automate_hub.config.settings import load_worker_config

        worker_config = load_worker_config()
        tz = timezone("America/Sao_Paulo")
        start_time = datetime.now(tz).isoformat()

        # Armazenar início da operação no histórico
        start_data = RpaHistoricoDTO(
            uuidProcesso=task["uuidProcesso"],
            uuidRobo=worker_config["UUID_ROBO"],
            prioridade=processo["prioridade"],
            desStatus=RpaHistoricoStatusEnum.Processando,
            configEntrada=task["configEntrada"],
            datInicioExecucao=start_time,
            datEntradaFila=task["datEntradaFila"],
            identificador=task.get('configEntrada', {}).get('nfe'),
        )

        store_response = await store(start_data)
        console.print(f"\nHistorico salvo com o uuid: {store_response["success"]["uuidHistorico"]}\n", style="green")
        return store_response
    except Exception as e:
        console.print(f"Erro ao salvar o histórico do processo: {e}\n", style="red")
        logger.error(f"Erro ao salvar o histórico do processo: {e}")


async def _update_historico(
    historico_uuid: str,
    task: dict,
    sucesso: bool,
    retorno_processo: dict,
    processo: dict,
):
    try:
        from worker_automate_hub.config.settings import load_worker_config

        worker_config = load_worker_config()
        tz = timezone("America/Sao_Paulo")
        des_status = (
            RpaHistoricoStatusEnum.Sucesso if sucesso else RpaHistoricoStatusEnum.Falha
        )
        end_time = datetime.now(tz).isoformat()

        # Armazenar fim da operação no histórico
        end_data = RpaHistoricoDTO(
            uuidHistorico=historico_uuid,
            uuidProcesso=task["uuidProcesso"],
            uuidRobo=worker_config["UUID_ROBO"],
            prioridade=processo["prioridade"],
            desStatus=des_status,
            configEntrada=task["configEntrada"],
            retorno=retorno_processo,
            datFimExecucao=end_time,
        )

        update_response = await update(end_data)
        console.print(f"\nHistorico atualizado com o uuid: {update_response["success"]["uuidHistorico"]}\n", style="green")
        return update_response

    except Exception as e:
        err_msg = f"Erro ao atualizar o histórico do processo: {e}"
        console.print(f"\n{err_msg}\n", style="red")
        logger.error(err_msg)
