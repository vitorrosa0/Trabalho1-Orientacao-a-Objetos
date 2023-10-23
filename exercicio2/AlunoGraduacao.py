from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def verificar_aprovacao(self):
        media = self.getMedia()
        if media >= 7:
            return "**APROVADO**"
        else:
            return "**REPROVADO**"