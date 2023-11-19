from Cliente import Cliente

class Veiculo:

    def __init__(self):

        self.__placa = ""
        self.__valor = 0.0
        self.__cliente = Cliente()
        self.__alugado = bool
        self.__historico = []

    def setPlaca(self,placa):
        self.__placa = placa
    def getPlaca(self):
        return self.__placa 
    
    def setValor(self,valor):
        self.__valor = valor
    def getValor(self):
        return self.__valor
    
    def setCliente(self,cliente):
        self.__cliente = cliente
    def getCliente(self):
        return self.__cliente 

    def setAlugado(self,alugado):
        self.__alugado = alugado
    def getAlugado(self):
        return self.__alugado 

    def setHistorico(self, historico):
        self.__historico = historico
    def addHistorico(self, historico):
        self.__historico.append(historico)
    def removeHistorico(self, historico):
        self.__historico.remove(historico)
    def getHistorico(self):
        return self.__historico
        

    def alugar(self, cliente, dias):
        if not self.__alugado:
            custo_aluguel = self.calcularAluguel(dias)
            self.__alugado = True
            self.__historico.append(f"{cliente} alugou o veículo por {dias} dias, custando R${custo_aluguel}")
            return f"Aluguel confirmado para o veículo de placa {self.__placa}"
        else:
            return "Veículo já está alugado"
            
    def devolver(self):
        if self.__alugado:
            self.__alugado = False
            self.__historico.append(f"Veículo de placa {self.__placa} foi devolvido")
            return f"Devolução realizada para o veículo de placa {self.__placa}"
        else:
            return "Veículo não está alugado"
    
    def listarHistorico(self):
        if not self.__historico:
            print("Nenhum registro no histórico.")
        else:
            print(f"Histórico do veículo de placa {self.__placa}:")
            for registro in self.__historico:
                print(f"{registro.getCliente().getNome()} {registro}")