from Veiculo import Veiculo

class Moto(Veiculo):

    
    def calcularAluguel(self, dias):
        dias = self.getDias()
        return f"O Valor do aluguel é de R${(self.getValor() * dias)}"