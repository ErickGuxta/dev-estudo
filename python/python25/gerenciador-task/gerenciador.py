def add_task(tasks, name_task):
    
    task = {"name": name_task, "complete":False}
    tasks.append(task)

    print("Ok")

    return 

def view_task(tasks):
    for i, task in enumerate(tasks):
        status = "✔" if task["complete"] else " "

        name_tarefa = task["name"]
        print(f"{i+1}. [{status}] {name_tarefa}")
    return

def update_task(tasks, number_task_update, name_task_update,):
    indice_task = number_task_update - 1
    tasks[indice_task]["name"] = name_task_update

    print("Update task OK")
    return

def complete_task(number_task, tasks):
    indice_task = number_task - 1

    tasks[indice_task]["complete"] = True

    print("Complete task OK")


tasks = []
   

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Add task")
    print("2. View task")
    print("3. Update task")
    print("4. Complete task")
    print("5. Del task")
    print("6. Go out")

    e = int(input("Write your choice: "))

    #ADD TASK
    if e == 1:
        name_task = input("Write task: ")
        add_task(tasks, name_task)
    #VIEW TASK
    elif e == 2:
        view_task(tasks)
    #UPDATE TASK
    elif e ==3:
        view_task(tasks)

        number_task = int(input("Write the task number : "))
        name_task = input("Write the task name: ")

        update_task(tasks, number_task, name_task)
    #COMPLETAR TASK
    elif e == 4:
        view_task(tasks)

        number_task = int(input("Write the task number complete: "))
        complete_task(number_task, tasks)

    elif e == 6:
        break

    print("Finish programm")


    
print(tasks)