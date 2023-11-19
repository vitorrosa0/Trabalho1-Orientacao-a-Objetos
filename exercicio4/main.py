from Cliente import Cliente
from Carro import Carro
from Moto import Moto
from Veiculo import Veiculo

if __name__ == '__main__':

    cliente1 = Cliente()
    cliente1.setNome("vítor")
    cliente2 = Cliente()
    cliente2.setNome("Lucas")

    carro1 = Carro()
    carro1.setModelo("Celta")
    carro1.setPlaca("ABC123")
    carro1.setValor(100.0)
    
    carro2 = Carro()
    carro2.setModelo("Uno")
    carro2.setPlaca("XYZ123")
    carro2.setValor(80.0)

    moto1 = Moto()
    moto1.setPlaca("MOT123")
    moto1.setValor(40.0)

    moto2 = Moto()
    moto2.setPlaca("MOT234")
    moto2.setValor(50.0)

    print(carro1.alugar(cliente1,10))
    print(carro1.alugar(cliente1,10))
    print(carro1.devolver())
    print(carro2.alugar(cliente2,15))
    print()
    carro1.listarHistorico()
    
    
    
