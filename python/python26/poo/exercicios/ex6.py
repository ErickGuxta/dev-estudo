class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Equipe:
    def __init__(self, participantes, projeto):
        self.participantes = participantes
        self.projeto = projeto

class GerenciadorEquipes:
    def __init__(self):
        self.equipes = []

    def criarEquipe(self, alunos, projeto):
        for equipe in self.equipes:
            if equipe.projeto == projeto:
                for aluno in alunos:
                    for participante in equipe.participantes:
                        if aluno.cpf == participante.cpf:
                            print(f"Equipe não pode ser criada! {aluno.nome} já está em outra equipe com o mesmo projeto.")
                            return

        nova_equipe = Equipe(alunos, projeto)
        self.equipes.append(nova_equipe)
        print("Equipe criada com sucesso!")


# Teste
a1 = Aluno("Erick", "111")
a2 = Aluno("Cinthia", "222")
a3 = Aluno("Bob", "333")

g = GerenciadorEquipes()
g.criarEquipe([a1, a2], "Robo PI")          # Criada
g.criarEquipe([a2, a3], "App Mobile")       # Não criada (Cinthia já está)
g.criarEquipe([a2, a3], "Site Web")         # Criada (projeto diferente)