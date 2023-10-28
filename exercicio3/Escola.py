from Cidade import Cidade

class Escola:

    def __init__(self):

        self.__professor = []
        self.__curso = []
        self.__cidade = Cidade()

    def setProfessor(self, professor):
        self.__professor = professor
    def addProfessor(self, professor):
        self.__professor.append(professor)
    def removeProfessor(self, professor):
        self.__professor.remove(professor)
    def getProfessor(self):
        return self.__professor

    def setCurso(self, curso):
        self.__curso = curso
    def addCurso(self, curso):
        self.__curso.append(curso)
    def removeCurso(self, curso):
        self.__curso.remove(curso)
    def getCurso(self):
        return self.__curso
        