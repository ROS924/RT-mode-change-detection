class SERVER:
    def __init__(self, taskCalls:list, modeList:list):
        self.taskCalls = taskCalls
        self.modeList = modeList
        self.currentMode = modeList[0]

    def getTaskCalls(self):
        return self.taskCalls
    
    def getModeList(self):
        return self.modeList
    
    def addOpMode(self, newMode):
        self.modeList.append(newMode)


    def changeCurrentMode(self):
        pass