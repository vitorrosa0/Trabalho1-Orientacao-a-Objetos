from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self):
        #super().__init__(id, nome, cpf, dataNascimento, email, endereco, telefone, identidade)
        self.__matricula = ""
        self.__titulacaoMaxima = 0
        self.__turma = []
        self.__curso = []


    def setMatricula(self,matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula
    

    def setTitulocaoMaxima(self,titulacaoMaxima):
        self.__titulacaoMaxima = titulacaoMaxima
    def getTitulocaoMaxima(self):
        return self.__titulacaoMaxima
    

    def setTurma(self, turma):
        self.__turma = turma
    def addTurma(self, turma):
        self.__turma.append(turma)
    def removeTurma(self, turma):
        self.__turma.remove(turma)
    def getTurma(self):
        return self.__turma
    

    def setCurso(self, curso):
        self.__curso = curso
    def addCurso(self, curso):
        self.__curso.append(curso)
    def removeCurso(self, curso):
        self.__curso.remove(curso)
    def getCurso(self):
        return self.__curso
    

    def __str__(self):
        return f'**** ID: {self.getId()}, Nome: {self.getNome()}, CPF: {self.getCpf()}, Data de Nascimento: {self.getDataNascimento()}, Email: {self.getEmail()}, Endereço: {self.getEndereco()}, Telefone: {self.getTelefone()}, Identidade: {self.getIdentidade()}, Matricula: {self.getMatricula()}, Titulação máxima: {self.getTitulocaoMaxima()}'