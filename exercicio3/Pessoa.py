from Escolaridade import Escolaridade
from Cidade import Cidade

class Pessoa:

    def __init__(self):
        self.__escolaridade = Escolaridade()
        self.__cidade = Cidade()

    def setCidade(self, cidade):
        self.__cidade = cidade
    def getCidade(self):
        return self.__cidade

    def setEscolaridade(self, escolaridade):
        self.__escolaridade = escolaridade
    def getEscolaridade(self):
        return self.__escolaridade
    
    