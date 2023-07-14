from classes import opmode, task


class SERVER:
    def __init__(self, id:int, taskCalls:list, modeList:list):
        self.id = id
        self.taskIndex = 0
        self.taskCalls = taskCalls
        self.modeList = modeList
        self.currentMode = opmode.OPMODE(modeList[0].id,modeList[0].budget,modeList[0].deadline,modeList[0].beneficio)
        self.currentTask = task.Task(taskCalls[self.taskIndex][0],taskCalls[self.taskIndex][1],taskCalls[self.taskIndex][1])
        self.startTime = 0
        self.executedTime = 0
        self.executionTimePerQuantum = 0
        self.metDeadline = True
        self.deadlineLost = 0

    def getTaskCalls(self):
        return self.taskCalls
    
    def getMetDeadline(self):
        return self.metDeadline

    def getId(self):
        return self.id

    def getModeList(self):
        return self.modeList
    
    def addOpMode(self, newMode):
        self.modeList.append(newMode)

    def getCurrentMode(self):
        return self.currentMode
    
    def getStartTime(self):
        return self.startTime
    
    def getDeadline(self):
        modo = self.getCurrentMode()
        periodo = modo.getDeadline()
        
        return periodo
    
    def getBudget(self):
        modo = self.getCurrentMode()
        budget = modo.getBudget()

        return budget
    
    def getExecutedTime(self):
        return self.executedTime

    def getTaskExecTime(self):
        task = self.currentTask
        execution = task.getExecutionTime()
        return execution
    
    def getTaskDeadline(self):
        task = self.currentTask
        deadline = task.getDeadline()
        return deadline

    def updateStartTime(self):
        periodo = self.getDeadline()
        self.startTime = self.startTime + periodo
        return 0

    def getExecutionTimePerQuantum(self):
        return self.executionTimePerQuantum

    def clone(self):
        serv = SERVER(self.id,self.taskCalls,self.modeList)
        serv.id = self.id
        serv.taskCalls = self.taskCalls
        serv.modeList = self.modeList
        serv.currentMode = self.currentMode
        serv.currentTask = self.currentTask
        serv.executedTime = self.executedTime
        serv.startTime = self.startTime
        serv.executionTimePerQuantum = self.executionTimePerQuantum
        serv.taskIndex = self.taskIndex
        serv.metDeadline = self.metDeadline
        serv.deadlineLost = self.deadlineLost

        return serv


    def changeCurrentMode(self):
        pass

    def changeTask(self):
        taskQuantity = len(self.taskCalls)
        if(self.taskIndex < (taskQuantity-1)):
            self.taskIndex += 1
            tarefa = self.taskCalls[self.getTaskIndex()]
            self.currentTask = task.Task(tarefa[0], tarefa[1], tarefa[1])
            return True
        else:
            return False
        
    def getDeadlineLost(self):
        return self.deadlineLost
    
    def deadlinesPerdidos(self):
        perdidos = self.deadlineLost / len(self.taskCalls)
        return perdidos
    
    def getTaskIndex(self):
        return self.taskIndex
