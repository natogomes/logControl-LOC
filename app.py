from interface_grafica import *
from modulos.class_cliente import *
from modulos.class_produto import *
from modulos.class_pedido import *

# Abre a janela principal do programa
window_ini()
while True:
    window, event, values = sg.read_all_windows()
    entrada = values['entrada'].strip().title()
    cliente = Cliente(entrada)
    produto = Produto(entrada)
    pedido = Pedido(entrada)
    if event == sg.WIN_CLOSED:
        break
    # Faz um print de todos os cliente cadastrados(menu)
    elif event == 'Clientes':
        window['saida'].update('')
        cliente.get_clientes()

    # Faz um print dos dados do cliente solicitado(botão de atalho)
    elif event == 'CONSULTAR CLIENTE':
        window['saida'].update('')
        cliente.get_cliente()

    # Faz um print dos dados do cliente solicitado(menu)
    elif event == 'Cliente':
        window['saida'].update('')
        cliente.get_cliente()

    # Abre uma janela para fazer cadastro de cliente(botão de atalho)
    elif event == 'CADASTRAR CLIENTE':
        window['saida'].update('')
        window_cad_cliente(entrada)
        while True:
            window, event, values = sg.read_all_windows()
            if event == sg.WIN_CLOSED:
                window.close()
                break

            elif event == 'Fechar':
                window.close()
                break

            elif event == 'Concluir':
                nome = values['nome'].title().strip()
                endr = values['end'].title().strip()
                numr = values['num'].strip()
                comp = values['comp'].title().strip()
                bairro = values['bairro'].title().strip()
                cidade = values['cidade'].title().strip()
                fone = values['cel'].title().strip()

                if post_cliente(nome, endr, numr, bairro, cidade, fone, comp):
                    window.close()
                    break

    # Abre uma janela para fazer cadastro de cliente(menu)
    elif event == 'Inserir cliente':
        window['saida'].update('')
        window_cad_cliente(entrada)
        while True:
            window, event, values = sg.read_all_windows()
            if event == sg.WIN_CLOSED:
                window.close()
                break

            elif event == 'Fechar':
                window.close()
                break

            elif event == 'Concluir':
                nome = values['nome'].title().strip()
                endr = values['end'].title().strip()
                numr = values['num'].strip()
                comp = values['comp'].title().strip()
                bairro = values['bairro'].title().strip()
                cidade = values['cidade'].title().strip()
                fone = values['cel'].title().strip()

                if post_cliente(nome, endr, numr, bairro, cidade, fone, comp):
                    window.close()
                    break

    # Abre uma janela para fazer alteração de cadastro de cliente(menu)
    elif event == 'Alterar cliente':
        window['saida'].update('')
        validacao = cliente.validar_alt_clt()
        if validacao:
            window_alt_cliente(validacao)
            while True:
                window, event, values = sg.read_all_windows()

                id_cliente = values['id-cliente'].strip()
                novo_nome = values['alt-nome'].title().strip()
                end = values['alt-end'].title().strip()
                num = values['alt-num'].strip()
                comp = values['alt-comp'].title().strip()
                bairro = values['alt-bairro'].title().strip()
                cidade = values['alt-cidade'].title().strip()
                fone = values['alt-cel'].title().strip()


                if event == sg.WIN_CLOSED:
                    window.close()
                    break

                elif event == 'Fechar':
                    window.close()
                    break

                elif event == 'Buscar':
                    busca = cliente.buscar_dados(id_cliente, novo_nome)
                    if busca:
                        window['alt-end'].update(busca[0])
                        window['alt-num'].update(busca[1])
                        window['alt-comp'].update(busca[2])
                        window['alt-cel'].update(busca[3])
                        window['alt-bairro'].update(busca[4])
                        window['alt-cidade'].update(busca[5])

                elif event == 'Salvar':
                    if cliente.put_cliente(id_cliente, validacao, novo_nome, end, num, bairro, cidade, fone, comp):
                        window.close()
                        break

                elif event == 'Excluir':
                    valid_del = cliente.validar_del_clt(id_cliente, novo_nome, end, num, bairro, cidade, fone)
                    if valid_del:
                        window.close()
                        window_delete_clt(valid_del[0], valid_del[1], valid_del[2], valid_del[3], valid_del[4],
                                          valid_del[5], valid_del[6])

                        while True:
                            window, event, values = sg.read_all_windows()
                            if event == sg.WIN_CLOSED:
                                window.close()
                                break

                            elif event == 'Voltar':
                                window_alt_cliente(validacao)
                                window.close()
                                break

                            elif event == 'Excluir':
                                cliente.delete_cliente(id_cliente, novo_nome)
                                window_alt_cliente('')
                                window.close()
                                break

    # Faz um print de todos os produtos cadastrados(menu)
    elif event == 'Produtos':
        window['saida'].update('')
        produto.get_produtos()

    # Faz um print dos dados do produto solicitado(botão de atalho)
    elif event == 'CONSULTAR PRODUTO':
        window['saida'].update('')
        produto.get_produto()

    # Faz um print dos dados do produto solicitado(menu)
    elif event == 'Produto':
        window['saida'].update('')
        produto.get_produto()

    # Abre uma janela para fazer cadastro de produto(botão de atalho)
    elif event == 'CADASTRAR PRODUTO':
        window['saida'].update('')
        window_cad_produto(entrada)
        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                window.close()
                break

            elif event == 'Fechar':
                window.close()
                break

            elif event == 'Concluir':
                cad_produto = values['produto'].title().strip()
                cad_quantidade = values['qtd'].strip()
                cad_valor = values['valor'].strip()

                if produto.post_produto(cad_produto, cad_quantidade, cad_valor):
                    window.close()
                    break

    # Abre uma janela para fazer cadastro de produto(menu)
    elif event == 'Inserir produto':
        window['saida'].update('')
        window_cad_produto(entrada)
        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                window.close()
                break

            elif event == 'Fechar':
                window.close()
                break

            elif event == 'Concluir':
                cad_produto = values['produto'].title().strip()
                cad_quantidade = values['qtd'].strip()
                cad_valor = values['valor'].strip()

                if produto.post_produto(cad_produto, cad_quantidade, cad_valor):
                    window.close()
                    break

    # Abre uma janela para fazer alteração de cadastro de produto(menu)
    elif event == 'Alterar produto':
        window['saida'].update('')

        validacao = produto.validar_alt_prod()
        if validacao:
            window_alt_produto(validacao[0], validacao[1], validacao[2])
            while True:
                window, event, values = sg.read_all_windows()
                novo_prod = values['alt-produto'].title().strip()
                qtd = values['alt-quantidade'].strip()
                valor = values['alt-valor'].strip()

                if event == sg.WIN_CLOSED:
                    window.close()
                    break

                elif event == 'Fechar':
                    window.close()
                    break

                elif event == 'Salvar':
                    if produto.put_produto(entrada, novo_prod, qtd, valor):
                        window.close()
                        break

                elif event == 'Excluir':
                    if produto.validar_del_prod():
                        window.close()
                        window_delete_prod(novo_prod)
                        while True:
                            window, event, values = sg.read_all_windows()

                            if event == sg.WIN_CLOSED:
                                window.close()
                                window_alt_produto(validacao[0], validacao[1], validacao[2])
                                break

                            elif event == 'Voltar':
                                window.close()
                                window_alt_produto(validacao[0], validacao[1], validacao[2])
                                break

                            elif event == 'Excluir':
                                produto.delete_produto(novo_prod)
                                window.close()
                                window_alt_produto('', '', '')
                                break

    # Faz um print de todos os pedidos cadastrados(menu)
    elif event == 'Pedidos':
        window['saida'].update('')
        pedido.get_pedidos()

    # Faz um print dos dados do pedido(produto) solicitado(menu)
    elif event == 'Pedido':
        window['saida'].update('')
        pedido.get_pedido(entrada)

    # Abre uma janela para fazer cadastro de pedido(botão de atalho)
    elif event == 'CADASTRAR PEDIDO':
        window['saida'].update('')
        window_cad_pedido(entrada)
        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                window.close()
                break

            elif event == 'Fechar':
                window.close()
                break

            elif event == 'Concluir':
                from datetime import datetime
                data_hora = datetime.today()
                id_c = values['id-clt-ped'].strip()
                cliente = values['cliente'].title().strip()
                pedido = values['pedido'].title().strip()
                qtd = values['unidades'].strip()
                descricao = values['descricao'].strip().title()
                data = datetime.strftime(data_hora, "%d/%m/%y - %H:%Mh")

                if post_pedido(id_c, cliente, pedido, qtd, data, descricao):
                    window.close()
                    break

    # Abre uma janela para fazer cadastro de pedido(menu)
    elif event == 'Inserir pedido':
        window['saida'].update('')
        window_cad_pedido(entrada)
        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                window.close()
                break

            elif event == 'Fechar':
                window.close()
                break

            elif event == 'Concluir':
                from datetime import datetime
                data_hora = datetime.today()
                id_c = values['id-clt-ped'].strip()
                cliente = values['cliente'].title().strip()
                pedido = values['pedido'].title().strip()
                qtd = values['unidades'].strip()
                descricao = values['descricao'].strip().title()
                data = datetime.strftime(data_hora, "%d/%m/%y - %H:%Mh")

                if post_pedido(id_c, cliente, pedido, qtd, data, descricao):
                    window.close()
                    break

    # Abre uma janela para fazer alteração de cadastro de pedido(menu)
    elif event == 'Alterar pedido':
        window['saida'].update('')
        validacao = pedido.validar_alt_ped()
        if validacao:
            window_alt_pedido(validacao)
            while True:
                window, event, values = sg.read_all_windows()
                nome_alt = values['alt-cliente'].strip().title()
                ped = values['alt-pedido'].title().strip()
                qtd_prod = values['alt-unidades'].strip()
                valor = values['alt-valor'].strip()
                descricao_ped = values['alt-descricao'].strip()
                id_clt = values['id-clt'].strip()
                id_ped = values['id-ped'].strip()

                if event == sg.WIN_CLOSED:
                    window.close()
                    break

                elif event == 'Fechar':
                    window.close()
                    break

                elif event == 'Buscar':
                    buscar = pedido.buscar_pedido(id_clt, id_ped, nome_alt)
                    if buscar:
                        window['alt-pedido'].update(buscar[0])
                        window['alt-unidades'].update(buscar[1])
                        window['alt-valor'].update(buscar[2])
                        window['alt-descricao'].update(buscar[3])

                elif event == 'Salvar':
                    if pedido.put_pedido(id_clt, nome_alt, id_ped, ped, qtd_prod, valor, descricao_ped):
                        window.close()
                        break

                elif event == 'Excluir':
                    valid_del = pedido.validar_del_ped(nome_alt, ped, qtd_prod, valor, id_clt, id_ped)
                    if valid_del:
                        window.close()
                        window_delete_ped(valid_del[0], valid_del[1], valid_del[2], valid_del[3], valid_del[4])
                        while True:
                            window, event, values = sg.read_all_windows()

                            if event == sg.WIN_CLOSED:
                                window.close()
                                break

                            elif event == 'Voltar':
                                window.close()
                                window_alt_pedido(validacao)
                                break

                            elif event == 'Cancelar':
                                pedido.cancela_pedido(id_clt, id_ped, nome_alt)
                                window.close()
                                window_alt_pedido('')
                                break

                            elif event == 'Excluir':
                                pedido.delete_pedido(id_clt, id_ped, nome_alt)
                                window.close()
                                window_alt_pedido('')
                                break


