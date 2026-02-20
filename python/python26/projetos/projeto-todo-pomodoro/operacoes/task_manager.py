from rich.traceback import install
install()

from datetime import datetime

from entidades.task import Task

"""
filtrar por prioridade
filtrar por status

create task OK


listar_task
get_task

editar task
concluir task
delete task
    _
"""


class TodoManager:

    """
        Classe para gerenciar operações
    """

    def __init__(self, nome:str = "Gerencidor") :
        #contador
        self._contID = 0
        self.nome = nome

        
        #dicionario com as task gerenciadas _dic = {"ID": task}
        self._gerenciar_tasks = {}

        self._prioridades = { 
            3: "alta",
            2: "media", 
            1: "baixa" 
        }

    def create_task(self, titulo: str, prazo:str, prioridade, descricao:str = "") -> Task:
        """
        Cria uma nova task e retorna a task criada.
        
        Args:
            titulo: Título da task (não pode ser vazio)
            prazo: Prazo da task (string)
            prioridade: Prioridade da task (1=baixa, 2=média, 3=alta)
            descricao: Descrição opcional da task
            
        Returns:
            Task criada ou None se houver erro
        """
        # Validação: título não vazio e prioridade válida (1, 2 ou 3)
        if titulo != "" and prioridade in self._prioridades:

            new_task = Task(titulo, prazo, prioridade, descricao)
            self._contID += 1
            self._gerenciar_tasks[self._contID] = new_task
            return new_task

        else:
            print("Erro: Entrada inválida. Título não pode ser vazio e prioridade deve ser 1, 2 ou 3.")
            return None

