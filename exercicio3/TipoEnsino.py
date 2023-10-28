class TipoEnsino:

    def __init__(self):
        self.__curso = []

    def setCurso(self, curso):
        self.__curso = curso
    def addCurso(self, curso):
        self.__curso.append(curso)
    def removeCurso(self, curso):
        self.__curso.remove(curso)
    def getCurso(self):
        return self.__curso