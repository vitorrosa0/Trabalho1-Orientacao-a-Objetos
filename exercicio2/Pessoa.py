class Pessoa():

    def __init__(self):
        self.__nome = " "



    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
 
    

    def __str__(self):

        return f"**** Nome: {self.getNome()}"