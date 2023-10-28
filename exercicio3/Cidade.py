from Estado import Estado

class Cidade:

    def __init__(self):
        self.__pessoa = []
        self.__estado = Estado()

    def setPessoa(self, pessoa):
        self.__pessoa = pessoa
    def addPessoa(self, pessoa):
        self.__pessoa.append(pessoa)
    def removePessoa(self, pessoa):
        self.__pessoa.remove(pessoa)
    def getPessoa(self):
        return self.__pessoa
    
    def setEstado(self, estado):
        self.__estado = estado
    def getEstado(self):
        return self.__estado