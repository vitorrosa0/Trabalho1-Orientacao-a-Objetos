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
