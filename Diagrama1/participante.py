class Participante:

    def __init__(self):
        self.__id = 0
        self.__codigo = 0
        self.__razaoSocial = ""
        self.__cnpj = ""
        self.__nota = []


    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id


    def setCodigo(self, codigo):
        self.__codigo = codigo
    def getCodigo(self):
        return self.__codigo


    def setRazaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial
    def getRazaoSocial(self):
        return self.__razaoSocial


    def setCnpj(self, cnpj):
        self.__cnpj = cnpj
    def getCnpj(self):
        return self.__cnpj


    def setNota(self, nota):
        self.__nota = nota
    def addNota(self, nota):
        self.__nota.append(nota)
    def removeNota(self, nota):
        self.__nota.remove(nota)
    def getNota(self):
        return self.__nota


    def __str__(self):
        notas_str = ', '.join([str(nota) for nota in self.getNota()])
        return f'**** ID Participante: {self.getId()}, Código: {self.getCodigo()}, RazãoSocial: {self.getRazaoSocial()}, CNPJ: {self.getCnpj()}, Notas: [{notas_str}]'