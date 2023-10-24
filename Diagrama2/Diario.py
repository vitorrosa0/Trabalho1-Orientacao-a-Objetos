from Aluno import Aluno
from Turma import Turma

class Diario:
    def __init__(self):

        self.__v1 = 0.0
        self.__v2 = 0.0
        self.__vS = 0.0
        self.__vT = 0.0
        self.__faltas = 0
        self.__aluno = Aluno()
        self.__turma = Turma()


    def setV1(self, v1):
        self.__v1 = v1
    def getV1(self):
        return self.__v1


    def setV2(self, v2):
        self.__v2 = v2
    def getV2(self):
        return self.__v2


    def setVS(self, vS):
        self.__vS = vS
    def getVS(self):
        return self.__vS


    def setVT(self, vT):
        self.__vT = vT
    def getVT(self):
        return self.__vT


    def setFaltas(self, faltas):
        self.__faltas = faltas
    def getFaltas(self):
        return self.__faltas


    def setAluno(self, aluno):
        self.__aluno = aluno
    def getAluno(self):
        return self.__aluno


    def setTurma(self, turma):
        self.__turma = turma
    def getTurma(self):
        return self.__turma


    def __str__(self):
        return f"**** V1: {self.getV1()}, V2: {self.getV2()}, VS: {self.getVS()}, VT: {self.getVT()}, Faltas: {self.getFaltas()}"