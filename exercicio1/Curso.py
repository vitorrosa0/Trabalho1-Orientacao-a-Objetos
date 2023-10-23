class Curso():
    def __init__(self):
        self.__aluno = []
        self.__turma = []
        self.__professor = []
        self.__disciplina = []


    def setAluno(self, aluno):
        self.__aluno = aluno
    def addAluno(self, aluno):
        self.__aluno.append(aluno)
    def removeAluno(self, aluno):
        self.__aluno.remove(aluno)
    def getAluno(self):
        return self.__aluno
    
    def setProfessor(self, professor):
        self.__professor = professor
    def addProfessor(self, professor):
        self.__professor.append(professor)
    def removeProfessor(self, professor):
        self.__professor.remove(professor)
    def getProfessor(self):
        return self.__professor


    def setTurma(self, turma):
        self.__turma = turma
    def addTurma(self, turma):
        self.__turma.append(turma)
    def removeTurma(self, turma):
        self.__turma.remove(turma)
    def getTurma(self):
        return self.__turma
    
    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina
    def addDisciplina(self, disciplina):
        self.__disciplina.append(disciplina)
    def removeDisciplina(self, disciplina):
        self.__disciplina.remove(disciplina)
    def getDisciplina(self):
        return self.__disciplina
    
    def aluno_no_curso(self, aluno):
        return aluno in self.__aluno
    
    def turma_no_curso(self, turma):
        return turma in self.__turma


    def __str__(self):
        return f"**** Alunos: {self.getAluno()}, Turmas: {self.getTurma()}, Professores: {self.getProfessor()}"