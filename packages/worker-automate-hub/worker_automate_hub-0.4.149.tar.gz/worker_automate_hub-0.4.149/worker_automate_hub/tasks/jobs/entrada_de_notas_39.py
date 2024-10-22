import asyncio
import warnings

import pyperclip
import pyautogui
from pywinauto.application import Application
from rich.console import Console

from worker_automate_hub.api.client import get_config_by_name
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import (
    find_target_position,
    import_nfe,
    kill_process,
    login_emsys,
    select_model_capa,
    take_screenshot,
    type_text_into_field,
    verify_nf_incuded,
    rateio_window,
    set_variable,
    importar_notas_outras_empresas,
    digitar_datas_emissao,
    digitar_numero_nota,
    worker_sleep,
)

pyautogui.PAUSE = 0.5
console = Console()



async def entrada_de_notas_39(task):
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
        model  = select_model_capa()
        if model['sucesso'] == True:
            console.log(model['retorno'], style='bold green')
        else:
            return {"sucesso": False, "retorno": f"{model['retorno']}"}

        #Clica em 'Importar-Nfe'
        imported_nfe  = await import_nfe()
        if imported_nfe['sucesso'] == True:
            console.log(imported_nfe['retorno'], style='bold green')
        else:
            return {"sucesso": False, "retorno": f"{import_nfe['retorno']}"}

        # Clica em Notas de Outras Empresas
        pyautogui.click(824, 547)
        await worker_sleep(2)

        #Clica em  'OK' para selecionar
        pyautogui.click(975, 674)
        await worker_sleep(2)

        empresa = str(int(nota['cnpjFornecedor'][8:12]))
        await importar_notas_outras_empresas(nota["dataEmissao"], nota["numeroNota"], empresa)

        # #Digita datas de emissão
        # data_emissao = nota['dataEmissao'].replace('/', '')
        # digitar_datas_emissao(data_emissao)

        #Digita numero da nota
        # numero_nota = nota['numeroNota']
        # digitar_numero_nota(numero_nota)
        #await worker_sleep(100)
  
        # #clica na nota
        # pyautogui.click(791,483)
        # await worker_sleep(2)

        # #Clica em 'Importar'
        # screenshot_path = take_screenshot()
        # field = find_target_position(screenshot_path, "cancelar",0 ,100 , 15)
        # if field == None:
        #     return {"sucesso": False, "retorno": f"Não foi possivel encontrar o botão importar"}
        # pyautogui.click(field)
        
        await worker_sleep(10)

        # Identifica se ja foi importada
        screenshot_path = take_screenshot()
        field = find_target_position(screenshot_path, "Mensagem", 0, 0, 10)
        if field == None:
            ...
        else:
            console.log("Nota já lançada ou não encontrada.", style='bold green')
            return {"sucesso": False, "retorno": f"Nota já lançada ou não encontrada."}

        #Tela "Infromações para importação da Nota Fiscal Eletrônica"
        screenshot_path = take_screenshot()

        if nota['existeDespesa'] == 'Sim':
            #Digita natureza da operação
            pyautogui.hotkey('tab')
            pyautogui.write("1152")
            pyautogui.hotkey('tab')

            #Digita tipo despesa
            pyautogui.click(800, 479)
            pyautogui.click(field)
            pyautogui.write("291")
            pyautogui.hotkey("tab")

            #Marca "Manter Natureza de operação selecionada"
            pyautogui.click(963, 578)
            #Marca "Manter Calculo PIS/COFINS"
            pyautogui.click(705, 667)

        #Clica em OK

        pyautogui.click(704, 665)
        await worker_sleep(5)
        pyautogui.click(1100, 730)
        await worker_sleep(20)

        try:
            # Tratativa de "itens com ncm divergente" - PASSO 27.1 DA IT
            screenshot_path = take_screenshot()
            console.log("Procurando itens com ncm divergente", style='bold yellow')
            itens = find_target_position(screenshot_path, 'NCM', 0, 0, 15)

            if itens is not None:
                pyautogui.click(1000, 568)
                console.log("Clicou em não nos itens com ncm divergente", style='bold yellow')
            else:
                console.log("0 Itens com ncm divergente", style='bold green')

            await worker_sleep(10)

            # Itens não localizados - Clica em Sim
            screenshot_path = take_screenshot()
            console.log("Verificando tela de Itens Não Localizados", style='bold yellow')
            itens_nloc = find_target_position(screenshot_path, 'associar', 0, 0, 15)

            if itens_nloc:
                pyautogui.click(920, 562)
                await worker_sleep(3)
                pyautogui.click(920, 304)
                pyautogui.hotkey("ctrl", "c")
                clipboard = pyperclip.paste()

                if clipboard:
                    console.log("Itens não localizados na nota.", style='bold red')

            # Tratativa "Selecionar itens fornecedor" - PASSO 27.3 da it
            multi_ref = True
            while multi_ref:
                screenshot_path = take_screenshot()
                field = find_target_position(screenshot_path, "fornecedor", 0, 0, 5)

                if field:
                    pyautogui.click(1075, 624)
                    await worker_sleep(20)
                else:
                    multi_ref = False

        except Exception as e:
            console.print(f"Erro durante a execução: {e}", style="red")
            await worker_sleep(3)

        #Seleciona pagamento
        console.log("Seleciona Pagamento", style='bold yellow')
        pyautogui.click(623, 374)
        await worker_sleep(1)
        pyautogui.click(889, 349)
        await worker_sleep(1)
        pyautogui.write("27")
        await worker_sleep(1)
        pyautogui.hotkey("enter")

        #Digita "Valor"

        pyautogui.click(1285, 352)
        await worker_sleep(1)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("del")
        await worker_sleep(1)
        pyautogui.write(nota['valorNota'])
        pyautogui.click(593, 302)
        await worker_sleep(10)

        # Nota com itens bloqueados?
        pyautogui.click(1007, 562)
        await worker_sleep(1)
        pyautogui.click(1358, 751)
        await worker_sleep(1)

        pyautogui.click(1111, 608)
        await worker_sleep(1)
        pyautogui.click(1234, 628)
        await worker_sleep(60)

        #Clica para lançar a nota
        pyautogui.click(971, 569)
        await worker_sleep(1)
        console.log("Clicou pra lançar nota", style='bold green')

        #Variação Maxima de custo
        pyautogui.click(1234, 633)
        console.log("Clicou 'OK' variacao maxima de custo", style='bold green')

        #Quantidade de tempo alta devido o emsys ser lento
        console.log("Aguardando delay...", style='bold green')
        await worker_sleep(30)

        console.log("Verificando se nota foi lançada", style='bold green')
        retorno = verify_nf_incuded()
        if retorno:
            pyautogui.click(959, 564)
            return {"sucesso": True, "retorno": f"Nota Lançada com sucesso!"}
        else:
            console.log("Verficando se necessita realizar o rateio")
        

        if nota['existeDespesa'] == 'Sim':
            console.log("Inicializando o rateio", style='bold green')
            await rateio_window(nota)
            asyncio.sleep(10)

        #Aviso CFOP
        console.log("Verificando aviso CFOP", style='bold green')
        screenshot_path = take_screenshot()
        field = None
        field = find_target_position(screenshot_path, "mesmo", 0, 0, 8)
        if field == None:
            console.print("Nota com CFOP correto")
        else:
            #Clica em OK
            pyautogui.click(1096, 603)
            #Clica em "Principal"
            field = find_target_position(screenshot_path, "Principal", 0, 0, 8)
            pyautogui.click(field)
            #Selecio no "Principal" a NOP correta
            field = find_target_position(screenshot_path, "Inscrição", 20, 0, 8)
            pyautogui.click(field)
            pyautogui.write("1152")
            #Clica para lançar a nota
            pyautogui.click(594, 299)

            #Clica novamente em ok na variação de custo      
            field = find_target_position(screenshot_path, "ultrapassam", 0, 0, 8)
            if field == None:
                console.print("Nota sem itens com variação de custo")
            else:
                pyautogui.click(1234, 633)

        #Clica para lançar a nota
        pyautogui.click(594, 299)
        await worker_sleep(5)

        #Verifica se a info 'Nota fiscal incluida' está na tela   
        retorno = verify_nf_incuded()
        if retorno:
            pyautogui.click(959, 564)
            return {"sucesso": True, "retorno": f"Nota Lançada com sucesso!"}
        else:
            return {"sucesso": False, "retorno": f"Erro ao lançar nota"}

    except Exception as ex:
        observacao = f"Erro Processo Entrada de Notas: {str(ex)}"
        logger.error(observacao)
        console.print(observacao, style="bold red")
        return {"sucesso": False, "retorno": observacao}
