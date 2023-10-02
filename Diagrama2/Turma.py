from Professor import Professor
from Disciplina import Disciplina


class Turma:

    def __init__(self):
        
        self.__id = 0
        self.__descricao = " "
        self.__ano = 0
        self.__semestre = 0
        self.__professor = None
        self.__instituicao = None
        self.__disciplina = None
        self.__diario = []


    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id


    def setDescricao(self, descricao):
        self.__descricao = descricao
    def getDescricao(self):
        return self.__descricao


    def setAno(self, ano):
        self.__ano = ano
    def getAno(self):
        return self.__ano


    def setSemestre(self, semestre):
        self.__semestre = semestre
    def getSemestre(self):
        return self.__semestre


    def setProfessor(self, professor):
        self.__professor = professor
    def getProfessor(self):
        return self.__professor


    def setInstituicao(self, instituicao):
        self.__instituicao = instituicao
    def getInstituicao(self):
        return self.__instituicao


    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina
    def getDisciplina(self):
        return self.__disciplina
    

    def setDiario(self, diario):
        self.__diario = diario
    def addDiario(self, diario):
        self.__diario.append(diario)
    def removeDiario(self, diario):
        self.__diario.remove(diario)
    def getDiario(self):
        return self.__diario


    def __str__(self):
        return f"**** ID: {self.getId()}, Descrição: {self.getDescricao()}, Ano: {self.getAno()}, Semestre: {self.getSemestre()}"