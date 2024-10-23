import asyncio

from rich.console import Console

from worker_automate_hub.core.so_manipulation import update_assets

console = Console()


async def playground(task):
    console.print(f"\nProcesso de teste iniciado: {task}\n", style="green")
    for numero in range(1, 5):
        console.print(f"Etapa [{numero}] de 5", style="green")
        await asyncio.sleep(1)
    console.print(f"Processo de teste finalizado.", style="green")
    return {"sucesso": True, "mensagem": "Processo de teste executado com sucesso"}


if __name__ == "__main__":
    task_fake = {}
    asyncio.run(playground(task_fake))