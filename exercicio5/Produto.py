from Venda import Venda
from Compra import Compra

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
