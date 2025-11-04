print("Hello, World!")
print
#--------- variáveis ---------

#são de tipagem dinâmica e são case-sensitive

nome = "Maria"
idade =  25
altura = 1.87
estudante = True

# --------- strings ---------

nome = "Erick Gustavo"
sobrenome = "Costa de Souza"

#concatenação
nome_completo = nome + " " + sobrenome
print(nome_completo)

#fatiamento
tres_primeiras = nome[1:4] #a posição 4 é não incluso

#/// métodos úteis ///
texto = "python é incrível"

print(texto.upper())         # PYTHON É INCRÍVEL
print(texto.capitalize())    # Python é incrível
print(texto.replace("é", "é muito"))  # python é muito incrível
print(texto.split())         # ['python', 'é', 'incrível']
print(len(texto))            # 17 (comprimento da string)

