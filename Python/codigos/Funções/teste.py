def alcoolico(bebida):
    bebida = bebida.upper()
    if 'BEB' in bebida:
        return True
    else:
        return False

produtos= ["beb46275", "tfa46275", "beb46435", "beb79271", "bsa46275"]

for produto in produtos:
    if alcoolico(produto):
        print("Enviar {} para o setor de bebidas alcolicas.".format(produto))
    else:
        pass



    