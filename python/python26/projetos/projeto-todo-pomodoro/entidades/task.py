from datetime import datetime

class Task:

    
    status_pendente = "pendente"
    status_andamento = "em_andamento"
    status_concluido = "concluida"


    def __init__(self, titulo: str, prazo:str ,prioridade:int , descricao:str = ""):
        
        self.titulo      = titulo
        self.prazo       = prazo
        self.prioridade  = prioridade
        self.descricao   = descricao

        #status por padrão pendente
        self.status      = Task.status_pendente
    
        #data criação e conclusão(quando finalizar)
        self.data_criacao = datetime.now()
        self.data_conclusão = None


    def marcarConcluida(self):

        self.status = Task.status_concluido
        self.data_conclusão = datetime.now()

    # retorno da string
    def __str__(self):
        
        return f"Task: {self.titulo} | Status: {self.status} | Prioridade: {self.prioridade}"
