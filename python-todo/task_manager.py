from sys import stdout

from task import Task
class TaskManager:

    taskList = []

    def __init__(self):
        pass

    def addTask(self, status, description):
        task = Task(len(self.taskList)+1, status, description)
        self.taskList.append(task)

    def setStatus(self, taskPosition, status):
        task = self.taskList[taskPosition - 1]
        task.setDone(status)

    def removeTask(self, taskPosition):
        del self.taskList[taskPosition - 1]

    def listTasks(self):
        for i in range(len(self.taskList)):
            self.taskList[i].printTask()
