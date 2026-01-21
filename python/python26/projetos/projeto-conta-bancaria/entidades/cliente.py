# Módulo da Entidade Cliente

class Cliente:

    #método para difinir os atributos (contrutor):
    def __init__(self, nome = str, cpf = str):

        self.nome = nome
        self.cpf = cpf

        #lista para as contas dos meus clientes
        #obs.: o meu cliente ele pode ter uma ou varias contas  (corrente, poupança)
        self.contas = []

    #médodo para adicionar uma conta à lista de contas do cliente:
    def add_conta(self, conta):

        self.contas.append(conta)

    #método especial que define as representações em string de um objeto, ou seja, o retorno é sempre strings
    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}" 

