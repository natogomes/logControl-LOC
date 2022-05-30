import PySimpleGUI as sg
logo = 'logoLoc.ico'


# CRIA JANELA INICAL
def window_ini():
    sg.theme('DarkGrey2')

    menu = [
        ['Arquivo', ['Clientes', 'Produtos', 'Pedidos']],
        ['Editar', ['Alterar cliente', 'Alterar produto', 'Alterar pedido']],
        ['Inserir', ['Inserir cliente', 'Inserir produto', 'Inserir pedido']],
        ['Consultar', ['Cliente', 'Produto', 'Pedido']]
    ]

    col_logo = [
        [sg.Image('logoCabeca.png')]
    ]

    col_pesquisa = [
        [sg.Text('Olá, Seja Bem vindo!', font='arial 20')],
        [sg.Text('Informe o nome (Cliente ou Produto)', font='arial 12', pad=(0, (10, 0)))],
        [sg.Input(font='arial 12', size=(40, 1), pad=(0, (0, 10)), background_color='white', key='entrada')],
        [sg.Button('CONSULTAR CLIENTE', pad=(0, 10), size=(41, 2), font='arial 13 bold underline')],
        [sg.Button('CONSULTAR PRODUTO', pad=(0, (0, 10)), size=(41, 2), font='arial 13 bold underline')],
        [sg.Button('CADASTRAR CLIENTE', button_color='#cccccc', pad=(0, (0, 10)), size=(41, 2),
                   font='arial 13 bold underline')],
        [sg.Button('CADASTRAR PRODUTO', button_color='#cccccc', pad=(0, (0, 10)), size=(41, 2),
                   font='arial 13 bold underline')],
        [sg.Button('CADASTRAR PEDIDO', button_color='#cccccc', pad=(0, (0, 10)), size=(41, 2),
                   font='arial 13 bold underline')],
    ]

    col_out = [
        [sg.Output(size=(50, 20), background_color='white', font='arial 12 bold', key='saida')]
    ]

    layout = [
        [sg.Menu(menu, background_color='white')],
        [sg.Column(col_logo, pad=(0, (0, 10)))],
        [sg.Column(col_pesquisa),
         sg.Text(' ' * 10),
         sg.Column(col_out, pad=(0, (0, 6)))],
        [sg.CButton('Sair', font='arial 12', size=(8, 1), pad=(0, (20, 0)))],
        [sg.Text('RenatoGomes©', font='arial 10 underline', pad=(0, (20, 0)))]
    ]
    winPrin = sg.Window('Log Control', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                        size=(1000, 600), finalize=True)


# CRIA A JANELA DE CADASTRO DE CLIENTE
def window_cad_cliente(nome):
    sg.theme('DarkGrey2')

    col_cont1 = [
        [sg.Text('NOME:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('ENDEREÇO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('Nº:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('COMPLEMENTO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('CEL:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('BAIRRO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('CIDADE:', font='arial 13', pad=(0, (0, 15)))]
    ]

    col_cont2 = [
        [sg.Input(nome, size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='nome')],
        [sg.Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='end')],
        [sg.Input(size=(8, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='num')],
        [sg.Input('**Opcional', size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='comp')],
        [sg.Input(size=(11, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='cel'),
         sg.Text('DDD + número (só números)', pad=(5, (0, 15)))],
        [sg.Input(size=(27, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='bairro')],
        [sg.Input(size=(27, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='cidade')]
    ]

    layout = [
        [sg.Text('CADASTRO DE CLIENTES', font='arial 20', pad=(0, (0, 25)))],
        [sg.Column(col_cont1), sg.Text(' ' * 5), sg.Column(col_cont2)],
        [sg.Button('Concluir', button_color='#cccccc', font='arial 12', size=(10, 1), pad=(10, (20, 0))),
         sg.Button('Fechar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))]
    ]
    winCad = sg.Window('Cadastro de Clientes', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                       size=(550, 400), finalize=True)


# CRIA A JANELA DE CADASTRO DE PRODUTOS
def window_cad_produto(nome):
    sg.theme('DarkGrey2')

    col_cont1 = [
        [sg.Text('PRODUTO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('QUANTIDADE:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('VALOR R$:', font='arial 13', pad=(0, (0, 15)))]

    ]

    col_cont2 = [
        [sg.Input(nome, size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='produto')],
        [sg.Input(size=(5, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='qtd')],
        [sg.Input(size=(10, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='valor'),
         sg.Text('(0000,00)', font='arial 13', pad=(5, (0, 15)))]
    ]

    layout = [
        [sg.Text('CADASTRO DE PRODUTOS', font='arial 20', pad=(0, (0, 25)))],
        [sg.Column(col_cont1), sg.Text(' ' * 5), sg.Column(col_cont2)],
        [sg.Button('Concluir', button_color='#cccccc', font='arial 12', size=(10, 1), pad=(10, (20, 0))),
         sg.Button('Fechar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))]
    ]
    winProd = sg.Window('Cadastro de Produtos', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                        size=(550, 250), finalize=True)


# CRIA A JANELA DE CADASTRO DE PEDIDOS
def window_cad_pedido(nome):
    sg.theme('DarkGrey2')

    col_cont1 = [
        [sg.Text('CLIENTE:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('Nº DO CLIENTE:', font='arial 13', pad=(0, (0, 35)))],
        [sg.Text('PRODUTO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('QUANTIDADE:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('DESCRIÇÃO:', font='arial 13', pad=(0, (20, 30)))],

    ]

    col_cont2 = [
        [sg.Input(nome, size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='cliente')],
        [sg.Input(size=(5, 1), background_color='white', font='arial 12', pad=(0, (0, 35)),
                  key='id-clt-ped')],
        [sg.Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='pedido')],
        [sg.Input(size=(5, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='unidades')],
        [sg.Multiline('**Opcional', size=(33, 3), background_color='white', font='arial 12', pad=(0, (0, 15)),
                      key='descricao')],
    ]

    layout = [
        [sg.Text('CADASTRO DE PEDIDOS', font='arial 20', pad=(0, (0, 25)))],
        [sg.Column(col_cont1), sg.Text(' ' * 5), sg.Column(col_cont2)],
        [sg.Button('Concluir', button_color='#cccccc', font='arial 12', size=(10, 1), pad=(10, (20, 0))),
         sg.Button('Fechar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))]
    ]
    winProd = sg.Window('Cadastro de Pedidos', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                        size=(550, 381), finalize=True)


# CRIA A JANELA DE ALTERAÇÃO DE CADASTRO DE CLIENTE
def window_alt_cliente(nome):

    sg.theme('DarkGrey2')

    col_cont1 = [
        [sg.Text('NOME:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('Nº DO CLIENTE:', font='arial 13', pad=(0, (0, 35)))],
        [sg.Text('ENDEREÇO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('Nº:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('COMPLEMENTO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('CEL:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('BAIRRO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('CIDADE:', font='arial 13', pad=(0, (0, 15)))]
    ]

    col_cont2 = [
        [sg.Input(nome, size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)),
                  key='alt-nome')],
        [sg.Input(size=(5, 1), background_color='white', font='arial 12', pad=(0, (0, 35)),
                  key='id-cliente'),
         sg.Text('Informe o nº e clique "Buscar"', font='arial 13', pad=(10, (0, 35)))],
        [sg.Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-end')],
        [sg.Input(size=(8, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-num')],
        [sg.Input('**Opcional', size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-comp')],
        [sg.Input(size=(14, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-cel')],
        [sg.Input(size=(27, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-bairro')],
        [sg.Input(size=(27, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-cidade')]
    ]

    layout = [
        [sg.Text('CADASTRO DE CLIENTE', font='arial 20', pad=(0, (0, 25)))],
        [sg.Column(col_cont1), sg.Text(' ' * 5), sg.Column(col_cont2)],
        [sg.Button('Salvar', button_color='#cccccc', font='arial 12', size=(8, 1), pad=(10, (20, 0))),
         sg.Button('Buscar', font='arial 12', size=(8, 1), pad=(10, (20, 0))),
         sg.Button('Excluir', font='arial 12', size=(9, 1), pad=(10, (20, 0))),
         sg.Button('Fechar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))]
    ]
    winAtl = sg.Window('Alterar cadastro (Cliente)', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                       size=(550, 458), finalize=True)


# CRIA A JANELA DE ALTERAÇÃO DE CASTRO DE PRODUTO
def window_alt_produto(produto, qtd, valor):
    sg.theme('DarkGrey2')

    col_cont1 = [
        [sg.Text('PRODUTO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('QUANTIDADE:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('VALOR R$:', font='arial 13', pad=(0, (0, 15)))],

    ]

    col_cont2 = [
        [sg.Input(produto, size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)),
                  key='alt-produto')],
        [sg.Input(qtd, size=(5, 1), background_color='white', font='arial 12', pad=(0, (0, 15)),
                  key='alt-quantidade')],
        [sg.Input(valor, size=(10, 1), background_color='white', font='arial 12', pad=(0, (0, 15)),
                  key='alt-valor'),
         sg.Text('(0000,00)', font='arial 13', pad=(5, (0, 15)))]
    ]

    layout = [
        [sg.Text('CADASTRO DE PRODUTOS', font='arial 20', pad=(0, (0, 25)))],
        [sg.Column(col_cont1), sg.Text(' ' * 5), sg.Column(col_cont2)],
        [sg.Button('Salvar', button_color='#cccccc', font='arial 12', size=(8, 1), pad=(10, (20, 0))),
         sg.Button('Excluir', font='arial 12', size=(9, 1), pad=(10, (20, 0))),
         sg.Button('Fechar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))]
    ]
    winAtl = sg.Window('Alterar cadastro (Produto)', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                       size=(550, 250), finalize=True)


# CRIA A JANELA DE ALTERAÇÃO DE CADASTRO DE PEDIDO
def window_alt_pedido(cliente):
    sg.theme('DarkGrey2')

    col_cont1 = [
        [sg.Text('CLIENTE:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('Nº DO CLIENTE:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('Nº DO PEDIDO:', font='arial 13', pad=(0, (0, 35)))],
        [sg.Text('PRODUTO:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('QUANTIDADE:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('VALOR R$:', font='arial 13', pad=(0, (0, 15)))],
        [sg.Text('DESCRIÇÃO:', font='arial 13', pad=(0, (20, 30)))],

    ]

    col_cont2 = [
        [sg.Input(cliente, size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)),
                  key='alt-cliente')],
        [sg.Input(size=(5, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='id-clt'),
         sg.Text('Informe o nº e clique "Buscar"', font='arial 13', pad=(10, (0, 15)))],
        [sg.Input(size=(5, 1), background_color='white', font='arial 12', pad=(0, (0, 35)), key='id-ped'),
         sg.Text('Informe o nº e clique "Buscar"', font='arial 13', pad=(10, (0, 35)))],
        [sg.Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-pedido')],
        [sg.Input(size=(5, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-unidades')],
        [sg.Input(size=(10, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-valor'),
         sg.Text('(0000,00)', font='arial 13', pad=(5, (0, 15)))],
        [sg.Multiline(size=(33, 3), background_color='white', font='arial 12', pad=(0, (0, 15)), key='alt-descricao')],

    ]

    layout = [
        [sg.Text('CADASTRO DE PEDIDOS', font='arial 20', pad=(0, (0, 25)))],
        [sg.Column(col_cont1), sg.Text(' ' * 5), sg.Column(col_cont2)],
        [sg.Button('Salvar', button_color='#cccccc', font='arial 12', size=(8, 1), pad=(10, (20, 0))),
         sg.Button('Buscar', font='arial 12', size=(8, 1), pad=(10, (20, 0))),
         sg.Button('Excluir', font='arial 12', size=(9, 1), pad=(10, (20, 0))),
         sg.Button('Fechar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))]
    ]
    winPed = sg.Window('Alterar cadastro (Pedido)', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                        size=(550, 455), finalize=True)


# CRIA A JANELA DE EXCLUÇÃO DE CADASTRO DE PEDIDO
def window_delete_ped(id_clt, nome_alt, ped, qtd_prod, valor):
    sg.theme('DarkGrey2')
    col_l = [
        [sg.Text(f'CLIENTE {id_clt}:', font='arial 13')],
        [sg.Text('PEDIDO:', font='arial 13')],
        [sg.Text('QUANTIDADE:', font='arial 13')],
        [sg.Text('VALOR:', font='arial 13')]
    ]
    col_r = [
        [sg.Text(nome_alt, font='arial 13')],
        [sg.Text(ped, font='arial 13')],
        [sg.Text(qtd_prod, font='arial 13')],
        [sg.Text(valor, font='arial 13')]
    ]
    layout = [
        [sg.Text('EXCLUIR PEDIDO', font='arial 20', pad=(0, (0, 15)))],
        [sg.Column(col_l), sg.Text(' ' * 3), sg.Column(col_r)],
        [sg.Text('Deseja excluir ou cancelar pedido?', font='arial 14', pad=(0, (10, 0)))],
        [sg.Button('Excluir', tooltip='Exclui o pedido e NÃO faz a devolução da quantidade produto para o estoque',
                   button_color='#cccccc', font='arial 12', size=(9, 1), pad=(10, (20, 0))),
         sg.Button('Cancelar', tooltip='Exclui o pedido e faz a devolução da quantidade produto para o estoque',
                   button_color='#cccccc', font='arial 12', size=(11, 1), pad=(10, (20, 0))),
         sg.Button('Voltar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))],
    ]
    windelPed = sg.Window('Excluir Pedido', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                       size=(550, 253), finalize=True)


# CRIA A JANELA DE EXCLUSÃO DE CADASTRO DE PRODUTO
def window_delete_prod(prod):
    sg.theme('DarkGrey2')
    col_l = [
        [sg.Text('PRODUTO:', font='arial 13')]
    ]
    col_r = [
        [sg.Text(prod, font='arial 13')]
    ]
    layout = [
        [sg.Text('EXCLUIR PRODUTO', font='arial 20', pad=(0, (0, 15)))],
        [sg.Column(col_l), sg.Text(' ' * 3), sg.Column(col_r)],
        [sg.Text('Deseja excluir este pedido?', font='arial 14', pad=(0, (10, 0)))],
        [sg.Button('Excluir', button_color='#cccccc', font='arial 12', size=(9, 1), pad=(10, (20, 0))),
         sg.Button('Voltar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))],
    ]
    windelProd = sg.Window('Excluir Pedido', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                       size=(550, 183), finalize=True)


# CRIA A JANELA DE EXCLUSÃO DE CADASTRO DE CLIENTE
def window_delete_clt(cliente, id_clt, end, num, bairro, cidade, fone):
    sg.theme('DarkGrey2')
    col_l = [
        [sg.Text(f'CLIENTE {id_clt}: {cliente}', font='arial 13')],
        [sg.Text(end, font='arial 13')],
        [sg.Text(f'Nº {num}', font='arial 13')],
        [sg.Text(bairro, font='arial 13')],
        [sg.Text(cidade, font='arial 13')],
        [sg.Text(fone, font='arial 13')],
    ]
    layout = [
        [sg.Text('EXCLUIR CLIENTE', font='arial 20', pad=(0, (0, 15)))],
        [sg.Column(col_l, element_justification='center')],
        [sg.Text('Deseja excluir este cliente?', font='arial 14', pad=(0, (10, 0)))],
        [sg.Button('Excluir', button_color='#cccccc', font='arial 12', size=(9, 1), pad=(10, (20, 0))),
         sg.Button('Voltar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))],
    ]
    windelClt = sg.Window('Excluir Pedido', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                       size=(550, 298), finalize=True)




