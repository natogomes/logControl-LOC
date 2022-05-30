import PySimpleGUI as sg
from models import Clientes, Produtos, Pedidos

logo = 'logoLoc.ico'


def post_pedido(id_c, client, ped, qtd_prod, datahora, descricao):
    """
    -> Insere um novo cadastro de pedido no sistema.
    :param id_c: Passa o id do cliente.
    :param client: Passa o nome do cliente.
    :param ped: Passa o nome do produto do pedido.
    :param qtd_prod: Passa a quantidade do produto.
    :param datahora: Passa a data e a hora que foi feito o pedido.
    :param descricao: Passa uma descrição/complemento do pedido (opcional).
    :return: Se "True" retorna um print dos dados do novo pedido.
    """
    produto = Produtos.query.filter_by(produto=ped).first()
    cliente = Clientes.query.filter_by(nome=client).first()
    clientes = Clientes.query.all()

    if client == '' or ped == '':
        sg.Popup(f'ERRO! Verifique se todos os campos foram preenchidos corretamente.',
                 icon=logo, font='arial 12', title='Pedido Erro')

    elif cliente is None:
        sg.Popup(f'{"Cliente não cadastrado.":<43}', icon=logo, font='arial 12', title='Pedido Erro')

    elif produto is None:
        sg.Popup(f'{"Produto não cadastrado.":<43}', icon=logo, font='arial 12', title='Pedido Erro')
    else:
        try:
            id_cliente = int(id_c)
            qtd = int(qtd_prod)
        except (ValueError, TypeError):
            sg.Popup(f'O campo "Quantidade" e/ou "Nº Cliente"\nDevem ser preenchidos com um valor numérico.',
                     icon=logo, font='arial 12', title='Pedido Erro')
        else:
            v_str = str(produto.valor).replace(',', '.')
            v_float = float(v_str)

            if produto.quantidade < qtd:
                sg.Popup(f'Quantidade de produto superior ao estoque.', icon=logo, font='arial 12', title='Pedido Erro')

            else:
                for c in clientes:
                    if c.id == id_cliente and c.nome == cliente.nome:
                        pedido = Pedidos(quantidade=qtd, data=datahora, descricao=descricao, cliente=c,
                                         pedido=produto)
                        produto.quantidade -= qtd
                        valor_final = v_float * qtd
                        pedido.valor = f'{valor_final:.2f}'
                        pedido.save()
                        sg.Popup(f'{"Pedido inserido com sucesso!.":^43}',
                                 icon=logo, font='arial 12', title='Cadastro de pedido')
                        print('PEDIDO CADASTRADO!')
                        print()
                        print(pedido)
                        print('-' * 90)
                        return True
                sg.Popup(f'Nº de cliente não relacionado.',
                         icon=logo, font='arial 12', title='Pedido erro')


class Pedido:
    def __init__(self, entrada):
        cliente = Clientes.query.filter_by(nome=entrada).first()
        produto = Produtos.query.filter_by(produto=entrada).first()
        pedido_pdt = Pedidos.query.filter_by(pedido=produto).first()
        pedidos = Pedidos.query.all()
        produtos = Produtos.query.all()
        clientes = Clientes.query.all()

        self.clientes = clientes
        self.cliente = cliente
        self.pedidos = pedidos
        self.pedido_pdt = pedido_pdt
        self.produto = produto
        self.produtos = produtos

    def get_pedidos(self):
        """
        -> Mostra na tela uma listagem de todos os pedidos cadastrados.
        :return: Sem retorno.
        """
        if not self.pedidos:
            sg.Popup(f'{"Nenhum pedido cadastrado.":^43}', icon=logo, font='arial 12', title='Cadastro Pedidos')
        for p in self.pedidos:
            print(p)
            print('-' * 90)

    def get_pedido(self, prod):
        """
        -> Mostra uma listagem de todos os pedidos feito para o produto solicitado.
        :param prod: Passa o nome do produto a ser solicitado o pedido correspondente.
        :return: Sem retorno.
        """
        if prod == '':
            sg.Popup('Infome um nome de produto.',
                     icon=logo, font='arial 12', title='Pedido Erro')

        elif self.produto is None:
            sg.Popup(f'{"Produto não cadastrado.":^35}',
                     icon=logo, font='arial 12', title='Pedido Erro')

        elif not self.pedido_pdt:
            sg.Popup(f'NENHUM PEDIDO DO PRODUTO ({self.produto.produto}).',
                     icon=logo, font='arial 12', title='Cadastro Pedido')

        else:
            for p in self.pedidos:
                if p.pedido.produto == self.produto.produto:
                    print(p)
                    print('-' * 90)

    def validar_alt_ped(self):
        """
        -> Faz uma validação do cliente vinculado ao pedido antes de abrir a janela para a alteração do cadastro.
        :return: Se "True" retorna o nome do cliente que fez o pedido solicitado.
        """
        try:
            nome = self.cliente.nome
        except:
            sg.Popup(f'Informe um nome de cliente cadastrado.',
                     icon=logo, font='arial 12', title='Cadastro Erro')
            return False
        else:
            return nome

    def buscar_pedido(self, id_clt, id_ped, nome):
        """
        -> Faz uma busca do pedido solicitado para um determinado cliente.
        :param id_clt: Passa o id do cliente.
        :param id_ped: Passa o id do pedido.
        :param nome: Passa o nome do cliente que fez o pedido.
        :return: Retorna uma lista com os dados do pedido solicitado.
        """
        try:
            id_cliente = int(id_clt)
            id_pedido = int(id_ped)
        except:
            sg.Popup(f'Nº de Cliente e/ou Pedido não foram preenchidos corretamente.',
                     icon=logo, font='arial 12', title='Pedido Erro')
        else:
            dados_list = []
            dados_dict = {}
            dados = []
            clts = False
            for c in self.clientes:
                if c.nome == nome and c.id == id_cliente:
                    clts = True
                    for p in self.pedidos:
                        if p.cliente.nome == c.nome and p.cliente.id == id_cliente:
                            ped = p.pedido.produto
                            qtd_ped = p.quantidade
                            valor_ped = p.valor
                            descricao_ped = p.descricao

                            dados_dict['pedido'] = ped
                            dados_dict['quantidade'] = qtd_ped
                            dados_dict['valor'] = valor_ped
                            dados_dict['descricao'] = descricao_ped
                            dados_list.append(dados_dict.copy())
                            dados_dict.clear()

                    if len(dados_list) == 0:
                        sg.Popup(f'Este cliente não tem pedido.',
                                 icon=logo, font='arial 12', title='Pedido erro')

                    elif id_pedido > len(dados_list):
                        sg.Popup(f'{"Número de pedido inválido.":^30}',
                                 icon=logo, font='arial 12', title='Pedido erro')

                    else:
                        pedido = dados_list[id_pedido - 1]['pedido']
                        quantidade = dados_list[id_pedido - 1]['quantidade']
                        valor = dados_list[id_pedido - 1]['valor']
                        descricao = dados_list[id_pedido - 1]['descricao']
                        dados.append(pedido)
                        dados.append(quantidade)
                        dados.append(valor)
                        dados.append(descricao)
                        return dados
            if not clts:
                sg.Popup(f'O Nº de cliente não existe para ({nome}).',
                         icon=logo, font='arial 12', title='Cadastro Erro')
                return clts

    def put_pedido(self, id_c, nome, id_p, ped, qtd_prod, valor, descricao):
        """
        -> Faz uma alteração no cadastro do pedido solicitado.
        :param id_c: Passa o id do cliente que fez o pedido solicitado.
        :param id_p: Passa o id do pedido solicitado.
        :param ped: Passa o pedido(produto) que foi alterado.
        :param qtd_prod: Passa o valor de quantidade do produto em estoque alterado.
        :param descricao: Passa a descrição do pedido alterado (opcional).
        :return: Se "True" retorna um print com os dados atualizados.
        """
        if id_c == '' or nome == '' or id_p == '' or qtd_prod == '' or valor == '':
            sg.Popup(f'Verifque nome e Nº do cliente e o Nº do pedido e clique "Buscar".',
                     icon=logo, font='arial 12', title='Pedido Erro')
            return False
        try:
            id_cliente = int(id_c)
            id_pedido = int(id_p)
        except:
            sg.Popup(f'Verifque se o Nº de Cliente ou Pedido foram preenchidos corretamente.',
                     icon=logo, font='arial 12', title='Pedido Erro')
        else:
            id_ped = 0
            for p in self.pedidos:
                if p.cliente.nome == nome and p.cliente.id == id_cliente:
                    id_ped += 1
                    if id_ped == id_pedido:
                        try:
                            qtd = int(qtd_prod)
                        except:
                            sg.Popup(f'Verifque se o campo "QUANTIDADE" é valor NUMÉRICO.',
                                     icon=logo, font='arial 12', title='Pedido erro')
                            return False
                        else:
                            try:
                                v_str = str(valor).replace(',', '.')
                                v_float = float(v_str)
                                v_float = v_float * qtd
                                v_final = f'{v_float:.2f}'
                            except:
                                sg.Popup(f'Verifque se o campo "VALOR" está no formato R$ (x.xxx,xx).',
                                         icon=logo, font='arial 12', title='Pedido Erro')
                            else:
                                prod_cont = 0
                                for prod in self.produtos:
                                    if prod.produto == ped:
                                        prod_cont += 1
                                        if prod.quantidade - qtd >= 0:
                                            p.pedido.quantidade += p.quantidade
                                            prod.quantidade -= qtd
                                            p.pedido = prod
                                            p.descricao = descricao
                                            p.quantidade = qtd
                                            p.valor = v_final.replace('.', ',')
                                            p.save()
                                            print('ALTERAÇÃO FEITA COM SUCESSO!')
                                            print()
                                            print(f'{p}\n'
                                                  f'{"Pedido:":<18}{id_ped}')
                                            print()
                                            return True
                                        sg.Popup(f'Quantidade de pedido maior do que o estoque.', font='arial 12',
                                                 icon=logo, title='Pedido erro')
                                        return False
                                if ped == '':
                                    sg.Popup(f'Informe um nome de produto válido.', font='arial 12',
                                             icon=logo, title='Pedido erro')
                                    return False

                                elif prod_cont == 0:
                                    sg.Popup(f'Produto alterado não cadastrado.', font='arial 12',
                                             icon=logo, title='Cadastro erro')
                                    return False
            sg.Popup('Nº do cliente não está relacionado ao nome.',
                     icon=logo, font='arial 12', title='Cadastro Erro')
            return False

    def validar_del_ped(self, nome_alt, ped, qtd_prod, valor, id_clt, id_ped):
        """
        -> Faz uma validação de pedido e cliente antes de abrir a janela para exclusão.
        :param nome_alt: Passa o nome do cliente.
        :param ped: Passa o pedido(produto) feito pelo cliente.
        :param qtd_prod: Passa a quantidade do pedido.
        :param id_clt: Passa o id do cliente.
        :param id_ped: Passa o id do pedido.
        :return: Se "True" retorna uma lista com os dados do pedido requsitado.
        """
        dados = list()
        validacao = False
        if nome_alt == '' or ped == '' or qtd_prod == '' or id_clt == '' or id_ped == '' or valor == '':
            sg.Popup(f'Verifique se todos os campos estão preenchidos ou então "Buscar".', font='arial 12',
                     icon=logo, title='Pedido erro')
            return False
        try:
            id_c = int(id_clt)
            id_p = int(id_ped)
        except:
            sg.Popup(f'Nº de cadastro e/ou pedido não foram preenchidos corretamente.', font='arial 12',
                     icon=logo, title='Erro pedido')
        else:
            cont_p = 0
            for p in self.pedidos:
                if p.cliente.nome == nome_alt and p.cliente.id == id_c:
                    cont_p += 1
                    if cont_p == id_p:
                        dados.append(p.cliente.id)
                        dados.append(p.cliente.nome)
                        dados.append(p.pedido.produto)
                        dados.append(p.quantidade)
                        dados.append(p.valor)
            validacao = True
            return dados

    def delete_pedido(self, id_c, id_p, nome):
        """
        -> Faz a exclusão do pedido solicitado sem a devolução da quantidade do produto para o estoque.
        :param id_c: Passa o id do cliente.
        :param id_p: Passa o id do pedido.
        :param nome: Passa o nome do cliente que fez o pedido.
        :return: Sem retorno.
        """
        id_cliente = int(id_c)
        id_pedido = int(id_p)
        cont_p = 0
        for p in self.pedidos:
            if p.cliente.nome == nome and p.cliente.id == id_cliente:
                cont_p += 1
                if cont_p == id_pedido:
                    p.delete()
                    sg.Popup(f'Pedido EXCLUÍDO com sucesso!', font='arial 12',
                             icon=logo, title='Cadastro de Pedido')

    def cancela_pedido(self, id_c, id_p, nome):
        """
        -> Faz o cancelamento do pedido fazendo assim a devolução da quantidade do produto do pedido para o estoque.
        :param id_c: Passa o id do cliente.
        :param id_p: Passa o ido do pedido.
        :param nome: Passa o nome do cliente que fez o pedido.
        :return: Sem retorno.
        """
        id_cliente = int(id_c)
        id_pedido = int(id_p)
        cont_p = 0
        for p in self.pedidos:
            if p.cliente.nome == nome and p.cliente.id == id_cliente:
                cont_p += 1
                if cont_p == id_pedido:
                    p.pedido.quantidade += p.quantidade
                    p.delete()
                    sg.Popup(f'Pedido CANCELADO com sucesso!', font='arial 12',
                             icon=logo, title='Cadastro de Pedido')
