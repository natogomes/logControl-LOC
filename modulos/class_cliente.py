import PySimpleGUI as sg
from models import Clientes, Pedidos

logo = 'logoLoc.ico'


def post_cliente(nome, endr, numr, bairro, cidade, cel, comp='**Opcional'):
    """
    -> Cria um novo cadastro de cliente na tabela (Clientes).
    :param nome: Recebe o nome do cliente.
    :param endr: Recebe o endereço do cliente.
    :param numr: Recebe o número da residência do cliente.
    :param bairro: Recebe o nome do bairro do cliente.
    :param cidade: Recebe o nome da Cidade do cliente.
    :param cel: Recebe o nº de telefone celular do cliente.
    :param comp: Recebe algum valor complementar para o cadastro.
    :return: Sem retorno.
    """
    if nome == '' or endr == '' or numr == '' or bairro == '' or cidade == '' or cel == '':
        sg.Popup(f'Verifque se os campos foram preenchidos corretamente.',
                 icon=logo, font='arial 12', title='Cadastro Erro')
    elif len(cel) < 11:
        sg.Popup(f'Verifque se o campo "CEL" foi preenchido corretamente.\n'
                 f'DDD + número (só números) total 11 números.',
                 icon=logo, font='arial 12', title='Cadastro Erro')
    else:
        try:
            fone = int(cel)
        except:
            sg.Popup(f'Verifque se o campo "CEL" foi preenchido corretamente (só números).',
                     icon=logo, font='arial 12', title='Cadastro Erro')
        else:
            cliente = Clientes(nome=nome, end=endr, num=numr, complemento=comp, bairro=bairro, cidade=cidade,
                               fone=fone)
            cliente.save()
            sg.Popup(f'{"Cliente inserido com sucesso!.":^40}', icon=logo, font='arial 12', title='Cliente cadastrado')
            print('CLIENTE CADASTRADO!')
            print()
            print(cliente)
            print('-' * 90)
            return True


class Cliente:
    def __init__(self, nome):
        cliente = Clientes.query.filter_by(nome=nome).first()
        pedido = Pedidos.query.filter_by(cliente=cliente).first()
        clientes = Clientes.query.all()
        pedidos = Pedidos.query.all()
        self.entrada = nome
        self.cliente = cliente
        self.clientes = clientes
        self.pedidos = pedidos
        self.pedido = pedido

    def get_clientes(self):
        """
        -> Mostra uma listagem na tela de todos os clientes cadastrados.
        :return: O retorno é o print.
        """
        if not self.clientes:
            sg.Popup(f'{"Nenhum cliente cadastrado.":^44}', icon=logo, font='arial 12', title='Cadastro Clientes')
        for c in self.clientes:
            print(f'Cliente {c.id}:  {c.nome}')
            print('-' * 90)

    def get_cliente(self):
        """
        -> Mostra uma listagem na tela de cliente ou clientes(caso tenha mais de um cliente com o mesmo nome),
         filtrado pelo nome.
        :return: Retorna o print.
        """
        if self.entrada == '':
            sg.Popup(f'{"Infome um nome de cliente.":>30}', icon=logo, font='arial 12', title='Cliente Erro')

        elif self.cliente is None:
            sg.Popup(f'Cliente ({self.entrada}) não cadastrado.', icon=logo, font='arial 12', title='Cliente Erro')
        else:
            for c in self.clientes:
                if c.nome == self.cliente.nome:
                    print('DADOS DO CLIENTE:')
                    print()
                    print(c)
                    print()
                    id_ped = 0
                    for p in self.pedidos:
                        if p.cliente.id == c.id:
                            id_ped += 1
                            print(f'PEDIDO Nº {id_ped}:')
                            print()
                            print(f'{"Pedido:":<18}{p.pedido.produto}')
                            print(f'{"Quantidade:":<14}{p.quantidade}')
                            print(f'{"Valor R$:":<18}{p.valor}'.replace('.', ','))
                            print(f'{"Data/Hora:":<16}{p.data}')
                            print(f'{"Descrição:":<16}{p.descricao}')
                            print()
                    if id_ped == 0:
                        print(f'CLIENTE NÃO TEM PEDIDO.')
                    print('-' * 90)

    def validar_alt_clt(self):
        """
        -> Faz uma validação do cliente antes de abrir a janela para fazer alteração de cadastro.
        :return: Retorna o Nome do cliente validado.
        """
        try:
            nome = self.cliente.nome
        except:
            sg.Popup(f'Informe um nome de cliente cadastrado.', icon=logo, font='arial 12', title='Cadastro Erro')
            return False
        else:
            return nome

    def buscar_dados(self, id_c, nome):
        """
        -> Faz um busca pelos pelos dados do cliente solicitado pelo nome e id.
        :param id_c: Passa o valor do id do cliente a ser solicitado.
        :param nome: Passa o nome do cliente a ser solicitado.
        :return: Retorna uma lista com os dados do cliente selecionado.
        """
        try:
            id_cliente = int(id_c)
        except:
            sg.Popup(f'Verifque se o Nº de cadastro foi preenchido corretamente.',
                     icon=logo, font='arial 12', title='Cadastro Erro')
        else:
            contador = False
            for c in self.clientes:
                if c.nome == nome and c.id == id_cliente:
                    contador = True
                    end = c.end
                    num = c.num
                    comp = c.complemento
                    cel = c.fone
                    bairro = c.bairro
                    cidade = c.cidade
                    dados = [end, num, comp, cel, bairro, cidade]
                    return dados
            if not contador:
                sg.Popup(f'O Nº de cadastro não existe para cliente ({nome}).',
                         icon=logo, font='arial 12', title='Cadastro Erro')
                return contador

    def put_cliente(self, id_cliente, nome, novo_nome, end, num, bairro, cidade, cel, comp):
        """
        -> Faz alterações no cadastro de clientes.
        :param id_cliente: Id do cliente a ser solicitado.
        :param nome: Nome do cliente a ser solicitado.
        :param novo_nome: Nome com as alterações feitas(caso faça alteração no nome).
        :param end: Endereço com as alterações feitas(caso faça alteração no nome).
        :param num: Número da residência com as alterações feitas(caso faça alteração no nome).
        :param bairro: Nome do bairro com as alterações feitas(caso faça alteração no nome).
        :param cidade: Nome da cidade com as alterações feitas(caso faça alteração no nome).
        :param cel: Nº do celular com as alterações feitas(caso faça alteração no nome).
        :param comp: Complemento do cadastro com as alterações feitas(caso faça alteração no nome).
        :return: Retorna "True" se encontrar os dados do cliente e "False" caso não encontre.
        """
        try:
            id_c = int(id_cliente)
        except:
            sg.Popup(f'Verifque se o Nº de cadastro foi preenchido corretamente.',
                     icon=logo, font='arial 12', title='Cadastro Erro')
        else:
            if novo_nome == '' or end == '' or num == '' or bairro == '' or cidade == '' or cel == '':
                sg.Popup(f'Verifque se todos campos estão preenchidos ou "Buscar".',
                         icon=logo, font='arial 12', title='Cliente Erro')
                return False
            elif len(cel) < 11:
                sg.Popup(f'Verifque se o campo "CEL" foi preenchido corretamente.\n'
                         f'DDD + número (só números) total 11 números.',
                         icon=logo, font='arial 12', title='Cadastro Erro')
            else:
                try:
                    fone = int(cel)
                except:
                    sg.Popup(f'Verifque se o campo "CEL" foi preenchido corretamente (só números).',
                             icon=logo, font='arial 12', title='Cadastro Erro')
                else:
                    clt = 0
                    for c in self.clientes:
                        if c.nome == nome and c.id == id_c:
                            clt += 1
                            c.nome = novo_nome
                            c.end = end
                            c.num = num
                            c.complemento = comp
                            c.bairro = bairro
                            c.cidade = cidade
                            c.fone = fone
                            c.save()
                            print(f'ALTERAÇÃO FEITA COM SUCESSO!')
                            print()
                            print(c)
                            return True

                        elif c.nome == novo_nome and c.id == id_c:
                            clt += 1
                            c.nome = novo_nome
                            c.end = end
                            c.num = num
                            c.complemento = comp
                            c.bairro = bairro
                            c.cidade = cidade
                            c.fone = fone
                            c.save()
                            print(f'ALTERAÇÃO FEITA COM SUCESSO!')
                            print()
                            print(c)
                            return True
                    if clt == 0:
                        sg.Popup('Nº do cliente não está relacionado ao nome.',
                                 icon=logo, font='arial 12', title='Cadastro Erro')

    def validar_del_clt(self, id_cliente, novo_nome, end, num, bairro, cidade, cel):
        """
        -> Faz uma validação e confirmação do cliente a ser excluído antes de abrir a janela para excluir.
        :param id_cliente: Id do cliente a ser excluído.
        :param novo_nome: Nome do cliente a ser excluído.
        :param end: Endereço do cliente a ser excluído.
        :param num: Numero residencial do cliente a ser excluído.
        :param bairro: Nome do bairro do cliente a ser excluído.
        :param cidade: Nome da cidade do cliente a ser excluído.
        :param cel: Nº do celular do cliente a ser excluído.
        :return: Retorna "False" caso não valide e "True" Retorna uma lista de dados confirmados.
        """
        dados = list()
        validacao = False
        if id_cliente == '' or novo_nome == '' or end == '' or num == '' or bairro == ''\
                or cidade == '' or cel == '':
            sg.Popup(f'Verifique se todos os campos estão preenchidos ou então "Buscar".', font='arial 12',
                     icon=logo, title='Cliente erro')
            return False
        try:
            id_c = int(id_cliente)
        except:
            sg.Popup(f'Nº de cadastro não foi preenchido corretamente (numérico).', font='arial 12',
                     icon=logo, title='Cliente erro')
        else:
            for p in self.pedidos:
                if p.cliente.nome == novo_nome and p.cliente.id == id_c:
                    sg.Popup(f'{"NÃO AUTORIZADO!":^87}\n'
                             f'O Cliente {id_c} ({self.cliente.nome}) está vinculado a um ou mais pedidos.',
                             icon=logo, font='arial 12', title='Cliente Erro')
                    return False

            for c in self.clientes:
                if c.nome == novo_nome and c.id == id_c:
                    dados.append(c.nome)
                    dados.append(c.id)
                    dados.append(c.end)
                    dados.append(c.num)
                    dados.append(c.bairro)
                    dados.append(c.cidade)
                    dados.append(c.fone)

            validacao = True
            return dados

    def delete_cliente(self, id_c, nome_clt):
        """
        -> Exclui o cadastro do cliente solicitado.
        :param id_c: Id do cliente solicitado.
        :param nome_clt: Nome do cliente solicitado.
        :return: Sem retorno.
        """
        try:
            id_clt = int(id_c)
        except:
            sg.Popup(f'Nº de cadastro não foi preenchido corretamente (numérico).', font='arial 12',
                     icon=logo, title='Erro cliente')
        else:
            for c in self.clientes:
                if c.nome == nome_clt and c.id == id_clt:
                    c.delete()
                    sg.Popup(f'{"Cadastro de cliente excluído.":^35}',
                             icon=logo, font='arial 12', title='Excluir Cliente')







