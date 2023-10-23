from Aluno import Aluno
from Professor import Professor
from Pessoa import Pessoa
from Turma import Turma
from Disciplina import Disciplina
from Curso import Curso

if __name__ == '__main__':

    
    # Pessoa 1 (Aluno):
    pa1 = Aluno()
    pa1.setNome("Vítor")

    # Pessoa 2 (Aluno):
    pa2 = Aluno()
    pa2.setNome("Lucas")

    # Pessoa 3 (Aluno):
    pa3 = Aluno()
    pa3.setNome("Camilo")

    # Pessoa 4 (Aluno):
    pa4 = Aluno()
    pa4.setNome("Otavio")

    # Pessoa 5 (Professor):
    pp1 = Professor()
    pp1.setNome("Gustavo")

    # Pessoa 6 (Professor):
    pp2 = Professor()
    pp2.setNome("Lennon")

    # Pessoa 6 (Professor):
    pp3 = Professor()
    pp3.setNome("Pedro")


    # Adicionando Alunos à Turma 1:
    t1 = Turma()
    t1.setId(1)
    t1.addAluno(pa1)
    t1.addAluno(pa2)
    t1.addAluno(pa3)
    t1.addAluno(pa4)


    # Adicionando Alunos à Turma 2:
    t2 = Turma()
    t2.setId(2)
    t2.addAluno(pa1)
    t2.addAluno(pa3)


    # Adicionando Alunos à Turma 3:
    t3 = Turma()
    t3.setId(3)
    t3.addAluno(pa2)
    t3.addAluno(pa4)


    # Adicionando Alunos a um Curso:
    c = Curso()
    c.addAluno(pa1)
    c.addAluno(pa2)
    c.addAluno(pa3)
    c.addAluno(pa4)

    
    # Adicionando Professores a um Curso:
    c.addProfessor(pp1)
    c.addProfessor(pp2)
    c.addProfessor(pp3)
    
    
    # Disciplina 1:
    d1 = Disciplina()
    d1.setNome("Orientação de Objetos")

    # Adicionando Turma à Disciplina 1:
    d1.addTurma(t1)
    d1.addTurma(t2)
    d1.addTurma(t3)

    # Disciplina 2:
    d2 = Disciplina()
    d2.setNome("Análise de Sistemas")

    # Adicionando Turma à Disciplina 2:
    d2.addTurma(t1)
    d2.addTurma(t3)

    # Disciplina 3:
    d3 = Disciplina()
    d3.setNome("Arquitetura de Computadores")

    # Adicionando Turma à Disciplina 3:
    d3.addTurma(t2)


    # Adicionando Disciplina a um Curso:
    c.addDisciplina(d1)
    c.addDisciplina(d2)
    c.addDisciplina(d3)


    # Adicionando Turmas a um Curso:
    c.addTurma(t1)
    c.addTurma(t2)
    c.addTurma(t3)


    # Remover aluno da turma:
    t3.removeAluno(pa2)

    # Remover turma do curso:
    c.removeTurma(t3)

    # Remover aluno do curso:
    c.removeAluno(pa1)

    ########## Print ###########

    # print("Aluno 1: ")
    # print(pa1.__str__())
    # print("Aluno 2: ")
    # print(pa2.__str__())
    # print("Aluno 3: ")
    # print(pa3.__str__())
    # print("Aluno 4: ")
    # print(pa4.__str__())


    print("Professor da turma 1: ")
    print(pp1.getNome())

    alunos = t1.getAluno()
    alunos_nomes = [aluno.getNome() for aluno in alunos]
    alunos_str = ', '.join(alunos_nomes)
    print("Alunos da turma 1:")
    print(alunos_str)

    professores = c.getProfessor()
    professores_nomes = [professor.getNome() for professor in professores]
    professores_str = ', '.join(professores_nomes)
    print("Professores que lecionam em alguma truma de um curso:")
    print(professores_str)

    alunos = c.getAluno()
    alunos_nomes = [aluno.getNome() for aluno in alunos]
    alunos_str = ', '.join(alunos_nomes)
    print("Alunos do Curso:")
    print(alunos_str)

    disciplinas = c.getDisciplina()
    disciplinas_nomes = [disciplina.getNome() for disciplina in disciplinas]
    disciplinas_str = ', '.join(disciplinas_nomes)
    print("Disciplinas em um curso:")
    print(disciplinas_str)

    if t3.aluno_na_turma(pa1):
        print(f"{pa1.getNome()} está na Turma {t3.getId()}.")
    else:
        print(f"{pa1.getNome()} não está na Turma {t3.getId()}.")

    if c.aluno_no_curso(pa4):
        print(f"{pa4.getNome()} está no Curso.")
    else:
        print(f"{pa4.getNome()} não está no Curso.")

    if c.turma_no_curso(t2):
        print(f"Turma {t2.getId()} está no Curso.")
    else:
        print(f"Turma {t2.getId()} não está no Curso.")


    

