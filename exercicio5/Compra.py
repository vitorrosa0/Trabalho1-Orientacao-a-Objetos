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
