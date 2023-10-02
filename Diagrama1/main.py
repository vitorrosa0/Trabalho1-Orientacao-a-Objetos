from datetime import datetime, date, time

from empresa import Empresa
from itemNota import ItemNota
from nota import Nota
from participante import Participante
from produto import Produto

if __name__ == '__main__':

    # Empresa 1:
    e1 = Empresa()
    e1.setId(1)
    e1.setCodigo(10)
    e1.setRazaoSocial('Vida')
    e1.setEndereco('Rua X')
    e1.setCnpj('39183')

    # Empresa 2:
    e2 = Empresa()
    e2.setId(2)
    e2.setCodigo(20)
    e2.setRazaoSocial('Morte')
    e2.setEndereco('Rua Y')
    e2.setCnpj('444444')

    print("Empresa 1:")
    print(e1.__str__())


    # Nota 1:
    n1 = Nota()
    n1.setId(1)
    n1.setData(datetime.strptime('14/01/2003', '%d/%m/%Y'))
    n1.setNumero(20)

    # Nota 2:
    n2 = Nota()
    n2.setId(2)
    n2.setData(datetime.strptime('22/01/2003', '%d/%m/%Y'))
    n2.setNumero(20)

    # Nota 3:
    n3 = Nota()
    n3.setId(3)
    n3.setData(datetime.strptime('04/04/2003', '%d/%m/%Y'))
    n3.setNumero(20)

    # Nota 4:
    n4 = Nota()
    n4.setId(4)
    n4.setData(datetime.strptime('01/09/2002', '%d/%m/%Y'))
    n4.setNumero(21)

    print()
    print("Nota 1:")
    print(n1.__str__())

    # Adionando as notas à empresa relacionada:
    e1.addNota(n1)
    e1.addNota(n2)
    e2.addNota(n3)
    e2.addNota(n4)

    print()
    print("Lista de notas na Empresa 1:")
    for n in e1.getNota():
        print(n)

    # Item Nota 1:
    iN1 = ItemNota()
    iN1.setId(1)
    iN1.setVrUnitario(1.5)
    iN1.setQuantidade(2)
    print(iN1.__str__())

    # Item Nota 2:
    iN2 = ItemNota()
    iN2.setId(2)
    iN2.setVrUnitario(4.0)
    iN2.setQuantidade(1)

    # Item Nota 3:
    iN3 = ItemNota()
    iN3.setId(3)
    iN3.setVrUnitario(0.5)
    iN3.setQuantidade(2)

    # Item Nota 4:
    iN4 = ItemNota()
    iN4.setId(4)
    iN4.setVrUnitario(10.0)
    iN4.setQuantidade(2)


    print()
    print("Item Nota1:")
    print(iN1.__str__())

    # Produto 1:
    pr1 = Produto()
    pr1.setId(1)
    pr1.setCodigo('A1')
    pr1.setDescricao('maçã')

    # Produto 2:
    pr2 = Produto()
    pr2.setId(2)
    pr2.setCodigo('B1')
    pr2.setDescricao('banana')

    # Produto 3:
    pr3 = Produto()
    pr3.setId(3)
    pr3.setCodigo('C1')
    pr3.setDescricao('Carambola')

    # Produto 4:
    pr4 = Produto()
    pr4.setId(4)
    pr4.setCodigo('D1')
    pr4.setDescricao('Damasco')

    print()
    print("Produto:")
    print(pr1.__str__())

    pr1.addItemNota(iN1)
    pr2.addItemNota(iN2)
    pr3.addItemNota(iN3)
    pr4.addItemNota(iN4)

    print()
    print("Lista de itens nota nos Produtos:\n")
    print("Lista de itens nota no Produto 1:")
    for pr in pr1.getItemNota():
        print(pr)

    print("Lista de itens nota no Produto 2:")
    for pr in pr2.getItemNota():
        print(pr)
    print("Lista de itens nota no Produto 3:")
    for pr in pr3.getItemNota():
        print(pr)
    print("Lista de itens nota no Produto 4:")
    for pr in pr4.getItemNota():
        print(pr)

    # Participante 1:
    p1 = Participante()
    p1.setId(1)
    p1.setCodigo(10)
    p1.setRazaoSocial('Vida')
    p1.setCnpj('093629306429')

    # Participante 2:
    p2 = Participante()
    p2.setId(2)
    p2.setCodigo(20)
    p2.setRazaoSocial('Morte')
    p2.setCnpj('983472893')

    # Participante 3:
    p3 = Participante()
    p3.setId(3)
    p3.setCodigo(30)
    p3.setRazaoSocial('Oi')
    p3.setCnpj('39427983034')

    # Participante 4:
    p4 = Participante()
    p4.setId(4)
    p4.setCodigo(40)
    p4.setRazaoSocial('Tchau')
    p4.setCnpj('32857298572')

    print()
    print("Participante:")
    print(p1.__str__())

    p1.addNota(n1)
    p2.addNota(n2)
    p3.addNota(n3)
    p4.addNota(n4)

    print()
    print("Lista de notas dos Participantes:\n")
    print("Lista de notas do Participante 1:")
    for p in p1.getNota():
        print(p)
    print("Lista de nota do Participante 2:")
    for p in p2.getNota():
        print(p)
    print("Lista de nota do Participante3:")
    for p in p3.getNota():
        print(p)
    print("Lista de nota do Participante4:")
    for p in p4.getNota():
        print(p)

    #Notas da empresa1:
    n1.addItemNota(iN1)
    n2.addItemNota(iN2)
    #Notas da empresa2:
    n3.addItemNota(iN3)
    n4.addItemNota(iN4)


    n_e1 = e1.getNota()
    n_e2 = e2.getNota()

    print()
    print("Notas da empresa: \n")

    print("Notas da empresa 1: ")
    for n in n_e1:
        print(
            n.__str__()
        )
    print("\n")

    print("Notas da empresa 2: ")
    for n in n_e2:
        print(
            n.__str__()
        )
    print("\n")