class Task:


    def __init__(self, id, status, description):
        self.id = id
        self.status = status
        self.description = description

    def setDone(self, status):
        self.status = status

    def printTask(self):
        doneIcon = ""
        print("debug:", self.status)
        if self.status == True:
            doneIcon = "[\u2713]"
        else:
            doneIcon = "[ ]"

        print(f"{doneIcon} - {self.id} -  {self.description}")

