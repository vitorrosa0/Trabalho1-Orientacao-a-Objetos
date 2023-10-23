import Aluno

class Situacao:
    def __init__(self):
        self.__situacao = ""
        self.__anoSemestre = 0
        self.__aluno = []


    def setSituacao(self,situacao):
        self.__situacao = situacao
    def getSituacao(self):
        return self.__situacao


    def setAnoSemestre(self,anoSemestre):
        self.__anoSemestre = anoSemestre
    def getAnoSemestre(self):
        return self.__anoSemestre


    def setAluno(self, aluno):
        self.__aluno = aluno
    def addAluno(self, aluno):
        self.__aluno.append(aluno)
    def removeAluno(self, aluno):
        self.__aluno.remove(aluno)
    def getAluno(self):
        return self.__aluno

    
    def __str__(self):
        return f"**** Situação: {self.getSituacao()}, Semestre:{self.getAnoSemestre()}"