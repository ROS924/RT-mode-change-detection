class OPMODE:
    def __init__(self, Q, T):
        self.budget = Q
        self.deadline = T   

    def __repr__(self):
        return repr((self.budget, self.deadline))
    
    def getBudget(self):
        return self.budget
    
    def getDeadline(self):
        return self.deadline