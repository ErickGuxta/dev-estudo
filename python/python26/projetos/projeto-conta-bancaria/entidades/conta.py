# Módulo das Classes/Entidades de Conta (abstrata, corrente, poupanca)

# Importa a classe base abstrata e o decorador para métodos abstratos | Abstract Base Class - Classe Base Abstrata
from abc import ABC, abstractmethod

# Importa Data time
from datetime import datetime

# Importa exceção personalizada
from utilitarios.exceptions import SaldoInsuficienteError

class Conta(ABC):

    """
        CLASSE BASE PARA TODAS AS OUTRAS CONTAS
    """

    _total_contas = 0
    #construtor da classe
    def __init__(self, numero: int, cliente):
        # definindo os atributos como privador (_protegido)
        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        
        #hitorico de transações
        self._historico = []

        #incrementa o numero de contas criadas
        Conta._total_contas+= 1

    """
       OBS.! o decorador @property é usado para transformar um método em uma propriedade(atributos) de uma classe. Vai permitir que o método seja 
        acessado como atributo
    """

    # ---- Propriedade para acessar o saldo de forma controlada ----
    @property
    def saldo(self):
        """ GETTER para o saldo, permitindo acesso controlado """
        return self._saldo

    # ---- Método de classe para consultar o número total de contas ----
    @classmethod
    def get_total_contas(cls):
        """ método de classe para consultar o numero total de contas"""

        return cls._total_contas

    # ---- Método para realizar depósitos ----
    def depositar(self, valor : float):

        if valor > 0:
            self.saldo += valor
        
            self._historico.append((datetime.now(), f"Depósito de R$ {valor:.2f}"))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso! ")

        else:
            print("Deposito Inválido")

    # ---- Método para realizar saques ----
    @abstractmethod
    def sacar(self, valor : float):
        """ Método abstrato para sacar um valor. Deve ser implementado pelas subclasses"""
        pass

    # ---- Método para exibir extrato ----
    def extrato(self):

            """Exibe o extrato da conta."""
            print(f"\n--- Extrato da Conta Nº {self._numero} ---")
            print(f"Cliente: {self._cliente.nome}")
            print(f"Saldo atual: R${self._saldo:.2f}")
            print("Histórico de transações:")

            # Caso não haja transações registradas
            if not self._historico:
                print("Nenhuma transação registrada.")

            # Percorre o histórico e exibe cada transação
            for data, transacao in self._historico:
                print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")
            print("--------------------------------------\n")

# ---- Subclasse ContaCorrente ----
class ContaCorrente(Conta):

    # Construtor com limite padrão de cheque especial
    def __init__(self, numero: int, cliente, limite: float = 500.0):
         #chama o construtor da classe base
         super().__init__(numero, cliente)

         #define o limite de cheque
         self.limite = limite
    
    # Implementação do método abstrato herdado sacar
    def sacar(self, valor: float):
        if valor <= 0:
            print("Valor de saque inválido")
            return
        
        saldo_disponivel = self.saldo + self.limite

        # Caso o valor do saque ultrapasse o saldo disponível
        if valor > saldo_disponivel:
                raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes.")

        # Reduz o valor do saque do saldo
        self.saldo -= valor

        # Registra a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
            

# ---- Subclasse ContaPupanca ----
class ContaPoupanca(Conta):
    # Construtor da poupança, herda do construtor base
    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)

    # Implementação do método sacar apenas com saldo disponível
    def sacar(self, valor: float):

        # Permite saque apenas se houver saldo suficiente na conta.
        if valor <= 0:
            print("Valor de saque inválido.")
            return

        # Verifica se há saldo suficiente
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
            
        # Deduz o valor do saldo
        self.saldo -= valor
        
        # Registra a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")