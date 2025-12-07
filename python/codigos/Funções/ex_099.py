"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(* num):
    maior_numero = 0
    print("Analisando os valores de entrada... ")
    for i in num:
        print(f'{i}', end='')

    print(f"Ao todo foi informado {len(num)} valores. ")

    if len(num) == 0:
        print(f'O maior valor é {maior_numero}')
    
    else:
        maior_numero = max(num)
        print(f"O maior valor informado foi {maior_numero}")


maior(1 , 7, 10)
maior(6)
maior( )