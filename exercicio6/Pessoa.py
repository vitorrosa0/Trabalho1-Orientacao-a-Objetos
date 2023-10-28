class Pessoa:

    def __init__(self):
        self.__sexo = ""
        self.__peso = 0.0
        self.__altura = 0.0

    def calcularImc(self):

        imc = self.__peso/(self.__altura**2)
        n = ""

        if self.__sexo == "Masculino":
            if imc < 20.7:
                n ="Abaixo do peso"
            if 20.7 <= imc < 26.4:
                n =("Peso normal")
            if 26.4 <= imc < 27.8:
                n =("Marginalmente acima do peso")
            if 27.8 <= imc < 31.1:
                n =("Acima do peso ideal")               
            if imc >= 32.3:
                n =("Obeso")
                
        else:
            if imc < 19.1:
                n =("Abaixo do peso")
            if 19.1 <= imc < 25.8:
                n =("Peso normal")
            if 25.8 <= imc < 27.3:
                n =("Marginalmente acima do peso")
            if 27.3 <= imc < 32.3:
                n =("Acima do peso ideal")
            else:
                n =("Obeso")

        return f"IMC: {imc:.2f}, {n}"
    
    def setSexo(self,sexo):
        self.__sexo = sexo
    def getSexo(self):
        return self.__sexo 
    
    
    def setPeso(self,peso):
        self.__peso = peso
    def getPeso(self):
        return self.__peso
    
    
    def setAltura(self,altura):
        self.__altura = altura
    def getAltura(self):
        return self.__altura  