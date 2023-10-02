class Produto:

    def __init__(self):

        self.__id = 0
        self.__codigo = " "
        self.__descricao = " "
        self.__itemNota = []


    def setId(self,id):
        self.__id = id
    def getId(self):
        return self.__id 


    def setCodigo(self, codigo):
        self.__codigo = codigo
    def getCodigo(self):
        return self.__codigo


    def setDescricao(self, descricao):
        self.__descricao = descricao
    def getDescricao(self):
        return self.__descricao


    def setItemNota(self, itemNota):
        self.__itemNota = itemNota
    def addItemNota(self, itemNota):
        self.__itemNota.append(itemNota)
    def removeItemNota(self, itemNota):
        self.__itemNota.remove(itemNota)
    def getItemNota(self):
        return self.__itemNota


    def __str__(self):
        return f'**** ID Produto: {self.getId()}, Código {self.getCodigo()}, Descrição: {self.getDescricao()}'