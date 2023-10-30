from datetime import datetime, date, time
from Pessoa import Pessoa
from Cargo import Cargo
from Funcionario import Funcionario
from Dependente import Dependente
from Ocorrencia import Ocorrencia

def main():
    cargo1 = Cargo()
    cargo1.setFuncionario("Gerente")
    cargo1.setSalarioBruto( 5000)

    funcionario1 = Funcionario()
    funcionario1.setNome("João")
    funcionario1.setCargo(cargo1)

    dependente1 = Dependente()
    dependente1.setFuncionario(funcionario1)
    dependente1.setDataNascimento(datetime.strptime('15/10/2000', '%d/%m/%Y'))

    dependente2 = Dependente()
    dependente2.setFuncionario(funcionario1)
    dependente2.setDataNascimento(datetime.strptime('20/02/2015', '%d/%m/%Y'))

    funcionario1.addDependente(dependente1)
    funcionario1.addDependente(dependente2)

    ocorrencia1 = Ocorrencia()
    ocorrencia1.setDataOcorrencia(datetime.strptime('30/10/2023', '%d/%m/%Y'))
    ocorrencia1.setValorAcrescimo(100)
    ocorrencia1.setValorDesconto(50)
    ocorrencia1.setDescricaoOcorrencia("Bônus de aniversário")
    ocorrencia1.setFuncionario(funcionario1)

    funcionario1.addOcorrencia(ocorrencia1)

    salario = funcionario1.calcularSalario(2023, 10)
    print(f"Salário do funcionário: R${salario:.2f}")

    funcionario1.exibirDependentes()

if __name__ == "__main__":
    main()