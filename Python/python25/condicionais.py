idade = 18

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolecente")
elif idade < 65:
    print("Adulto")

# Forma compactada:

idade_nova = 20
retorno = "maior de idade" if idade_nova >= 18 else "menor de idade"
print(retorno)