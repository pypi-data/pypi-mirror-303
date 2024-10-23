import warnings

import pyautogui
import pyperclip
from pywinauto.application import Application
from rich.console import Console

from worker_automate_hub.api.client import get_config_by_name
from worker_automate_hub.models.dto.rpa_historico_request_dto import (
    RpaHistoricoStatusEnum,
    RpaRetornoProcessoDTO,
)
from worker_automate_hub.models.dto.rpa_processo_entrada_dto import (
    RpaProcessoEntradaDTO,
)
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import (
    api_simplifica,
    extract_nf_number,
    faturar_pre_venda,
    find_element_center,
    find_target_position,
    kill_process,
    login_emsys,
    set_variable,
    take_screenshot,
    take_target_position,
    type_text_into_field,
    wait_window_close,
    worker_sleep,
)

console = Console()

ASSETS_BASE_PATH = "assets/descartes_transferencias_images/"
ALMOXARIFADO_DEFAULT = "50"


async def transferencias(task: RpaProcessoEntradaDTO) -> RpaRetornoProcessoDTO:
    try:
        # Inicializa variaveis
        # pre_venda_message = None
        nota_fiscal = [None]
        log_msg = None
        valor_nota = None

        # Get config from BOF
        config = await get_config_by_name("Transferencias_Emsys")
        itens = task.configEntrada.get("itens")
        multiplicador_timeout = int(float(task.sistemas[0].timeout))
        set_variable("timeout_multiplicador", multiplicador_timeout)

        # Obtém a resolução da tela
        screen_width, screen_height = pyautogui.size()

        # Print da resolução
        console.print(f"Largura: {screen_width}, Altura: {screen_height}")

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
                "Cadastro Pré Venda", app["TFrmMenuPrincipal"]["Edit"], True, "50"
            )
            pyautogui.press("enter")
            await worker_sleep(1)
            pyautogui.press("enter")
            console.print(
                f"\nPesquisa: 'Cadastro Pre Venda' realizada com sucesso",
                style="bold green",
            )
        else:
            logger.info(f"\nError Message: {return_login.retorno}")
            console.print(f"\nError Message: {return_login.retorno}", style="bold red")
            return return_login

        await worker_sleep(7)

        # Deveríamos habilitar?
        # Preenche data de validade
        # screenshot_path = take_screenshot()
        # target_pos = find_target_position(screenshot_path, "Validade", 10, 0, 15)
        # if target_pos == None:
        #     return {"sucesso": False, "retorno": f"Não foi possivel encontrar o campo de validade"}

        # Condição da Pré-Venda
        screenshot_path = take_screenshot()
        condicao_field = find_target_position(screenshot_path, "Condição", 10, 0, 15)
        if condicao_field == None:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno="Não foi possivel encontrar o campo de condição",
                status=RpaHistoricoStatusEnum.Falha,
            )

        pyautogui.click(condicao_field)
        await worker_sleep(1)
        pyautogui.write("T")
        await worker_sleep(1)
        pyautogui.press("down")
        pyautogui.press("enter")
        await worker_sleep(1)

        # Preenche o campo do cliente com o número da filial
        cliente_field_position = await find_element_center(
            ASSETS_BASE_PATH + "field_cliente.png", (795, 354, 128, 50), 10
        )
        if cliente_field_position == None:
            cliente_field_position = (884, 384)

        pyautogui.click(cliente_field_position)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("del")
        pyautogui.write(task.configEntrada.get("filialEmpresaOrigem"))
        pyautogui.hotkey("tab")
        await worker_sleep(10)

        # Clica em cancelar na Janela "Busca Representante"
        # screenshot_path = take_screenshot()
        # window_busca_representante_position = take_target_position(screenshot_path, "Representante")
        # if window_busca_representante_position is not None:
        #     button_cancelar_position = find_target_position(screenshot_path, "Cancelar", attempts=15)
        #     pyautogui.click(button_cancelar_position)
        pyautogui.click(1150, 650)

        await worker_sleep(8)

        # Aviso "Deseja alterar a condição de pagamento informada no cadastro do cliente?"
        # screenshot_path = take_screenshot()
        # payment_condition_warning_position = take_target_position(screenshot_path, "pagamento")
        # if payment_condition_warning_position is not None:
        button_no_position = (
            999,
            568,
        )  # find_target_position(screenshot_path, "No", attempts=15)
        pyautogui.click(button_no_position)
        console.print(
            f"\nClicou 'No' Mensagem 'Deseja alterar a condição de pagamento informada no cadastro do cliente?'",
            style="bold green",
        )
        await worker_sleep(10)
        # else:
        #     log_msg = f"\nError Message: Aviso de condição de pagamento não encontrado"
        #     logger.info(log_msg)
        #     console.print(log_msg, style="bold red")

        # Seleciona 'Custo Médio' (Seleção do tipo de preço)
        console.print("Seleciona 'Custo Médio' (Seleção do tipo de preço)...\n")
        # screenshot_path = take_screenshot()
        # custo_medio_select_position = find_target_position(screenshot_path, "Médio", attempts=15)
        # if custo_medio_select_position == None:
        custo_medio_select_position = (851, 523)
        # if custo_medio_select_position is not None:
        pyautogui.click(custo_medio_select_position)
        button_ok_position = (
            1042,
            583,
        )  # find_target_position(screenshot_path, "OK", attempts=15)
        pyautogui.click(button_ok_position)
        await worker_sleep(1)
        console.print(f"\nClicou OK 'Custo médio'", style="bold green")
        await worker_sleep(10)

        # Clica em ok na mensagem "Existem Pré-Vendas em aberto para este cliente."
        screenshot_path = take_screenshot()
        existing_pre_venda_position = find_target_position(
            screenshot_path, "Existem", attempts=15
        )

        if existing_pre_venda_position == None:
            existing_pre_venda_position = await find_element_center(
                ASSETS_BASE_PATH + "existing_pre_venda.png", (831, 437, 247, 156), 15
            )

        if existing_pre_venda_position is not None:
            button_ok_position = (962, 562)
            pyautogui.click(button_ok_position)
            console.print(f"\nClicou OK 'Pre Venda Existente'", style="bold green")
            await worker_sleep(5)
        else:
            log_msg = f"\nError Message: Menssagem de prevenda existente não encontrada"
            logger.info(log_msg)
            console.print(log_msg, style="bold yellow")

        # Define representante para "1"
        screenshot_path = take_screenshot()
        field_representante_position = find_target_position(
            screenshot_path, "Representante", 0, 50, attempts=15
        )

        if field_representante_position == None:
            field_representante_position = await find_element_center(
                ASSETS_BASE_PATH + "field_representante.png", (679, 416, 214, 72), 15
            )
            if field_representante_position is not None:
                lista = list(field_representante_position)
                lista[0] += 50
                lista[1] += 1
                field_representante_position = tuple(lista)

        if field_representante_position is not None:
            pyautogui.doubleClick(field_representante_position)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.hotkey("del")
            pyautogui.write("1")
            pyautogui.hotkey("tab")

        await worker_sleep(3)

        # Abre Menu itens
        menu_itens = await find_element_center(
            ASSETS_BASE_PATH + "menu_itens.png", (526, 286, 152, 45), 10
        )

        if menu_itens == None:
            menu_itens = (570, 317)

        if menu_itens is not None:
            pyautogui.click(menu_itens)
        else:
            log_msg = f'Campo "Itens" no menu da pré-venda não encontrado'
            await api_simplifica(
                task.configEntrada.get("urlRetorno"),
                "ERRO",
                log_msg,
                task.configEntrada.get("uuidSimplifica"),
                nota_fiscal,
                valor_nota,
            )
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=log_msg,
                status=RpaHistoricoStatusEnum.Falha,
            )

        await worker_sleep(2)

        for item in itens:
            screenshot_path = take_screenshot()
            # Clica no botão inclui para abrir a tela de item
            button_incluir = (
                905,
                573,
            )  # find_target_position(screenshot_path, "Incluir", 0, 0, attempts=15)
            if button_incluir is not None:
                pyautogui.click(button_incluir)
                console.print("\nClicou em 'Incluir'", style="bold green")
            else:
                log_msg = f'Botão "Incluir" não encontrado'
                await api_simplifica(
                    task.configEntrada.get("urlRetorno"),
                    "ERRO",
                    log_msg,
                    task.configEntrada.get("uuidSimplifica"),
                    nota_fiscal,
                    valor_nota,
                )
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=log_msg,
                    status=RpaHistoricoStatusEnum.Falha,
                )

            await worker_sleep(3)

            screenshot_path = take_screenshot()
            # Digita Almoxarifado
            field_almoxarifado = (
                839,
                313,
            )  # find_target_position(screenshot_path, "Almoxarifado",0, 129, 15)
            if field_almoxarifado is not None:
                pyautogui.doubleClick(field_almoxarifado)
                pyautogui.hotkey("del")
                pyautogui.write(
                    task.configEntrada.get("filialEmpresaOrigem") + ALMOXARIFADO_DEFAULT
                )
                pyautogui.hotkey("tab")
                await worker_sleep(2)
                console.print(
                    f"\nDigitou almoxarifado {task.configEntrada.get('filialEmpresaOrigem') + ALMOXARIFADO_DEFAULT}",
                    style="bold green",
                )
            else:
                log_msg = f"Campo Almoxarifado não encontrado"
                await api_simplifica(
                    task.configEntrada.get("urlRetorno"),
                    "ERRO",
                    log_msg,
                    task.configEntrada.get("uuidSimplifica"),
                    nota_fiscal,
                    valor_nota,
                )
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=log_msg,
                    status=RpaHistoricoStatusEnum.Falha,
                )

            # Segue para o campo do item
            field_item = (
                841,
                339,
            )  # find_target_position(screenshot_path, "Item", 0, 130, 15)
            if field_item is not None:
                pyautogui.doubleClick(field_item)
                pyautogui.hotkey("del")
                pyautogui.write(item["codigoProduto"])
                pyautogui.hotkey("tab")
                await worker_sleep(2)
                console.print(
                    f"\nDigitou item {item['codigoProduto']}", style="bold green"
                )
            else:
                log_msg = f"Campo Item não encontrado."
                await api_simplifica(
                    task.configEntrada.get("urlRetorno"),
                    "ERRO",
                    log_msg,
                    task.configEntrada.get("uuidSimplifica"),
                    nota_fiscal,
                    valor_nota,
                )
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=log_msg,
                    status=RpaHistoricoStatusEnum.Falha,
                )

            screenshot_path = take_screenshot()

            # Checa tela de pesquisa de item
            window_pesquisa_item = await find_element_center(
                ASSETS_BASE_PATH + "window_pesquisa_item.png", (488, 226, 352, 175), 5
            )

            if window_pesquisa_item is not None:
                observacao = (
                    f"Item {item['codigoProduto']} não encontrado, verificar cadastro"
                )
                console.log(f"{observacao}", style="bold green")
                logger.info(f"{observacao}")
                await api_simplifica(
                    task.configEntrada.get("urlRetorno"),
                    "ERRO",
                    observacao,
                    task.configEntrada.get("uuidSimplifica"),
                    nota_fiscal,
                    valor_nota,
                )
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=observacao,
                    status=RpaHistoricoStatusEnum.Falha,
                )

            console.log(
                f"Produto {item['codigoProduto']} encontrado", style="bold green"
            )
            logger.info(f"Produto {item['codigoProduto']} encontrado")

            # Checa se existe alerta de item sem preço, se existir retorna erro(simplifica e bof)
            warning_price = await find_element_center(
                ASSETS_BASE_PATH + "warning_item_price.png", (824, 426, 255, 191), 5
            )
            if warning_price is not None:
                observacao = f"Item {item['codigoProduto']} não possui preço, verificar erro de estoque ou de bloqueio."
                await api_simplifica(
                    task.configEntrada.get("urlRetorno"),
                    "ERRO",
                    observacao,
                    task.configEntrada.get("uuidSimplifica"),
                    nota_fiscal,
                    valor_nota,
                )
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=observacao,
                    status=RpaHistoricoStatusEnum.Falha,
                )

            screenshot_path = take_screenshot()

            # Seleciona o Saldo Disponivel e verifica se ah possibilidade do descarte
            field_saldo_disponivel = (
                916,
                606,
            )  # find_target_position(screenshot_path + "Saldo", 20, 0, 10)
            if field_saldo_disponivel is not None:
                pyautogui.doubleClick(field_saldo_disponivel)
                await worker_sleep(1)
                pyautogui.doubleClick(field_saldo_disponivel)
                await worker_sleep(1)
                pyautogui.hotkey("ctrl", "c")
                amount_avaliable = ""
                amount_avaliable = pyperclip.paste()
                console.print(
                    f"Saldo Disponivel: '{amount_avaliable}'", style="bold green"
                )

                # Verifica se o saldo disponivel é valido para descartar
                if int(amount_avaliable) > 0 and int(amount_avaliable) >= int(
                    item["qtd"]
                ):
                    field_quantidade = (
                        1047,
                        606,
                    )  # find_target_position(screenshot_path, "Quantidade", 20, 0, 15)
                    pyautogui.doubleClick(field_quantidade)
                    pyautogui.hotkey("del")
                    pyautogui.write(str(item["qtd"]))
                    pyautogui.hotkey("tab")
                    await worker_sleep(2)
                else:
                    log_msg = f"Saldo disponivel: '{amount_avaliable}' é menor que '{item['qtd']}' o valor que deveria ser transferido. Item: '{item['codigoProduto']}'"
                    await api_simplifica(
                        task.configEntrada.get("urlRetorno"),
                        "ERRO",
                        log_msg,
                        task.configEntrada.get("uuidSimplifica"),
                        nota_fiscal,
                        valor_nota,
                    )
                    console.print(log_msg, style="bold red")
                    return RpaRetornoProcessoDTO(
                        sucesso=False,
                        retorno=log_msg,
                        status=RpaHistoricoStatusEnum.Falha,
                    )

            # Clica em incluir para adicionar o item na nota
            button_incluir_item = (
                1007,
                745,
            )  # find_target_position(screenshot_path, "Inlcuir", 0, 0, 15)
            if button_incluir_item is not None:
                pyautogui.click(button_incluir_item)
                await worker_sleep(2)
            else:
                log_msg = f"Botao 'Incluir' item não encontrado"
                await api_simplifica(
                    task.configEntrada.get("urlRetorno"),
                    "ERRO",
                    log_msg,
                    task.configEntrada.get("uuidSimplifica"),
                    nota_fiscal,
                    valor_nota,
                )
                console.print(log_msg, style="bold red")
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=log_msg,
                    status=RpaHistoricoStatusEnum.Falha,
                )

            # Clica em cancelar para fechar a tela e abrir novamente caso houver mais itens
            button_cancela_item = (
                1194,
                745,
            )  # find_target_position(screenshot_path, "Cancela", 0, 0, 15)
            if button_cancela_item is not None:
                pyautogui.click(button_cancela_item)
                await worker_sleep(2)
            else:
                log_msg = f"Botao cancelar para fechar a tela do item nao encontrado"
                await api_simplifica(
                    task.configEntrada.get("urlRetorno"),
                    "ERRO",
                    log_msg,
                    task.configEntrada.get("uuidSimplifica"),
                    nota_fiscal,
                    valor_nota,
                )
                console.print(log_msg, style="bold red")
                return RpaRetornoProcessoDTO(
                    sucesso=False,
                    retorno=log_msg,
                    status=RpaHistoricoStatusEnum.Falha,
                )

        await worker_sleep(5)

        # Volta para Capa
        pyautogui.click(578, 302)

        # Clica no botão "+" no canto superior esquerdo para lançar a pre-venda
        screenshot_path = take_screenshot()
        button_lanca_pre_venda = await find_element_center(
            ASSETS_BASE_PATH + "button_lanca_prevenda.png", (490, 204, 192, 207), 15
        )
        if button_lanca_pre_venda is not None:
            pyautogui.click(button_lanca_pre_venda.x, button_lanca_pre_venda.y)
            console.print("\nLançou Pré-Venda", style="bold green")
        else:
            log_msg = f"Botao lança pre-venda nao encontrado"
            await api_simplifica(
                task.configEntrada.get("urlRetorno"),
                "ERRO",
                log_msg,
                task.configEntrada.get("uuidSimplifica"),
                nota_fiscal,
                valor_nota,
            )
            console.print(log_msg, style="bold red")
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=log_msg,
                status=RpaHistoricoStatusEnum.Falha,
            )

        await worker_sleep(8)

        # Verifica mensagem de "Pré-Venda incluida com número: xxxxx"
        console.print(
            "Verificando mensagem de 'Pré-Venda incluida com número: xxxxx'...\n"
        )
        # Clica no ok da mensagem
        button_ok = (1064, 604)  # find_target_position(screenshot_path, "Ok", 15)
        pyautogui.click(button_ok)

        # Window 'Deseja pesquisar pré-venda?'
        await worker_sleep(3)
        screenshot_path = take_screenshot()
        message_prevenda = take_target_position(screenshot_path, "Deseja")
        if message_prevenda is not None:
            button_yes = (
                921,
                562,
            )  # find_target_position(screenshot_path, "Yes", attempts=15)
            pyautogui.click(button_yes)
        else:
            log_msg = f"Mensagem 'Deseja pesquisar pré-venda?' não encontrada."
            console.print(log_msg, style="bold yellow")

        await worker_sleep(5)

        # screenshot_path = take_screenshot()
        # button_confirma_transferencia = take_target_position(screenshot_path, "confirma")
        # if button_confirma_transferencia is not None:
        #     pyautogui.click(button_confirma_transferencia)
        #     console.log("Confirmou Pré-venda da transferencia", style="bold green")
        # else:
        #     log_msg = f"Botao 'Confirma' não encontrado"
        #     console.print(log_msg, style="bold yellow")

        # Clica em "Yes" para confirmar a pré-venda
        confirma_pre_venda = (921, 562)
        pyautogui.click(confirma_pre_venda)
        console.log('Clicou em "Yes" para confirmar pré-venda', style="bold green")

        # pyautogui.confirm("vai clicar em confirmar")
        # Confirma pré-venda

        console.log("Clicando em 'Confirma' na pré-venda...", style="bold green")
        button_confirma = (1313, 333)
        pyautogui.hotkey("tab")
        pyautogui.doubleClick(button_confirma)
        # pyautogui.confirm("confirma pre venda")
        await worker_sleep(5)

        # Clica em YES na mensagem se sucesso de confirmação da pré-venda
        pre_venda_sucesso = (918, 550)
        # pyautogui.confirm("click yes")
        pyautogui.click(pre_venda_sucesso)
        console.log('Clicou em "Yes" na mensagem de sucesso', style="bold green")

        await worker_sleep(2)

        # Clica em OK na mensagem de sucesso de confirmação da pré-venda
        pre_venda_sucesso = (961, 550)
        # pyautogui.confirm("click ok")
        pyautogui.click(pre_venda_sucesso)
        console.log('Clicou em "OK" na mensagem de sucesso', style="bold green")

        await worker_sleep(5)

        # Faturando Pre-venda
        retorno = await faturar_pre_venda(task)
        if retorno.get("sucesso") == True:
            console.log(f"Faturou com sucesso!", style="bold green")
            valor_nota = retorno.get("valor_nota")
        else:
            await api_simplifica(
                task.configEntrada.get("urlRetorno"),
                "ERRO",
                retorno["retorno"],
                task.configEntrada.get("uuidSimplifica"),
                None,
                None,
            )
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=retorno.get("retorno"),
                status=RpaHistoricoStatusEnum.Falha,
            )

        # Extraindo nota fiscal
        await worker_sleep(5)
        console.log("Extraindo numero da nota fiscal", style="bold green")
        nota_fiscal = await extract_nf_number()
        console.print(f"\nNumero NF: '{nota_fiscal}'", style="bold green")

        await worker_sleep(7)

        # Transmitir a nota
        console.print("Transmitindo a nota...\n", style="bold green")
        pyautogui.click(875, 596)
        logger.info("\nNota Transmitida")
        console.print("\nNota Transmitida", style="bold green")

        await worker_sleep(5)

        # aguardando nota ser transmitida
        aguardando_nota = await wait_window_close("Aguarde")

        if aguardando_nota == False:
            # Clica em ok "processo finalizado"
            await worker_sleep(3)
            pyautogui.click(957, 556)
            # Clica em fechar
            await worker_sleep(3)
            pyautogui.click(1200, 667)
            log_msg = "Nota lançada com sucesso!"
            await api_simplifica(
                task.configEntrada.get("urlRetorno"),
                "SUCESSO",
                log_msg,
                task.configEntrada.get("uuidSimplifica"),
                nota_fiscal,
                valor_nota,
            )
            return RpaRetornoProcessoDTO(
                sucesso=True,
                retorno=log_msg,
                status=RpaHistoricoStatusEnum.Sucesso,
            )

        else:
            log_msg = "Tempo de espera para lançar a nota execedido."
            console.print(log_msg)
            logger.error(log_msg)
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=log_msg,
                status=RpaHistoricoStatusEnum.Falha,
            )

    except Exception as ex:
        log_msg = f"Erro Processo Transferências: {ex}"
        logger.error(log_msg)
        console.print(log_msg, style="bold red")
        await api_simplifica(
            task.configEntrada.get("urlRetorno"),
            "ERRO",
            log_msg,
            task.configEntrada.get("uuidSimplifica"),
            nota_fiscal,
            valor_nota,
        )
        return RpaRetornoProcessoDTO(
            sucesso=False,
            retorno=log_msg,
            status=RpaHistoricoStatusEnum.Falha,
        )
