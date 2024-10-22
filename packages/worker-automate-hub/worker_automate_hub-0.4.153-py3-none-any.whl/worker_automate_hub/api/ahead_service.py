import aiohttp

from worker_automate_hub.config.settings import load_env_config
from worker_automate_hub.utils.logger import logger


async def get_xml(chave_acesso: str):
    env_config, _ = load_env_config()
    try:
        headers_bearer = {"Authorization": f"Bearer {env_config['API_TOKEN']}"}

        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
        ) as session:
            async with session.get(
                f"{env_config['API_BASE_URL']}/api/Dados/ObterXml",
                params={"ChaveAcesso": chave_acesso},
                headers=headers_bearer,
            ) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    err_msg = (
                        f"Erro ao obter o XML: {response.status} - {response.reason}"
                    )
                    logger.error(err_msg)
                    return None
    except Exception as e:
        err_msg = f"Erro ao obter o XML: {e}"
        logger.error(err_msg)
        return None
