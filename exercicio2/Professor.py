from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self):
        self.__titulacaoMaxima = ""
    
    
    def setTitulacaoMaxima(self, titulacaoMaxima):
        self.__titulacaoMaxima = titulacaoMaxima
    def getTitulacaoMaxima(self):
        return self.__titulacaoMaxima
    

    def __str__(self):
        return f"**** Nome: {self.getNome()}, Titulação Máxima: {self.getTitulacaoMaxima()}"