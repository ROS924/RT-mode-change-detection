class Task(object):
    def __init__(self, C, T, D):
        self.executionTime = C
        self.period = T
        self.deadline = D   

    def __repr__(self):
        return repr((self.executionTime, self.period, self.deadline))

    def getPeriod(self):
        return self.period

    def getExecutionTime(self):
        return self.executionTime
    
    def getDeadline(self):
        return self.deadline

    def setImplicitDeadline(self):
        self.deadline = self.period