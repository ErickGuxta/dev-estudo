class ToDoList {
    constructor() {
        this.tarefas = []; // Armazena as tarefas como objetos
    }

    // Adicionar uma tarefa
    adicionarTarefa(descricao) {
        const novaTarefa = {
            id: Date.now(), // Gera um ID único com base no timestamp
            descricao,
            concluida: false
        };
        this.tarefas.push(novaTarefa);
        console.log(`Tarefa adicionada: "${descricao}"`);
    }

    // Listar todas as tarefas
    listarTarefas() {
        if (this.tarefas.length === 0) {
            console.log("Nenhuma tarefa cadastrada.");
            return;
        }

        console.log("Lista de tarefas:");
        this.tarefas.forEach((tarefa, index) => {
            const status = tarefa.concluida ? "✅" : "❌";
            console.log(`${index + 1}. ${tarefa.descricao} [${status}]`);
        });
    }

    // Marcar uma tarefa como concluída
    concluirTarefa(id) {
        const tarefa = this.tarefas.find(t => t.id === id);
        if (!tarefa) {
            console.log("Tarefa não encontrada.");
            return;
        }

        tarefa.concluida = true;
        console.log(`Tarefa concluída: "${tarefa.descricao}"`);
    }

    // Remover uma tarefa
    removerTarefa(id) {
        const indice = this.tarefas.findIndex(t => t.id === id);
        if (indice === -1) {
            console.log("Tarefa não encontrada.");
            return;
        }

        const [tarefaRemovida] = this.tarefas.splice(indice, 1);
        console.log(`Tarefa removida: "${tarefaRemovida.descricao}"`);
    }
}

// Testando a To-Do List
const minhaToDo = new ToDoList();

// Adicionando tarefas
minhaToDo.adicionarTarefa("Comprar pão");
minhaToDo.adicionarTarefa("Estudar JavaScript");

// Listando tarefas
minhaToDo.listarTarefas();

// Concluindo uma tarefa
const idParaConcluir = minhaToDo.tarefas[0].id; // Pega o ID da primeira tarefa
minhaToDo.concluirTarefa(idParaConcluir);

// Listando novamente
minhaToDo.listarTarefas();

// Removendo uma tarefa
const idParaRemover = minhaToDo.tarefas[1].id; // Pega o ID da segunda tarefa
minhaToDo.removerTarefa(idParaRemover);

// Listando novamente
minhaToDo.listarTarefas();
