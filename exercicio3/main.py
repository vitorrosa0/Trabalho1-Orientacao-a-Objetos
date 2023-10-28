from Professor import Professor
from Aluno import Aluno
from Curso import Curso
from Escola import Escola
from Cidade import Cidade
from Pessoa import Pessoa
from Estado import Estado

if __name__ == '__main__':

    pp1 = Professor()
    pp1.setEscolaridade("Ensino Superior")
    pp1.setEscola("UniAcademia")
    pp1.setCurso("Engenharia de Software")
    pp1.setCidade("Juiz de Fora")

    pp2 = Professor()
    pp2.setEscolaridade("Mestrado")
    pp2.setEscola("UniAcademia")
    pp2.setCurso("Engenharia de Software")
    pp2.setCidade("Juiz de Fora")

    pp3 = Professor()
    pp3.setEscolaridade("Doutorado")
    pp3.setEscola("UniAcademia")
    pp3.setCurso("Engenharia de Software")
    pp3.setCidade("Juiz de Fora")

    pa1 = Aluno()
    pa1.setEscolaridade("Ensino Superior incompleto")
    pa1.setCidade("Juiz de Fora")
    pa1.setCurso("Engenharia de Software")


    c1 = Curso()
    c1.setTipoEnsino("Ensino Superior")
    c1.setEscola("UniAcademia")

    c1.addProfessor(pp1)
    c1.addProfessor(pp2)
    c1.addProfessor(pp3)

    c1.addAluno(pa1)

    e1 = Escola()
    e1.addCurso(c1)
    e1.addProfessor(pp1)
    e1.addProfessor(pp2)
    e1.addProfessor(pp3)

    cd1 = Cidade()
    cd1.setEstado("Minas Gerais")
    cd1.addPessoa(pa1)
    cd1.addPessoa(pp1)
    cd1.addPessoa(pp2)
    cd1.addPessoa(pp3)
    
    es1 = Estado()
    es1.addCidade(cd1)











    ############
    print(f"a) {pp1.getEscolaridade()}")
    print(f"b) {pp2.getEscolaridade()}")
    print(f"c) {pp3.getEscolaridade()}")
    #print(f"d) {p.getEstado()}")
    print(f"e) {pp2.getCidade()}")
    #print(f"f) ")
    print(f"g) ")