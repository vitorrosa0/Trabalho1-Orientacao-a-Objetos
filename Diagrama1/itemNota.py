class ItemNota:

    def __init__(self):

        self.__id = 0
        self.__vrUnitario = 0
        self.__quantidade = 0
        self.__produto = None
        self.__nota = None


    def setId(self,id):
        self.__id = id
    def getId(self):
        return self.__id 


    def setVrUnitario(self, vrUnitario):
        self.__vrUnitario = vrUnitario
    def getVrUnitario(self):
        return self.__vrUnitario


    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade
    def getQuantidade(self):
        return self.__quantidade


    def setProduto(self,produto):
        self.__produto = produto
    def getProduto(self):
        return self.__produto


    def setNota(self,nota):
        self.__nota = nota
    def getNota(self):
        return self.__nota


    def __str__(self):
        return f'**** ID Item Nota : {self.getId()}, Valor Unitário: {self.getVrUnitario()}, Quantidade: {self.getQuantidade()}' 