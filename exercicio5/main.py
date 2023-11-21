
from Cliente import Cliente
from Compra import Compra
from Fornecedor import Fornecedor
from Pessoa import Pessoa
from Produto import Produto
from Transacao import Transacao
from Venda import Venda

if __name__ == '__main__':

    cliente1 = Cliente("Marco", "123")
    produto1 = Produto("Caneta", 100, 1.2, 10, 200)
    produto1.vender("26/07/2021", cliente1, 95)
    fornecedor1 = Fornecedor("Antonio", "456")
    produto1.comprar("26/07/2021", fornecedor1, 50, 1.1)
    produto1.exibirHistorico()

class Transacao:
    def __init__(self, dataTransacao, produto, qtde):
        self.dataTransacao = dataTransacao
        self.produto = produto
        self.qtde = qtde

class Compra:
    def __init__(self, dataCompra, produto, fornecedor, qtdeCompra, precoUnit):
        self.dataCompra = dataCompra
        self.produto = produto
        self.fornecedor = fornecedor
        self.qtdeCompra = qtdeCompra
        self.precoUnit = precoUnit

    def comprar(self, produto, qtdeCompra):
        if produto.verificarEstoqueExcedente(qtdeCompra):
            print("Quantidade excede o estoque máximo.")
            return False
        else:
            produto.creditarEstoque(qtdeCompra)
            return True

class Venda:
    def __init__(self, dataVenda, cliente, produto, qtdeVendida):
        self.dataVenda = dataVenda
        self.cliente = cliente
        self.produto = produto
        self.qtdeVendida = qtdeVendida

    def vender(self, produto, qtdeVendida):
        if produto.verificarEstoqueInsuficiente(qtdeVendida):
            print("Estoque insuficiente para a venda.")
            return False
        else:
            produto.debitarEstoque(qtdeVendida)
            valorVenda = produto.calcularValorVenda(qtdeVendida)
            print(f"Valor da venda = {valorVenda}")
            if produto.verificarEstoqueBaixo():
                print("Estoque baixo.")
            return True

class Fornecedor:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, nome, qtdeEstoque, precoUnit, estoqueMinimo, estoqueMaximo):
        self.nome = nome
        self.qtdeEstoque = qtdeEstoque
        self.precoUnit = precoUnit
        self.estoqueMinimo = estoqueMinimo
        self.estoqueMaximo = estoqueMaximo
        self.historico = []

    def debitarEstoque(self, quantidade):
        self.qtdeEstoque -= quantidade

    def creditarEstoque(self, quantidade):
        self.qtdeEstoque += quantidade

    def verificarEstoqueBaixo(self):
        return self.qtdeEstoque < self.estoqueMinimo

    def verificarEstoqueInsuficiente(self, quantidade):
        return quantidade > self.qtdeEstoque

    def verificarEstoqueExcedente(self, quantidade):
        return quantidade + self.qtdeEstoque > self.estoqueMaximo

    def calcularValorVenda(self, quantidade):
        return self.precoUnit * quantidade

    def vender(self, dataVenda, cliente, qtdeVendida):
        venda = Venda(dataVenda, cliente, self, qtdeVendida)
        if venda.vender(self, qtdeVendida):
            self.registrarHistorico(f"Venda do produto {self.nome}")

    def comprar(self, dataCompra, fornecedor, qtdeCompra, precoUnit):
        compra = Compra(dataCompra, self, fornecedor, qtdeCompra, precoUnit)
        if compra.comprar(self, qtdeCompra):
            self.registrarHistorico(f"Compra do produto {self.nome}")

    def registrarHistorico(self, transacao):
        self.historico.append(transacao)

    def exibirHistorico(self):
        for transacao in self.historico:
            print(transacao)



cliente1 = Cliente("Marco", "123")
produto1 = Produto("Caneta", 100, 1.2, 10, 200)
produto1.vender("26/07/2021", cliente1, 95)
fornecedor1 = Fornecedor("Antonio", "456")
produto1.comprar("26/07/2021", fornecedor1, 50, 1.1)
produto1.exibirHistorico()

