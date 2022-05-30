import PySimpleGUI as sg
from models import Produtos, Pedidos

logo = 'logoLoc.ico'


class Produto:
    def __init__(self, prod):
        produto = Produtos.query.filter_by(produto=prod).first()
        pedido = Pedidos.query.filter_by(pedido=produto).first()
        produtos = Produtos.query.all()
        pedidos = Pedidos.query.all()
        self.entrada = prod
        self.produto = produto
        self.produtos = produtos
        self.pedidos = pedidos
        self.pedido = pedido

    def get_produtos(self):
        """
        -> Faz uma listagem de todos os produtos cadastrados.
        :return: Retorna o print.
        """
        if not self.produtos:
            sg.Popup(f'{"Nenhum produto cadastrado.":^43}', icon=logo, font='arial 12', title='Cadastro Produtos')
        for p in self.produtos:
            print(p)
            print('-' * 90)

    def get_produto(self):
        """
        -> Mostra o produto solicitado.
        :return: Retorna o print
        """
        if self.entrada == '':
            sg.Popup(f'{"Infome um nome de produto.":^30}', icon=logo, font='arial 12', title='Produto Erro')

        elif self.produto is None:
            sg.Popup(f'Produto ({self.entrada}) não cadastrado.', icon=logo, font='arial 12', title='Produto Erro')
        else:
            print(self.produto)
            print('-' * 90)

    def post_produto(self, prod, quantidade, valor):
        """
        -> Cadastra um novo produto no sistema.
        :param prod: Passa o nome do produto a ser cadastrado.
        :param quantidade: Passa a quantidade do produto em estoque.
        :param valor: Passa o valor do produto cadastrado.
        :return: Retorna o Print dos dados do produto cadastrado. Se "False" quando ja tem o produto do mesmo
        nome cadastrado.
        """
        if prod == '' and valor == '':
            sg.Popup(f'Verifque se todos os campos foram preenchidos.',
                     icon=logo, font='arial 12', title='Produto Erro')
        else:
            try:
                qtd = int(quantidade)
                v_str = str(valor).replace(',', '.')
                v_float = float(v_str)
                v_final = f'{v_float:.2f}'
            except (ValueError, TypeError):
                sg.Popup(f'Verifque se o campo "QUANTIDADE" é valor NUMÉRICO\n'
                         f'e se o campo "VALOR" está no formato R$ (xxxx,xx).\n',
                         icon=logo, font='arial 12', title='Produto Erro')
            else:
                for p in self.produtos:
                    if p.produto == prod:
                        sg.Popup('Este produto ja está cadastrado.',
                                 icon=logo, font='arial 12', title='Produto Erro')
                        return False

                produto = Produtos(produto=prod, quantidade=qtd, valor=v_final)
                produto.save()
                sg.Popup(f'{"Produto inserido com sucesso!.":^40}',
                         icon=logo, font='arial 12', title='Produto cadastrado')
                print('PRODUTO CADASTRADO!')
                print()
                print(produto)
                print('-' * 90)
                return True

    def validar_alt_prod(self):
        """
        -> Faz uma validação do produto antes de abrir a janela para alteração do cadastro de produto.
        :return: Se "True" retorna uma lista com os dados do cadastro de produto.
        """
        try:
            prod = self.produto.produto
        except:
            sg.Popup(f'Informe um nome de produto cadastrado.', icon=logo, font='arial 12', title='Cadastro Erro')
            return False
        else:
            dados = [prod, self.produto.quantidade, self.produto.valor.replace('.', ',')]
            return dados

    def put_produto(self, prod, novo_prod, quantidade, valor):
        """
        -> Faz alteração nos dados do produto cadastrado em seção.
        :param novo_prod: Passa o nome do produto alterado.
        :param quantidade: Passa a quantidade de produto alterado.
        :param valor: Passa o valor do produto alterado.
        :return: Retorna "True" e "False". Se True, mostra na tela um print do cadastro alterado
        """
        valid = False
        if novo_prod == '' and valor == '':
            sg.Popup(f'Verifque se os campos foram preenchidos.',
                     icon=logo, font='arial 12', title='Produto Erro')
        else:
            try:
                qtd = int(quantidade)
                v_str = str(valor).replace(',', '.')
                v_float = float(v_str)
                v_final = f'{v_float:.2f}'
            except:
                sg.Popup(f'Verifque se o campo "QUANTIDADE" é valor NUMÉRICO\n'
                         f'e se o campo "VALOR" está no formato R$ (xxxx,xx).',
                         icon=logo, font='arial 12', title='Produto Erro')
            else:
                for p in self.produtos:
                    if p.produto == prod:
                        p.produto = novo_prod
                        p.quantidade = qtd
                        p.valor = v_final
                        p.save()
                        print('ALTERAÇÃO FEITA COM SUCESSO!')
                        print()
                        print(p)
                        valid = True
                        return valid

                    elif p.produto == novo_prod:
                        p.produto = novo_prod
                        p.quantidade = qtd
                        p.valor = v_final
                        p.save()
                        print('ALTERAÇÃO FEITA COM SUCESSO!')
                        print()
                        print(p)
                        valid = True
                        return valid

    def validar_del_prod(self):
        """
        -> Faz uma validação dos dados do produto antes de abrir a janela para exclusão de cadastro.
        :return: Se True, a janela de exclusão e aberta e se False a exclusão não está autorizada.
        """
        if self.pedido is None:
            return True
        else:
            sg.Popup(f'{"NÃO AUTORIZADO!":^87}\n'
                     f'O Produto ({self.produto.produto}) está vinculado a um ou mais pedidos.',
                     icon=logo, font='arial 12', title='Produto Erro')
            return False

    def delete_produto(self, prod):
        """
        -> Faz a exclusão do cadastro do produto solicitado.
        :return: Sem retorno.
        """
        for p in self.produtos:
            if p.produto == prod:
                p.delete()
                sg.Popup(f'{"Cadastro de produto excluído.":^33}',
                         icon=logo, font='arial 12', title='Excluir Produto')

