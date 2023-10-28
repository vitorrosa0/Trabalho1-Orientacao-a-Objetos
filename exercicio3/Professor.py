from Pessoa import Pessoa
from Escola import Escola
from Curso import Curso

class Professor(Pessoa):

    def __init__(self):
        
        self.__escola = Escola()
        self.__curso = Curso()

    def setCurso(self, curso):
        self.__curso = curso
    def getCurso(self):
        return self.__curso
    
    def setEscola(self, escola):
        self.__escola = escola
    def getEscola(self):
        return self.__escola