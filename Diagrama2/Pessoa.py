from datetime import date, datetime, time

class Pessoa():

    def __init__(self):
        self.__id = 0
        self.__nome = " "
        self.__cpf = " "
        self.__dataNascimento = None
        self.__email = " "
        self.__endereco = " "
        self.__telefone = " "
        self.__identidade = " "

    
    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id


    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
 
    
    def setCpf(self, cpf):
        self.__cpf = cpf
    def getCpf(self):
        return self.__cpf
 
    
    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
    def getDataNascimento(self):
        return self.__dataNascimento


    def setEmail(self, email):
        self.__email = email
    def getEmail(self):
        return self.__email

    
    def setEndereco(self, endereco):
        self.__endereco = endereco
    def getEndereco(self):
        return self.__endereco
 
    
    def setTelefone(self, telefone):
        self.__telefone = telefone
    def getTelefone(self):
        return self.__telefone
 
    
    def setIdentidade(self, identidade):
        self.__identidade = identidade
    def getIdentidade(self):
        return self.__identidade
    

    def __str__(self):

        return f"**** ID: {self.getId()}, Nome: {self.getNome()}, CPF: {self.getCpf()}, Data de Nascimento: {self.getDataNascimento()}, Email: {self.getEmail()}, Endereço: {self.getEndereco()}, Telefone: {self.getTelefone()}, Identidade: {self.getIdentidade()}"
        
    
