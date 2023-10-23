from Pessoa import Pessoa
from Aluno import Aluno
from Professor import Professor
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

if __name__ == '__main__':

    
    # Pessoa 1 (Aluno Graduação):
    pa1 = AlunoGraduacao()
    pa1.setNome("Vítor")
    pa1.setMatricula(1)
    pa1.setNota1(6.8)
    pa1.setNota2(5)
    pa1.setAprovacao(pa1.verificar_aprovacao())

    # Pessoa 2 (Aluno Ensino Médio):
    pa2 = AlunoEnsinoMedio()
    pa2.setNome("Lucas")

    # Pessoa 3 (Aluno Graduação):
    pa3 = AlunoGraduacao()
    pa3.setNome("Camilo")

    # Pessoa 4 (Aluno Ensino Médio):
    pa4 = AlunoEnsinoMedio()
    pa4.setNome("Otavio")

    # Pessoa 5 (Professor):
    pp = Professor()
    pp.setNome("Gustavo")
    pp.setTitulacaoMaxima("Mestre")



    ##############

    print("Aluno 1:")
    print(f"{pa1.getNome()} foi {pa1.getAprovacao()} com media {pa1.getMedia()}")

    print(pa1.__str__())

    print(pp.__str__())
