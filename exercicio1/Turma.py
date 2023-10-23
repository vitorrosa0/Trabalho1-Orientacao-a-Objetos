from Professor import Professor
from Disciplina import Disciplina
from Curso import Curso
from Pessoa import Pessoa


class Turma:

    def __init__(self):
        
        self.__id = ""
        self.__aluno = []
        self.__professor = Professor()
        self.__disciplina = Disciplina()
        self.__curso = Curso()

    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id


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
    def getProfessor(self):
        return self.__professor
    
    
    
    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina
    def getDisciplina(self):
        return self.__disciplina
    
    
    def setCurso(self, curso):
        self.__curso = curso
    def getCurso(self):
        return self.__curso
    
    def aluno_na_turma(self, aluno):
        return aluno in self.__aluno


    def __str__(self):
        alunos_str = ', '.join([aluno.getNome() for aluno in self.getAluno()])
        return f"**** Turma: {self.getId()}, Alunos: {alunos_str}, Professor: {self.getProfessor().getNome()}, Disciplina: {self.getDisciplina().getNome()}, Curso: {self.getCurso().getNome()}"