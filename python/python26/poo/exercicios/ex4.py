class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = 0

    def estudar(self, horas):
        self.tempoSemDormir += horas

    def dormir(self, horas):
        self.tempoSemDormir -= horas


# Teste
aluno = Aluno("Ana", "Engenharia")
aluno.estudar(8)
aluno.estudar(4)
aluno.dormir(6)

print(f"{aluno.nome} está sem dormir há {aluno.tempoSemDormir} horas.")
