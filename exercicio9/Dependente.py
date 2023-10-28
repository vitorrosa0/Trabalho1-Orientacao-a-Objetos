from Pessoa import Pessoa
from Funcionario import Funcionario
from datetime import date
from datetime import datetime

class Dependente(Pessoa):
    def __init__(self):
        self.__dataNascimento = None
        self.__funcionario = Funcionario()

    def setFuncionario (self, funcionario):
        self.__funcionario = funcionario
    def getFuncionario(self):
        return self.__funcionario
    
    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
    def getDataNascimento(self):
        return self.__dataNascimento


    def getData(dataAtual):
        dataTexto = dataAtual.strftime("%d/%m/%Y")
        print(dataTexto)