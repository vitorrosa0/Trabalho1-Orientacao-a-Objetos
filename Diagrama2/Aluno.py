from Pessoa import Pessoa
from Situacao import Situacao

class Aluno(Pessoa):
    def __init__(self):
        self.__matricula = ""
        self.__anoInicio = 0
        self.__semestreInicio = 0
        self.__situacao = None
        self.__diario = []

    
    def setMatricula(self,matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula
 
    
    def setAnoInicio(self,anoInicio):
        self.__anoInicio = anoInicio
    def getAnoInicio(self):
        return self.__anoInicio

    
    def setSemestreInicio(self,semestreInicio):
        self.__semestreInicio = semestreInicio
    def getSemestreInicio(self):
        return self.__semestreInicio

    
    def setSituacao(self,situacao):
        self.__situacao = situacao
    def getSituacao(self):
        return self.__situacao


    def setDiario(self, diario):
        self.__diario = diario
    def addDiario(self, diario):
        self.__diario.append(diario)
    def removeDiario(self, diario):
        self.__diario.remove(diario)
    def getDiario(self):
        return self.__diario


    def __str__(self):
        return f"**** ID: {self.getId()}, Nome: {self.getNome()}, CPF: {self.getCpf()}, Data de Nascimento: {self.getDataNascimento()}, Email: {self.getEmail()}, Endereço: {self.getEndereco()}, Telefone: {self.getTelefone()}, Identidade: {self.getIdentidade()}, Matricula: {self.getMatricula()}, Ano de início:{self.getAnoInicio()}, Semestre:{self.getSemestreInicio()}"