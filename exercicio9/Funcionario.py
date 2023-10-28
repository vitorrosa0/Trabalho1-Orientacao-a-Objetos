from Pessoa import Pessoa
from Cargo import Cargo


class Funcionario(Pessoa):

    def __init__(self):
        self.__cargo = Cargo()
        self.__ocorrencia = []
        self.__dependente = []

    def setCargo (self, cargo):
        self.__cargo = cargo
    def getCargo(self):
        return self.__cargo
    
    def setOcorrencia(self, ocorrencia):
        self.__ocorrencia = ocorrencia
    def addOcorrencia(self, ocorrencia):
        self.__ocorrencia.append(ocorrencia)
    def removeOcorrencia(self, ocorrencia):
        self.__ocorrencia.remove(ocorrencia)
    def getOcorrencia(self):
        return self.__ocorrencia
    
    def setDependente(self, dependente):
        self.__dependente = dependente
    def addDependente(self, dependente):
        self.__dependente.append(dependente)
    def removeDependente(self, dependente):
        self.__dependente.remove(dependente)
    def getDependente(self):
        return self.__dependente



    def calcularSalarioLiquido(mes, ano):
        salario = 

    def exibirDependentes():
