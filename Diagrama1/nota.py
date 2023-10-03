from empresa import Empresa

from datetime import date, datetime, time
from participante import Participante

class Nota:

    def __init__(self):
        self.__id = 0
        self.__data = None
        self.__numero = 0
        self.__empresa = Empresa()
        self.__participante = Participante()
        self.__itemNota = []


    def setId(self,id):
        self.__id = id
    def getId(self):
        return self.__id 


    def setData(self, data):
        self.__data = data
    def getData(self):
        return self.__data


    def setNumero(self, numero):
        self.__numero = numero
    def getNumero(self):
        return self.__numero


    def setEmpresa(self, empresa):
        self.__empresa = empresa
    def getEmpresa(self):
         return self.__empresa


    def setParticipante(self, participante):
        self.__participante = participante
    def getParticipante(self):
        return self.__participante


    def setItemNota(self, itemNota):
        self.__itemNota = itemNota
    def addItemNota(self, itemNota):
        self.__itemNota.append(itemNota)
    def removeItemNota(self, itemNota):
        self.__itemNota.remove(itemNota)
    def getItemNota(self):
        return self.__itemNota


    def getVrTotal(self):
        total = 0
        for item in self.__itemNota:
            total += item.getVrUnitario() * item.getQuantidade()
        return total



    def __str__(self):
        itemNota_str = ', '.join([str(item) for item in self.getItemNota()])
        return f'**** ID Nota: {self.getId()}, Data: {datetime.strftime(self.getData(), " %d-%m-%Y ")}, Número: {str(self.getNumero())}, VrTotal: R${self.getVrTotal()}, Empresa: {self.getEmpresa().getId()}, Participante: {self.getParticipante().getId()}, Itens de Nota: [{itemNota_str}]'