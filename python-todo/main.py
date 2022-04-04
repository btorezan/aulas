from task_manager import TaskManager
if __name__ == '__main__':

    #Instanciando Manager
    taskManager = TaskManager()

    #Adicionando Task
    taskManager.addTask(False, "Comprar Arroz")
    taskManager.addTask(False, "Comprar Feijão")
    taskManager.addTask(False, "Comprar Batata")
    taskManager.addTask(False, "Comprar Macarrão")

    #Marcando task como concluida
    taskManager.setStatus(1, True)
    taskManager.setStatus(2, True)

    #Removendo Task
    taskManager.removeTask(4)

    #Listando Tasks
    taskManager.listTasks()
