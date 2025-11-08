#Limitações das Lambdas

#As expressões lambda têm limitações importantes:

# -> São restritas a uma única expressão (sem múltiplas instruções)
# -> Não podem conter comandos como return, pass, assert ou atribuições
# -> Devem ser usadas para operações simples; para lógica complexa, use funções regulares


#função tradicional

def quadrado(x):
    return x**2

#função equivalente usando lambida
quadrado_lambda = lambda x: x**2 # lambda argumentos: expressão


print(quadrado(5))
print(quadrado_lambda(5))

par_impar = lambda x: "par" if x%2 == 0 else "impar"
print(par_impar(4))

"Lambdas com Funções de Ordem Superior"

"MAP()"
# map(função, iterável) - aplica a função a cada elemento do iterável
numeros = [1, 2, 3, 4, 5]

#Quadrado de cada número:

quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)

"FILTER()"
# filter(função, iterável) - filtra elementos baseado em uma função
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrando números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]


"SORTED()"
# sorted(iterável, key=None, reverse=False) - retorna uma lista ordenada de forma crescente(se for numeros)

alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 7.0},
    {"nome": "Maria", "nota": 9.0}
]

#ordenanar alunos por notas (maior pra menor)
por_nota = sorted(alunos, key= lambda aluno: aluno["nota"], reverse=True)
print([a["nome"] for a in por_nota])

"FILTER"
# filter(função, iterável) - filtra elementos baseado em uma função
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrando números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]


#### QUESTÕES

# Transformando e filtrando dados
dados = [
    {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 17, "cidade": "Rio de Janeiro"},
    {"nome": "Carlos", "idade": 32, "cidade": "São Paulo"},
    {"nome": "Diana", "idade": 15, "cidade": "Curitiba"},
    {"nome": "Eduardo", "idade": 28, "cidade": "Rio de Janeiro"}
]

# Filtrar maiores de idade e extrair seus nomes

#SEM LAMBDA
def extrair_idade(p):
    return p["idade"] >=18 #retorna true

maiores_idade = list(filter(extrair_idade, dados))
print(maiores_idade)

#EQUIVALENTE COM LAMBDA
maiores_idade = list(filter(lambda i: i["idade"] >= 18, dados))
nomes = list(map(lambda i: i["nome"], maiores_idade))

print(nomes)



