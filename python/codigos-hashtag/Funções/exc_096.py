# Faça um programa que tenha uma função chamada area(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno


def calculo_area(l, c): #não é obrigatorio definir um parâmetro 
    area = l * c
    return print("A área do terreno é de: {}".format(area))

l = float(input("Digite a largura do terreno: "))
c = float(input("Digite o comprimento do terreno: "))

calculo_area(l, c)