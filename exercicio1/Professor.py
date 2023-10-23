from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self):
        
        self.__turma = []
        
    
    def setTurma(self, turma):
        self.__turma = turma
    def addTurma(self, turma):
        self.__turma.append(turma)
    def removeTurma(self, turma):
        self.__turma.remove(turma)
    def getTurma(self):
        return self.__turma
    
    


    def __str__(self):
        return f"**** Nome: {self.getNome()}, Turmas: {self.getTurma()}"