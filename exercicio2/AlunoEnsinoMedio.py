from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def verificar_aprovacao(self):
        media = self.getMedia()
        if media >= 6:
            return "**APROVADO**"
        else:
            return "**REPROVADO**"


    