from Pessoa import Pessoa

if __name__ == '__main__':

    p1 = Pessoa()
    p1.setSexo("Masculino")
    p1.setAltura(1.83)
    p1.setPeso(80.0)

    p2 = Pessoa()
    p2.setSexo("Feminino")
    p2.setAltura(1.63)
    p2.setPeso(54.8)

    print(p1.calcularImc())
    