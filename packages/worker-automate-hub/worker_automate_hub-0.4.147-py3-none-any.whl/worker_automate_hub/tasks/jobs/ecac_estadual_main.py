from worker_automate_hub.tasks.jobs.ecac_estadual_go import ecac_estadual_go
from worker_automate_hub.tasks.jobs.ecac_estadual_mt import ecac_estadual_mt
from worker_automate_hub.tasks.jobs.ecac_estadual_sp import ecac_estadual_sp
from worker_automate_hub.tasks.jobs.ecac_estadual_sc import ecac_estadual_sc


async def ecac_estadual_main(task):
    try:
        task_process = task['configEntrada']['Estado']
    except Exception as e:
        return {"sucesso": False, "retorno": f"Não foi possivel iniciar o processo, pois o Estado não foi provisionado"}

    if task_process == 'GO':
        result = await ecac_estadual_go(task)
        return result
    elif task_process == 'MT':
        result = await ecac_estadual_mt(task)
        return result
    elif task_process == 'SP':
        result = await ecac_estadual_sp(task)
        return result
    elif task_process == 'SC':
        result = await ecac_estadual_sc(task)
        return result
    else:
        return {"sucesso": False, "retorno": f"Estado não mapeado ou desenvolvimento não concluido, {task_process}"}