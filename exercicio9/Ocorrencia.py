from Funcionario import Funcionario

class Ocorrencia:

    def __init__(self):
        
        self.__dataOcorrencia = None
        self.__valorAcrescimo = 0.0
        self.__valorDesconto = 0.0
        self.__descricaoOcorrencia = ""
        self.__funcionario = Funcionario()

    def setDataOcorrencia (self, dataOcorrencia):
        self.__dataOcorrencia = dataOcorrencia
    def getDataOcorrencia(self):
        return self.__dataOcorrencia
    
    def setValorAcrescimo (self, valorAcrescimo):
        self.__valorAcrescimo = valorAcrescimo
    def getValorAcrescimo(self):
        return self.__valorAcrescimo

    def setValorDesconto (self, valorDesconto):
        self.__valorDesconto = valorDesconto
    def getValorDesconto(self):
        return self.__valorDesconto
    
    def setDescricaoOcorrencia (self, descricaoOcorrencia):
        self.__descricaoOcorrencia = descricaoOcorrencia
    def getDescricaoOcorrencia(self):
        return self.__descricaoOcorrencia
    
    def setFuncionario (self, funcionario):
        self.__funcionario = funcionario
    def getFuncionario(self):
        return self.__funcionario