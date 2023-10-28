class Escolaridade:

    def __init__(self):

        self.__tipoescolaridade = ""
        self.__pessoa = []

    def setTipoEscolaridade(self, tipoescolaridade):
        self.__tipoescolaridade = tipoescolaridade
    def getTipoEscolaridade(self):
        return self.__tipoescolaridade

    def setPessoa(self, pessoa):
        self.__pessoa = pessoa
    def addPessoa(self, pessoa):
        self.__pessoa.append(pessoa)
    def removePessoa(self, pessoa):
        self.__pessoa.remove(pessoa)
    def getPessoa(self):
        return self.__pessoa
    

    
    
    
     