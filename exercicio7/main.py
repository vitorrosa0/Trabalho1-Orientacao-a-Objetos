from Funcionarios import Funcionario

f = Funcionario()
f.setNome("Lucas")
f.setSalarioBruto(1000)
f.setTotalAcrescimos(500)
f.setTotalDescontos(200)

print(f"Funcionário: {f.getNome()}")
print(f"Salário: R$ {f.calcularSalarioLiquido()},00")