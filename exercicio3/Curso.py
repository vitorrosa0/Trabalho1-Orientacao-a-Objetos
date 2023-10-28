from TipoEnsino import TipoEnsino

from Escola import Escola

class Curso:

    def __init__(self):
        self.__aluno = []
        self.__tipoEnsino = TipoEnsino()
        self.__professor = []
        self.__escola = Escola()

    def setAluno(self, aluno):
        self.__aluno = aluno
    def addAluno(self, aluno):
        self.__aluno.append(aluno)
    def removeAluno(self, aluno):
        self.__aluno.remove(aluno)
    def getAluno(self):
        return self.__aluno
    
    def setTipoEnsino(self, tipoEnsino):
        self.__tipoEnsino = tipoEnsino
    def getTipoEnsino(self):
        return self.__tipoEnsino
    
    def setProfessor(self, professor):
        self.__professor = professor
    def addProfessor(self, professor):
        self.__professor.append(professor)
    def removeProfessor(self, professor):
        self.__professor.remove(professor)
    def getProfessor(self):
        return self.__professor
    
    def setEscola(self, escola):
        self.__escola = escola
    def getEscola(self):
        return self.__escola