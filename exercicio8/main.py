<<<<<<< HEAD
from Cidade import Cidade
from Departamento import Departamento
from Empresa import Empresa
from Escolaridade import Escolaridade
from Estado import Estado
from Filial import Filial
from Funcionario import Funcionario
from Grupo import Grupo
from Pais import Pais

if __name__ == '__main__':
    # 1. Qual a escolaridade do presidente de um grupo?
    grupo1 = Grupo(presidente=Funcionario("Presidente1", Escolaridade("Doutorado"), None, None))
    escolaridade_presidente = grupo1.presidente.escolaridade.nivel
    print("Escolaridade do presidente do grupo: ", escolaridade_presidente)

    # 2. Qual o país de alocação de um funcionário?
    pais1 = Pais("Brasil")
    estado1 = Estado("São Paulo", pais1)
    cidade1 = Cidade("São Paulo", estado1)
    filial1 = Filial("Filial1", cidade1)
    funcionario1 = Funcionario("Funcionario1", None, filial1, None)
    pais_de_alocacao = funcionario1.filial.cidade.estado.pais.nome
    print("País de alocação do funcionário: ", pais_de_alocacao)

    # 3. Qual o estado da filial que um funcionário coordena?
    pais2 = Pais("EUA")
    estado2 = Estado("Califórnia", pais2)
    cidade2 = Cidade("Los Angeles", estado2)
    filial2 = Filial("Filial2", cidade2)
    funcionario2 = Funcionario("Funcionario2", None, filial2, None)
    estado_da_filial = funcionario2.filial.cidade.estado.nome
    print("Estado da filial que o funcionário coordena: ", estado_da_filial)

    # 4. Qual a escolaridade de um chefe de um departamento?
    departamento1 = Departamento("Departamento1", Funcionario("ChefeDepartamento1", Escolaridade("Mestrado"), None, None))
    escolaridade_chefe_departamento = departamento1.chefe.escolaridade.nivel
    print("Escolaridade do chefe de departamento: ", escolaridade_chefe_departamento)

    # 5. Qual o nome do diretor da empresa de uma filial?
    pais3 = Pais("Canadá")
    estado3 = Estado("Ontário", pais3)
    cidade3 = Cidade("Toronto", estado3)
    filial3 = Filial("Filial3", cidade3)
    empresa3 = Empresa("Empresa3", Funcionario("DiretorEmpresa3", None, None, None))
    filial3.empresa = empresa3
    nome_diretor_empresa = filial3.empresa.diretor.nome
    print("Nome do diretor da empresa da filial: ", nome_diretor_empresa)
=======
class Grupo:
    def __init__(self, presidente):
        self.presidente = presidente

class Pais:
    def __init__(self, nome):
        self.nome = nome

class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

class Cidade:
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

class Filial:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade

class Funcionario:
    def __init__(self, nome, escolaridade, filial, chefe_de_departamento):
        self.nome = nome
        self.escolaridade = escolaridade
        self.filial = filial
        self.chefe_de_departamento = chefe_de_departamento

class Departamento:
    def __init__(self, nome, chefe):
        self.nome = nome
        self.chefe = chefe

class Empresa:
    def __init__(self, nome, diretor):
        self.nome = nome
        self.diretor = diretor

class Escolaridade:
    def __init__(self, nivel):
        self.nivel = nivel

# 1. Qual a escolaridade do presidente de um grupo?
grupo1 = Grupo(presidente=Funcionario("Presidente1", Escolaridade("Doutorado"), None, None))
escolaridade_presidente = grupo1.presidente.escolaridade.nivel
print("Escolaridade do presidente do grupo: ", escolaridade_presidente)

# 2. Qual o país de alocação de um funcionário?
pais1 = Pais("Brasil")
estado1 = Estado("São Paulo", pais1)
cidade1 = Cidade("São Paulo", estado1)
filial1 = Filial("Filial1", cidade1)
funcionario1 = Funcionario("Funcionario1", None, filial1, None)
pais_de_alocacao = funcionario1.filial.cidade.estado.pais.nome
print("País de alocação do funcionário: ", pais_de_alocacao)

# 3. Qual o estado da filial que um funcionário coordena?
pais2 = Pais("EUA")
estado2 = Estado("Califórnia", pais2)
cidade2 = Cidade("Los Angeles", estado2)
filial2 = Filial("Filial2", cidade2)
funcionario2 = Funcionario("Funcionario2", None, filial2, None)
estado_da_filial = funcionario2.filial.cidade.estado.nome
print("Estado da filial que o funcionário coordena: ", estado_da_filial)

# 4. Qual a escolaridade de um chefe de um departamento?
departamento1 = Departamento("Departamento1", Funcionario("ChefeDepartamento1", Escolaridade("Mestrado"), None, None))
escolaridade_chefe_departamento = departamento1.chefe.escolaridade.nivel
print("Escolaridade do chefe de departamento: ", escolaridade_chefe_departamento)

# 5. Qual o nome do diretor da empresa de uma filial?
pais3 = Pais("Canadá")
estado3 = Estado("Ontário", pais3)
cidade3 = Cidade("Toronto", estado3)
filial3 = Filial("Filial3", cidade3)
empresa3 = Empresa("Empresa3", Funcionario("DiretorEmpresa3", None, None, None))
filial3.empresa = empresa3
nome_diretor_empresa = filial3.empresa.diretor.nome
print("Nome do diretor da empresa da filial: ", nome_diretor_empresa)
>>>>>>> 614eec8e9a842ce5b1a67a242106d593b76333af
