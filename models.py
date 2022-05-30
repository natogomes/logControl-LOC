from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# pip install sqlalchemy

engine = create_engine('sqlite:///clientes.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


# tabela de clientes
class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    end = Column(String(50))
    num = Column(String(10))
    complemento = Column(String(50))
    bairro = Column(String(30))
    cidade = Column(String(30))
    fone = Column(String(20))

    def __repr__(self):
        return f'{"Nome"}{":":<14}{self.nome}\n' \
               f'{"Nº Cliente":<17}{self.id}\n' \
               f'{"Endereço:":<15}{self.end}\n' \
               f'{"Nº:":<23}{self.num}\n' \
               f'{"Compl.:":<18}{self.complemento}\n' \
               f'{"Fone:":<20}({self.fone[:2]}){self.fone[2:3]}.{self.fone[3:7]}-{self.fone[7:]}\n' \
               f'{"Bairro:":<20}{self.bairro}\n' \
               f'{"Cidade:":<18}{self.cidade}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


# tabela de pedidos
class Pedidos(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    quantidade = Column(Integer)
    data = Column(String(20))
    descricao = Column(String(300))
    cliente = relationship('Clientes')
    pedido = relationship('Produtos')
    valor = Column(String(20))
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    pedido_id = Column(Integer, ForeignKey('produtos.id'))

    def __repr__(self):
        nome = f'{"Nome:":<18}{self.cliente.nome}\n'
        num = f'{"Cliente Nº:":<17}{self.cliente.id}\n'
        ped = f'{"Pedido:":<18}{self.pedido.produto}\n'
        qtd = f'{"Quantidade:":<14}{self.quantidade}\n'
        valor = f'{"Valor R$:":<18}{self.valor}\n'.replace('.', ',')
        data = f'{"Data/Hora:":<16}{self.data}\n'
        desc = f'{"Descrição:":<16}{self.descricao}'

        return f'{nome}{num}{ped}{qtd}{valor}{data}{desc}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


# tabela de produtos
class Produtos(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    produto = Column(String(90), index=True)
    quantidade = Column(Integer)
    valor = Column(String(20))

    def __repr__(self):
        produto = f'{"Produto:":<17}{self.produto}\n'
        qtd = f'{"Quantidade:":<14}{self.quantidade}\n'
        valor = f'{"Valor R$:":<18}{self.valor}'.replace('.', ',')

        return f'{produto}{qtd}{valor}'


    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
