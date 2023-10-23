from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self):
        self.__matricula = 0
        self.__nota1 = 0.0
        self.__nota2 = 0.0
        self.__media = 0.0
        self.__aprovacao = ""
    
    
    def setMatricula(self, matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula


    def setNota1(self, nota1):
        self.__nota1 = nota1
    def getNota1(self):
        return self.__nota1
    

    def setNota2(self, nota2):
        self.__nota2 = nota2
    def getNota2(self):
        return self.__nota2

    
    def getMedia(self):
        self.__media = float(self.__nota1 + self.__nota2) / 2
        return self.__media


    def setAprovacao(self, aprovacao):
        self.__aprovacao = aprovacao
    def getAprovacao(self):
        return self.__aprovacao
    

    def __str__(self):
        return f"**** Nome: {self.getNome()}, Matricula: {self.getMatricula()}, Aprovação: {self.getAprovacao()}"