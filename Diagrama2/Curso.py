from Turma import Turma

class Curso:
    def __init__(self):
        self.__id = 0
        self.__descricao = " "
        self.__disciplina = []
        self.__professor = []


    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id


    def setDescricao(self, descricao):
        self.__descricao = descricao
    def getDescricao(self):
        return self.__descricao



    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina
    def addDisciplina(self, disciplina):
        self.__disciplina.append(disciplina)
    def removeDisciplina(self, disciplina):
        self.__disciplina.remove(disciplina)
    def getDisciplina(self):
        return self.__disciplina


    def setProfessor(self, professor):
        self.__professor = professor
    def addProfessor(self, professor):
        self.__professor.append(professor)
    def removeProfessor(self, professor):
        self.__professor.remove(professor)
    def getProfessor(self):
        return self.__professor

    
    def __str__(self):
        return f"**** Id: {self.getId()}, Descrição:{self.getDescricao()}"
    
