from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self):
        self.__modelo = ""

        
    def calcularAluguel(self, dias):
        dias = self.getDias()
        return f"O Valor do aluguel é de R${(self.getValor() * dias)}"

    def setModelo(self,modelo):
        self.__modelo = modelo
    def getModelo(self):
        return self.__modelo

