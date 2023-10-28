class Estado:

    def __init__(self):
        self.__cidade = []


    def setCidade(self, cidade):
        self.__cidade = cidade
    def addCidade(self, cidade):
        self.__cidade.append(cidade)
    def removeCidade(self, cidade):
        self.__cidade.remove(cidade)
    def getCidade(self):
        return self.__cidade