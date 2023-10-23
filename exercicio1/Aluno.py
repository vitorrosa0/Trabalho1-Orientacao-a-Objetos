from Pessoa import Pessoa
from Turma import Turma
from Curso import Curso

class Aluno(Pessoa):
    def __init__(self):
        self.__turma = Turma()
        self.__curso = Curso()
    
    
    def setTurma(self, turma):
        self.__turma = turma
    def getTurma(self):
        return self.__turma
    

    def setCurso(self, curso):
        self.__curso = curso
    def getCurso(self):
        return self.__curso


    def __str__(self):
        return f"**** Nome: {self.getNome()}, Turma: {self.getTurma()}, Curso: {self.getCurso()}"