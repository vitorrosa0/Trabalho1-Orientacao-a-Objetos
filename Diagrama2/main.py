from datetime import datetime
from Aluno import Aluno
from Professor import Professor
from Pessoa import Pessoa
from Situacao import Situacao
from Diario import Diario
from Turma import Turma
from Instituicao import Instituicao
from Disciplina import Disciplina
from Curso import Curso


def principal():

    # Dados da Pessoa 1(Aluno):
    pa1 = Aluno()
    pa1.setId(1)
    pa1.setNome('Vítor')
    pa1.setCpf('899200173938')
    pa1.setDataNascimento(datetime.strptime('04/04/2003', '%d/%m/%Y'))
    pa1.setEmail('email@email.com')
    pa1.setEndereco('Rua C')
    pa1.setTelefone('32156789')
    pa1.setIdentidade('299273892')
    pa1.setMatricula('887739002873')
    pa1.setAnoInicio(2023)
    pa1.setSemestreInicio(1)

    # Dados da Pessoa 2(Aluno):
    pa2 = Aluno()
    pa2.setId(2)
    pa2.setNome('Lucas')
    pa2.setCpf('3284723894')
    pa2.setDataNascimento(datetime.strptime('22/01/2003', '%d/%m/%Y'))
    pa2.setEmail('email@email.com')
    pa2.setEndereco('Rua W')
    pa2.setTelefone('32176545')
    pa2.setIdentidade('5834579875')
    pa2.setMatricula('23857348957')
    pa2.setAnoInicio(2023)
    pa2.setSemestreInicio(1)

    
    # Dados da Situação:
    s = Situacao()
    s.setSituacao('Inscrito')
    s.setAnoSemestre(1)

    # Adicionando os Alunos a uma Situação:
    s.addAluno(pa1)
    s.addAluno(pa2)

    

    # Dados do Diario 1:
    d1 = Diario()
    d1.setV1(8.5)
    d1.setV2(6.9)
    d1.setVS(15.4)
    d1.setVT(7.7)
    d1.setFaltas(2)

    # Dados do Diario 2:
    d2 = Diario()
    d2.setV1(7.0)
    d2.setV2(9.0)
    d2.setVS(16.0)
    d2.setVT(8.0)
    d2.setFaltas(1)
    
    # Adicionando um Diário a um Aluno:
    pa1.addDiario(d1)
    pa2.addDiario(d2)

    
    
    # Dados da Turma 1:
    t1 = Turma()
    t1.setId(75489573)
    t1.setDescricao('A')
    t1.setAno(1)
    t1.setSemestre(2)

    # Dados da Turma 2:
    t2 = Turma()
    t2.setId(49835793)
    t2.setDescricao('B')
    t2.setAno(1)
    t2.setSemestre(2)

    # Dados da Turma 3:
    t3 = Turma()
    t3.setId(438247289)
    t3.setDescricao('C')
    t3.setAno(1)
    t3.setSemestre(2)
    
    

    # Adicionando um Diário a uma Turma:
    t1.addDiario(d1)
    t2.addDiario(d2)

    

    # Dados de Instituição:
    i = Instituicao()
    i.setId(9829479)
    i.setDescricao('Uniacademia')

    

    # Adicionando as Turma a uma Instituição:
    i.addTurma(t1)
    i.addTurma(t2)
    i.addTurma(t3)

    

    # Dados de Disciplina 1:
    disc1 = Disciplina()
    disc1.setId(387837929)
    disc1.setDescricao('Orientação a Objeto')

    # Dados de Disciplina 2:
    disc2 = Disciplina()
    disc2.setId(23647245)
    disc2.setDescricao('Analise de Sistemas')

    # Dados de Disciplina 3:
    disc3 = Disciplina()
    disc3.setId(387837929)
    disc3.setDescricao('Desenvolvimento de Web Sites')
    
   
    # Adicionando as Turmas a uma Disciplina:
    disc1.addTurma(t1)
    disc1.addTurma(t2)
    disc1.addTurma(t3)
    
    
    # Dados da Pessoa 1(Professor):
    pp1 = Professor()
    pp1.setId(2)
    pp1.setNome('Lennon')
    pp1.setCpf('34897289472897')
    pp1.setDataNascimento(datetime.strptime('19/11/1998', '%d/%m/%Y'))
    pp1.setEmail('gmail@gmail.com')
    pp1.setEndereco('Rua A')
    pp1.setTelefone('32156789')
    pp1.setIdentidade('74387892343824')
    pp1.setMatricula('Ativo')
    pp1.setTitulocaoMaxima('Mestre')

    # Dados da Pessoa 2(Professor):
    pp2 = Professor()
    pp2.setId(2)
    pp2.setNome('Otavio')
    pp2.setCpf('43857384957')
    pp2.setDataNascimento(datetime.strptime('06/09/1999', '%d/%m/%Y'))
    pp2.setEmail('gmail@gmail.com')
    pp2.setEndereco('Rua B')
    pp2.setTelefone('32109753')
    pp2.setIdentidade('34895738945')
    pp2.setMatricula('Ativo')
    pp2.setTitulocaoMaxima('Doutor')

    

    # Adicionando um Diário a um Professor:
    pp1.addTurma(t1)
    pp1.addTurma(t2)

    
    
    # Dados do Curso 1:
    c1 = Curso()
    c1.setId(238478934)
    c1.setDescricao('Engenharia de Software')
    
    # Dados do Curso 2:
    c2 = Curso()
    c2.setId(43857398)
    c2.setDescricao('BSI')

    

    # Adicionando as Disciplinas a um Curso:
    c1.addDisciplina(disc1)
    c1.addDisciplina(disc2)
    c1.addDisciplina(disc3)

    

    # Adicionando Professores a um Curso:
    c1.addProfessor(pp1)
    c1.addProfessor(pp2)

    
        
    # Adicionando Curos a um Professor:
    pp1.addCurso(c1)
    pp1.addCurso(c2)

    

    #####################

    print("Aluno 1:")
    print(pa1.__str__())

    # Lista da Alunos nessa situação:
    print()
    print("Situação do Aluno:")
    print(s.__str__())
    print()
    print("Lista de Alunos nessa situação:")
    for sit in s.getAluno():
        print(sit)

    # Print dos Diarios dos Alunos:
    print()
    print("Diário dos Alunos:\n")
    print(' - Diário do Aluno 1:')
    for pa in pa1.getDiario():
        print(pa)
    print(' - Diário do Aluno 2:')
    for pa in pa2.getDiario():
        print(pa)

    print()
    print("Informações da Turma 1:")
    print(t1.__str__())

    # Print dos Diarios das Turmas:
    print()
    print('Lista de diarios da Turma:\n')
    print('Diario do Aluno 1:')
    for t in t1.getDiario():
        print(t)
    print('Diario do Aluno 2:')
    for t in t2.getDiario():
        print(t)

    print()
    print("Instituição:")
    print(i.__str__())

    # Print das Turmas de uma Instituição:
    print()
    print('Lista de turmas da instituição:')
    for inst in i.getTurma():
        print(inst)

    print()
    print('Disciplina 1:')
    print(disc1.__str__())

    # Print das Turmas de uma Disciplinas:
    print()
    print('Lista de turmas na disciplina 1:')
    for di in disc1.getTurma():
        print(di)

    print()
    print("Professor 1:")
    print(pp1.__str__())
    
    # Print da lista de turmas de um Professor:
    print()
    print('Lista de turmas do Professor 1:')
    for pp in pp1.getTurma():
        print(pp)

    print()
    print('Informações do Curso 1')
    print(c1.__str__())

    # Print das disciplinas do Curso 1:
    print()
    print('Disciplinas no Curso 1:')
    for c in c1.getDisciplina():
        print(c)


    # Print dos Professores do Curso 1:
    print()
    print('Professores no Curso 1:')
    for c in c1.getProfessor():
        print(c)

    # Print dos cursos do Professor 1:
    print()
    print('Cursos do Professor 1:')
    for pp in pp1.getCurso():
        print(pp)





if __name__ == '__main__':
    principal()

