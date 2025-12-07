import random

# Gerar um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

tentativas = 0
max_tentativas = 10

print("Bem-vindo ao jogo de adivinhação!")
print("Eu escolhi um número entre 1 e 100. Tente adivinhar em até", max_tentativas, "tentativas.")

while tentativas < max_tentativas:
    # Solicitar uma tentativa ao jogador
    tentativa = int(input("Tentativa {}: ".format(tentativas + 1)))

    # Verificar se a tentativa é válida
    if tentativa < 1 or tentativa > 100:
        print("Por favor, insira um número entre 1 e 100.")
        continue

    # Verificar se a tentativa é correta
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou o número secreto:", numero_secreto)
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")

    tentativas += 1

if tentativas == max_tentativas:
    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)

