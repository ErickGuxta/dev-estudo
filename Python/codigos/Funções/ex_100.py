"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint


def sorteia(lista):
    numeros = list()
    for n in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Sorteando {len(numeros)} valores da lista: ', end="")

    for i in numeros:
        print(f'{i}', end="")
    return numeros

def soma(lista_numeros):
    numeros_pares = list()
    for n in lista_numeros:
        if n % 2 == 0:
            numeros_pares.append(n)
    print(f' A soma dos valores pares é: {sum(numeros_pares)}')


soma(sorteia('lista'))


