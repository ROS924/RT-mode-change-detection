import random

def generateTaskFromUtilization(UtilizationSet):
    taskList = []
    for i in range(len(UtilizationSet)):
        p = random.randint(2, 50)
        e = p * UtilizationSet[i]
        taskList.append(Task(e,p,p))
    return taskList

class Task(object):
    def __init__(self, C, T, D):
        self.executionTime = C
        self.period = T
        self.deadline = D   


    def getPeriod(self):
        return self.period

    def getExecutionTime(self):
        return self.executionTime
    
    def getDeadline(self):
        return self.deadline

    def setImplicitDeadline(self):
        self.deadline = self.period