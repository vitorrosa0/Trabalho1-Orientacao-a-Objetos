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
    dependente1.setNome("Lucas")
    dependente1.setFuncionario(funcionario1)
    dependente1.setDataNascimento(datetime.strptime('15/10/2000', '%d/%m/%Y'))

    dependente2 = Dependente()
    dependente2.setNome("Vítor")
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

    print("Informações do Funcionário 1")
    print(f"Nome: {funcionario1.getNome()}")
    print(f"Cargo: {funcionario1.getCargo().getFuncionario()}")

    salario = funcionario1.calcularSalario(2023, 10)
    print(f"Salário do funcionário: R${salario:.2f}")

    print()
    funcionario1.exibirDependentes()

    print("Ocorrências:")
    for ocorrencia in funcionario1.getOcorrencia():
        print(f"Data da Ocorrência: {ocorrencia.getDataOcorrencia().strftime('%d/%m/%Y')}")
        print(f"Valor de Acréscimo: R${ocorrencia.getValorAcrescimo():.2f}")
        print(f"Valor de Desconto: R${ocorrencia.getValorDesconto():.2f}")
        print(f"Descrição da Ocorrência: {ocorrencia.getDescricaoOcorrencia()}")
        print("")

if __name__ == "__main__":
    main()