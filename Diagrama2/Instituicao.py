

class Instituicao:
    def __init__(self):
        self.__id = 0
        self.__descricao = " "
        self.__turma = []


    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id
 
    
    def setDescricao(self, descricao):
        self.__descricao = descricao
    def getDescricao(self):
        return self.__descricao
 
    
    def setTurma(self, turma):
        self.__turma = turma
    def addTurma(self, turma):
        self.__turma.append(turma)
    def removeTurma(self, turma):
        self.__turma.remove(turma)
    def getTurma(self):
        return self.__turma


    def __str__(self):
        return f"**** Id: {self.getId()}, Descrição:{self.getDescricao()}"
