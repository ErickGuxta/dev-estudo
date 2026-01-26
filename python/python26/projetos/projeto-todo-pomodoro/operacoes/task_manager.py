from datetime import datetime

from entidades.task import Task

"""
filtrar por prioridade
filtrar por status

create task

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

    def __init__(self):
        #contador
        self._contID = 0

        
        #dicionario com as task gerenciadas _dic = {"ID": task}
        self._gerenciar_tasks = {}

        self._prioridades = { 
            3: "alta",
            2: "media", 
            1: "baixa" 
        }

    def create_task(self, titulo: str, prazo:str,prioridade, descricao:str = "") -> Task:

        new_task = Task(titulo, prazo,prioridade, descricao)

        self._contID += 1

        self._gerenciar_tasks[self._contID] = new_task
        