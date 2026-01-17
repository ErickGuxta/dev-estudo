# Módulo das Classes/Entidades de Conta (abstrata, corrente, poupanca)

# Importa a classe base abstrata e o decorador para métodos abstratos | Abstract Base Class - Classe Base Abstrata
from abc import ABC, abstractmethod

# Importa Data time
from datetime import datetime


class Conta(ABC):

    """
        CLASSE BASE PARA TODAS AS OUTRAS CONTAS
    """

    _total_contas = 0
    #construtor da classe
    def __init__(self, numero=int, cliente):
        # definindo os atributos como privador (_protegido)
        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        
        #hitorico de transações
        self._historico = []

        #incrementa o numero de contas criadas
        Conta._total_contas+= 1

    # Propriedade para acessar o saldo de forma controlada
    @property
    def saldo(self)