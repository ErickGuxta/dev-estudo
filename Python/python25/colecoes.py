# --------- coleções ---------

            #/// listas(list) ///

import string


carros = ["carro1", "carro2", "carro3", 5, False]

#acessar:
primeiro_elemento = carros[0]

#modificar:
carros[4] = True

#adicionar e remover elementos:
carros.append("carro4")  # Adiciona ao final
carros.insert(0, "carro_insert") # indicando a posição a ser inserida
carros.extend(["civic", "corola"]) # adiciona vários

carros.remove("carro2") #remove pelo valor
ultimo_carro = carros.pop() #remove e retorna o último item
 

print(carros)

            #/// tuplas(tuple) -> são imutáveis///
cores_rgb = (255, 0, 0)
#desenpacotar
r, g, b = cores_rgb
print(r, g, b)


            #/// dicionários(dict) ///
config = {"debug": True, "max_connections": 100}  
misturado = {"chave": 1, 2: "valor", "lista": [1, 2, 3]}
vazio = {}


#acessar: obs: gera erro se a chava não existir
var = config["debug"]
var2 = config.get("teste", "mensagem que aparece se não existir a chave")


#adicionar e remover:
config['id'] = "08826254" 
del config["max_connections"]

print(config)

#interendo
for chave in config:
    print(f"{chave}: {config[chave]}")

#obter chaves e valores:
todas_chaves  = config.keys()
todos_valores = config.values()
todos_chave_valor = config.items() # Obter todos os pares chave-valor

print(todas_chaves)
print(todos_valores)

            #/// conjuntos(set) ///s - Coleções ordenntos duplicados
vogais = {"a", "e", "i", "o", "u"}   
vazio = set()

# Criando a partir de outras sequências
vogais = set[string]("aeiou")  # {"a", "e", "i", "o", "u"}
unicos = set[int]([1, 2, 2, 3, 3, 3, 4])  # {1, 2, 3, 4}


# Adicionando elementos
vogais.add("y")  # Em alguns idiomas, y pode ser considerada uma vogal

# Removendo elementos
vogais.remove("y")

# Operações de conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

uniao = conjunto1 | conjunto2        # {1, 2, 3, 4, 5, 6}
intersecao = conjunto1 & conjunto2   # {3, 4}
diferenca = conjunto1 - conjunto2    # {1, 2}