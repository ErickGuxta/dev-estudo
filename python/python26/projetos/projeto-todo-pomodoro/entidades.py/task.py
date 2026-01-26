from datetime import datetime

class task:

    
    status_pendente = "pendente"
    status_andamento = "em_andamento"
    status_concluido = "concluida"

    def __init__(self, titulo: str, prioridade: int, prazo:str, descricao:str = ""):
        
        self.titulo      = titulo
        self.prioridade  = prioridade
        self.prazo       = prazo
        self.descricao   = descricao

        #status por padrão pendente
        self.status_pendente

        #data criaçao



    # retorno da string
    def __str__(self):
        
        return f"Task: {self.titulo} | Status: {self.status} | Prioridade: {self.prioridade}"