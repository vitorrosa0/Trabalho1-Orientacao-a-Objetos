class Cargo:

    def __init__(self):
        
        self.__salarioBruto = 0.0
        self.__funcionario = []

    def setSalarioBruto (self, salarioBruto):
        self.__salarioBruto = salarioBruto
    def getSalarioBruto(self):
        return self.__salarioBruto
    
    def setFuncionario(self, funcionario):
        self.__funcionario = funcionario
    def addFuncionario(self, funcionario):
        self.__funcionario.append(funcionario)
    def removeFuncionario(self, funcionario):
        self.__funcionario.remove(funcionario)
    def getFuncionario(self):
        return self.__funcionario