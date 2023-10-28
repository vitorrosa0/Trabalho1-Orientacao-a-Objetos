from Pessoa import Pessoa
from Curso import Curso


class Aluno(Pessoa):

    def __init__(self):
        
        self.__curso = Curso()

    def setCurso(self, curso):
        self.__curso = curso
    def getCurso(self):
        return self.__curso
