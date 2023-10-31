from Pessoa import Pessoa
from Cargo import Cargo
from datetime import datetime, date


class Funcionario(Pessoa):

    def __init__(self):
        self.__cargo = Cargo()
        self.__ocorrencia = []
        self.__dependentes = []

    def setCargo (self, cargo):
        self.__cargo = cargo
    def getCargo(self):
        return self.__cargo
    
    def setOcorrencia(self, ocorrencia):
        self.__ocorrencia = ocorrencia
    def addOcorrencia(self, ocorrencia):
        self.__ocorrencia.append(ocorrencia)
    def removeOcorrencia(self, ocorrencia):
        self.__ocorrencia.remove(ocorrencia)
    def getOcorrencia(self):
        return self.__ocorrencia
    
    def setDependentes(self, dependentes):
        self.__dependentes = dependentes
    def addDependente(self, dependente):
        self.__dependentes.append(dependente)
    def removeDependente(self, dependente):
        self.__dependentes.remove(dependente)
    def getDependentes(self):
        return self.__dependentes



    def calcularSalario(self, ano, mes):
        salario_bruto = self.__cargo.getSalarioBruto()
        acrescimos = 0
        descontos = 0

        # Calcular idade dos dependentes
        data_referencia = datetime(ano, mes, 1).date()
        for dependente in self.__dependentes:
            data_nascimento_dependente = dependente.getDataNascimento()
            idade_dependente = (data_referencia.year - data_nascimento_dependente.year)- ((data_referencia.month, data_referencia.day) < (data_nascimento_dependente.month, data_nascimento_dependente.day))
            if idade_dependente < 18:
                acrescimos += 100

        # Calcular acréscimos e descontos das ocorrências
        for ocorrencia in self.__ocorrencia:
            data_ocorrencia = ocorrencia.getDataOcorrencia()
            if data_ocorrencia.year == ano and data_ocorrencia.month == mes:
                acrescimos += ocorrencia.getValorAcrescimo()
                descontos += ocorrencia.getValorDesconto()

        salario_liquido = salario_bruto + acrescimos - descontos

        return salario_liquido

    def exibirDependentes(self):
        print("Dependentes do Funcionário", self.getNome())
        data_referencia = datetime.now().date()
        
        for dependente in self.__dependentes:
            nome_dependente = dependente.getNome()
            data_nascimento = dependente.getDataNascimento()
            idade_dependente = (data_referencia.year - data_nascimento.year) - ((data_referencia.month, data_referencia.day) < (data_nascimento.month, data_nascimento.day))            
            
            proximo_aniversario = datetime(data_referencia.year, data_nascimento.month, data_nascimento.day).date()
            if proximo_aniversario < data_referencia:
                proximo_aniversario = datetime(data_referencia.year + 1, data_nascimento.month, data_nascimento.day).date()

            dias_faltantes = (proximo_aniversario - data_referencia).days
            dia_semana = proximo_aniversario.strftime('%A')

            print(f"Nome: {nome_dependente}")
            print(f"Data de Nascimento: {data_nascimento}")
            print(f"Próximo Aniversário: {proximo_aniversario.strftime('%d/%m/%Y')}")
            print(f"Dias Restantes: {dias_faltantes} dias")
            print(f"Dia da Semana do Próximo Aniversário: {dia_semana}\n")
