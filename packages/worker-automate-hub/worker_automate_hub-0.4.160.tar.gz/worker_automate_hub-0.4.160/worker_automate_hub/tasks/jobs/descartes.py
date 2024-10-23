
import warnings
from datetime import datetime

import pyautogui
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


async def descartes(task: RpaProcessoEntradaDTO) -> RpaRetornoProcessoDTO:
    try:
        # Inicializa variaveis
        nota_fiscal = [None]
        log_msg = None
        valor_nota = None
        # Get config from BOF
        console.print("Obtendo configuração...\n")
        config = await get_config_by_name(name="Descartes_Emsys")
        # Popula Variaveis
        itens = task.configEntrada.get("itens", [])
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
            console.print("Pesquisando por: Cadastro Pré Venda")
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

        # Preenche data de validade
        console.print("Preenchendo a data de validade...\n")
        screenshot_path = take_screenshot()
        target_pos = (
            961,
            331,
        )  # find_target_position(screenshot_path, "Validade", 10, 0, 15)
        if target_pos == None:
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno="Não foi possivel encontrar o campo de validade",
                status=RpaHistoricoStatusEnum.Falha,
            )

        pyautogui.click(target_pos)
        pyautogui.write(f'{datetime.now().strftime("%d/%m/%Y")}', interval=0.1)
        pyautogui.press("tab")
        console.print(
            f"\nValidade Digitada: '{datetime.now().strftime("%d/%m/%Y")}'\n",
            style="bold green",
        )
        await worker_sleep(1)

        # Condição da Pré-Venda
        console.print("Selecionando a Condição da Pré-Venda\n")
        condicao_field = find_target_position(screenshot_path, "Condição", 10, 0, 15)
        if condicao_field == None:
            condicao_field = (1054, 330)

        pyautogui.click(condicao_field)
        await worker_sleep(1)
        pyautogui.write("A")
        await worker_sleep(1)
        pyautogui.press("down")
        pyautogui.press("enter")
        await worker_sleep(1)

        # Preenche o campo do cliente com o número da filial
        console.print("Preenchendo o campo do cliente com o número da filial...\n")
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

        # Verifica se precisa selecionar endereço
        console.print("Verificando se precisa selecionar endereço...\n")
        screenshot_path = take_screenshot()
        window_seleciona_endereco_position = take_target_position(
            screenshot_path, "Endereço"
        )
        if window_seleciona_endereco_position is not None:
            log_msg = f"Aviso para selecionar Endereço"
            await api_simplifica(
                task.configEntrada.get("urlRetorno"),
                "ERRO",
                log_msg,
                task.configEntrada.get("uuidSimplifica"),
                nota_fiscal,
                valor_nota,
            )
            return RpaRetornoProcessoDTO(
                sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
            )
        else:
            log_msg = "Sem Aviso de Seleção de Endereço"
            console.print(log_msg, style="bold green")
            logger.info(log_msg)

        # Clica em cancelar na Janela "Busca Representante"
        console.print("Cancelando a Busca Representante\n")
        screenshot_path = take_screenshot()
        window_busca_representante_position = take_target_position(
            screenshot_path, "Representante"
        )
        if window_busca_representante_position is not None:
            button_cancelar_position = find_target_position(
                screenshot_path, "Cancelar", attempts=15
            )
            pyautogui.click(button_cancelar_position)

        await worker_sleep(5)

        # Aviso "Deseja alterar a condição de pagamento informada no cadastro do cliente?"
        console.print(
            "Verificando alerta de alteração de pagamento informada no cadastro do cliente...\n"
        )
        # screenshot_path = take_screenshot()
        # payment_condition_warning_position = take_target_position(screenshot_path, "pagamento")
        # if payment_condition_warning_position is not None:
        button_no_position = (
            1000,
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

        await worker_sleep(10)

        # Seleciona 'Custo Médio' (Seleção do tipo de preço)
        console.print("Seleciona 'Custo Médio' (Seleção do tipo de preço)...\n")
        custo_medio_select_position = (851, 523)
        pyautogui.click(custo_medio_select_position)
        await worker_sleep(1)
        button_ok_position = (
            1042,
            583,
        )  # find_target_position(screenshot_path, "OK", attempts=15)
        pyautogui.click(button_ok_position)
        await worker_sleep(1)
        console.print(f"\nClicou OK 'Custo médio'", style="bold green")

        await worker_sleep(5)

        # Clica em ok na mensagem "Existem Pré-Vendas em aberto para este cliente."
        console.print(
            "Clica em ok na mensagem 'Existem Pré-Vendas em aberto para este cliente.'\n"
        )
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
        console.print("Definindo representante para '1'\n")
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

        # Seleciona modelo de capa
        console.print("Selecionando o modelo de capa...")
        screenshot_path = take_screenshot()
        model_descarte_position = find_target_position(
            screenshot_path, "Modelo", 0, 100, attempts=8
        )

        if model_descarte_position == None:
            model_descarte_position = await find_element_center(
                ASSETS_BASE_PATH + "field_modelo_faturamento.png",
                (681, 489, 546, 96),
                15,
            )
            if model_descarte_position is not None:
                lista = list(model_descarte_position)
                lista[0] += 100
                model_descarte_position = tuple(lista)

        if model_descarte_position == None:
            model_descarte_position = (848, 527)

        if model_descarte_position is not None:
            pyautogui.click(model_descarte_position)
            pyautogui.click(1500, 800)
            pyautogui.write("B")
            pyautogui.hotkey("tab")
        else:
            log_msg = f"Campo Modelo na capa da nota não encontrado"
            await api_simplifica(
                task.configEntrada.get("urlRetorno"),
                "ERRO",
                log_msg,
                task.configEntrada.get("uuidSimplifica"),
                nota_fiscal,
                valor_nota,
            )
            return RpaRetornoProcessoDTO(
                sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
            )

        # Abre Menu itens
        console.print("Abrindo Menu Itens...\n")
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
                sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
            )

        await worker_sleep(2)

        # Loop de itens
        console.print("Inicio do loop de itens\n")
        for item in itens:
            screenshot_path = take_screenshot()
            # Clica no botão inclui para abrir a tela de item
            console.print("Clicando em Incluir...\n")
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
                    sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
                )
            await worker_sleep(3)

            # Digita Almoxarifado
            console.print("Preenchendo o campo de almoxarifado...\n")
            screenshot_path = take_screenshot()
            field_almoxarifado = (
                839,
                313,
            )  # find_target_position(screenshot_path, "Almoxarifado",0, 129, 15)
            if field_almoxarifado is not None:
                pyautogui.doubleClick(field_almoxarifado)
                pyautogui.hotkey("del")
                pyautogui.write(
                    task["configEntrada"]["filialEmpresaOrigem"] + ALMOXARIFADO_DEFAULT
                )
                pyautogui.hotkey("tab")
                await worker_sleep(2)
                console.print(
                    f"\nDigitou almoxarifado {task['configEntrada']['filialEmpresaOrigem'] + ALMOXARIFADO_DEFAULT}",
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
                    sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
                )

            # Segue para o campo do item
            console.print("Preenchendo o campo do item...\n")
            field_item = (
                841,
                339,
            )  # find_target_position(screenshot_path, "Item", 0, 130, 15)
            pyautogui.doubleClick(field_item)
            pyautogui.hotkey("del")
            pyautogui.write(item["codigoProduto"])
            pyautogui.hotkey("tab")
            await worker_sleep(2)
            console.print(f"\nDigitou item {item['codigoProduto']}", style="bold green")

            # Checa tela de pesquisa de item
            console.print("Verificando a existencia da tela de pesquisa de item...\n")
            screenshot_path = take_screenshot()
            window_pesquisa_item = await find_element_center(
                ASSETS_BASE_PATH + "window_pesquisa_item.png", (488, 226, 352, 175), 10
            )
            console.print(
                f"Produto {item['codigoProduto']} encontrado", style="bold green"
            )
            logger.info(f"Produto {item['codigoProduto']} encontrado")

            if window_pesquisa_item is not None:
                observacao = (
                    f"Item {item['codigoProduto']} não encontrado, verificar cadastro"
                )
                console.print(f"{observacao}", style="bold green")
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

            # Checa se existe alerta de item sem preço, se existir retorna erro(simplifica e bof)
            console.print(
                "Verificando se existe alerta de item sem preço, se existir retorna erro(simplifica e bof)...\n"
            )
            warning_price = await find_element_center(
                ASSETS_BASE_PATH + "warning_item_price.png", (824, 426, 255, 191), 10
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

            await worker_sleep(2)

            # Seleciona o Saldo Disponivel e verifica se ah possibilidade do descarte
            console.print(
                "Selecionando o Saldo Disponivel e verificando se há possibilidade do descarte...\n"
            )
            # screenshot_path = take_screenshot()
            app = Application().connect(title="Inclui Item Pré Venda")
            item_pre_venda = app["Inclui Item Pré Venda"]
            saldo_disponivel = item_pre_venda.child_window(
                class_name="TDBIEditNumber", found_index=9
            ).window_text()
            saldo_disponivel = saldo_disponivel.replace(".", "")
            saldo_disponivel = saldo_disponivel.replace(",", ".")
            amount_avaliable = int(float(saldo_disponivel))
            # field_saldo_disponivel = (916, 606) #find_target_position(screenshot_path + "Saldo", 20, 0, 10)
            # if field_saldo_disponivel is not None:
            #     pyautogui.doubleClick(field_saldo_disponivel)
            #     await worker_sleep(1)
            #     pyautogui.doubleClick(field_saldo_disponivel)
            #     await worker_sleep(1)
            #     pyautogui.doubleClick(field_saldo_disponivel)
            #     await worker_sleep(1)
            #     pyautogui.hotkey('ctrl', 'c')
            #     amount_avaliable= ''
            #     amount_avaliable = pyperclip.paste()
            console.print(f"Saldo Disponivel: '{amount_avaliable}'", style="bold green")

            # Verifica se o saldo disponivel é valido para descartar
            if int(amount_avaliable) > 0 and int(amount_avaliable) >= int(item["qtd"]):
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
                log_msg = f"Saldo disponivel: '{amount_avaliable}' é menor que '{item['qtd']}' o valor que deveria ser descartado. Item: '{item['codigoProduto']}'"
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
                    sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
                )

            # Clica em incluir para adicionar o item na nota
            console.print("Clicando em incluir para adicionar o item na nota...\n")
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

            try:
                # Verificar tela de Valor de custo maior que preço de venda do item
                console.print("Verificando tela de Valor de custo...\n")
                custo_window = Application().connect(title="Warning")
                custo_window = custo_window["Warning"]

                text_custo = custo_window.window_text()
                if "Warning" in text_custo:
                    log_msg = f"O valor de custo do Item: {item['codigoProduto']} é maior que o valor de venda."
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
            except:
                console.log(
                    "Nenhuma tela de warning foi encontrada", style="bold green"
                )

            # Clica em cancelar para fechar a tela e abrir novamente caso houver mais itens
            console.print(
                "Clicando em cancelar para fechar a tela e abrir novamente caso houver mais itens...\n"
            )
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
                    sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
                )

        await worker_sleep(2)

        # Clica no botão "+" no canto superior esquerdo para lançar a pre-venda
        console.print(
            "Clica no botão '+' no canto superior esquerdo para lançar a pre-venda"
        )
        # Precisa manter por imagem pois não tem texto
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
                sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
            )

        await worker_sleep(5)

        screenshot_path = take_screenshot()

        # Verifica mensagem de "Pré-Venda incluida com número: xxxxx"
        console.print(
            "Verificando mensagem de 'Pré-Venda incluida com número: xxxxx'...\n"
        )
        # Clica no ok da mensagem
        button_ok = (1064, 604)  # find_target_position(screenshot_path, "Ok", 15)
        pyautogui.click(button_ok)

        screenshot_path = take_screenshot()

        # Message 'Deseja pesquisar pré-venda?'
        console.print(
            "Verificando a existencia da mensagem: 'Deseja pesquisar pré-venda?'...\n"
        )
        message_prevenda = take_target_position(screenshot_path, "Deseja")
        if message_prevenda is not None:
            button_yes = find_target_position(screenshot_path, "Yes", attempts=15)
            pyautogui.click(button_yes)
        else:
            log_msg = f"Mensagem 'Deseja pesquisar pré-venda?' não encontrada."
            console.print(log_msg, style="bold yellow")

        screenshot_path = take_screenshot()
        # Confirma pré-venda
        # Pode não precisar em descartes, mas em trânsferencias é obrigatório
        console.print("Confirmando a Pre-Venda...\n")
        button_confirma_transferencia = take_target_position(
            screenshot_path, "confirma"
        )
        if button_confirma_transferencia is not None:
            pyautogui.click(button_confirma_transferencia)
            console.log("Confirmou transferencia", style="bold green")
        else:
            log_msg = f"Botao 'Confirma' não encontrado"
            console.print(log_msg, style="bold yellow")

        pyautogui.moveTo(1200, 300)

        console.print("Verificando a mensagem: Confirmar transferencia...\n")
        screenshot_path = take_screenshot()
        message_confirma_transferencia = take_target_position(
            screenshot_path, "confirmar"
        )
        if message_confirma_transferencia is not None:
            # clica em sim na mensagem
            button_yes = find_target_position(screenshot_path, "Yes", attempts=8)
            pyautogui.click(button_yes)
            console.log(
                "Cliclou em 'Sim' para cofirmar a pré-venda", style="bold green"
            )
            pyautogui.moveTo(1200, 300)
            await worker_sleep(5)
            screenshot_path = take_screenshot()
            vencimento_message_primeira_parcela = take_target_position(
                screenshot_path, "vencimento"
            )
            # Pode nao aparecer na prod
            if vencimento_message_primeira_parcela is not None:
                button_yes = find_target_position(screenshot_path, "Yes", attempts=15)
                pyautogui.click(button_yes)
            await worker_sleep(5)
            screenshot_path = take_screenshot()
            # Clica no OK 'Pre-Venda incluida com sucesso'
            button_ok = find_target_position(screenshot_path, "Ok", attempts=15)
            pyautogui.click(button_ok)
            console.log(
                "Cliclou em 'OK' para pré-venda confirmada com sucesso",
                style="bold green",
            )
        else:
            log_msg = (
                f"Mensagem 'Deseja realmente confirmar esta pré-venda?' não encontrada."
            )
            console.print(log_msg, style="bold yellow")

        pyautogui.moveTo(1000, 500)

        retorno = await faturar_pre_venda(task)
        if retorno.get("sucesso") == True:
            console.log(f"Faturou com sucesso!", style="bold green")
            valor_nota = retorno.get("valor_nota")
        else:
            await api_simplifica(
                task.configEntrada.get("urlRetorno"),
                "ERRO",
                retorno.get("retorno"),
                task.configEntrada.get("uuidSimplifica"),
                None,
                None,
            )
            return RpaRetornoProcessoDTO(
                sucesso=False,
                retorno=retorno.get("retorno"),
                status=RpaHistoricoStatusEnum.Falha,
            )

        await worker_sleep(10)

        # Mensagem de nota fiscal gerada com número
        log_msg = "Extraindo numero da nota fiscal"
        console.log(log_msg, style="bold green")
        logger.info(log_msg)
        nota_fiscal = await extract_nf_number()
        console.print(f"\nNumero NF: '{nota_fiscal}'", style="bold green")

        await worker_sleep(15)

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
                sucesso=True, retorno=log_msg, status=RpaHistoricoStatusEnum.Sucesso
            )

        else:
            log_msg = "Tempo de espera para lançar a nota execedido."
            console.print(log_msg)
            logger.error(log_msg)
            return RpaRetornoProcessoDTO(
                sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
            )

    except Exception as ex:
        log_msg = f"Erro Processo Descartes: {ex}"
        logger.error(log_msg)
        console.print(log_msg, style="bold red")
        await api_simplifica(
            task.configEntrada.get("urlRetorno"),
            "ERRO",
            log_msg,
            task.configEntrada.get("uuidSimplifica"),
            nota_fiscal[0],
            valor_nota,
        )
        return RpaRetornoProcessoDTO(
            sucesso=False, retorno=log_msg, status=RpaHistoricoStatusEnum.Falha
        )
