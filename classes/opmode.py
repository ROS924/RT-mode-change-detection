class OPMODE:
    def __init__(self, id, Q, T,A):
        self.id = id
        self.budget = Q
        self.deadline = T
        self.beneficio = A
        self.utilizacao = Q/T   

    def __repr__(self):
        return repr((self.budget, self.deadline, self.beneficio))
    
    def getBudget(self):
        return self.budget
    
    def getDeadline(self):
        return self.deadline
    
    def getBeneficio(self):
        return self.beneficio
    
    def getId(self):
        return self.id