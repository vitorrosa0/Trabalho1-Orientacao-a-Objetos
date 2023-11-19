from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self):
        super().__init__()
        self.__modelo = ""

        
    def calcularAluguel(self, dias):
        dias = dias
        return f"O Valor do aluguel é de R${(self.getValor() * dias)}"

    def setModelo(self,modelo):
        self.__modelo = modelo
    def getModelo(self):
        return self.__modelo

