import random
from classes.task import Task, generateTaskFromUtilization


def uunifast(n, U):
    vectU = []
    sumU = U
    for i in range(1, n):
        nextSumU = sumU * (random.uniform(0, 1)**(1/(n-i)))
        vectU.append(sumU-nextSumU)
        sumU = nextSumU
    vectU.append(sumU)
    AllSum = 0

    #summation over all utilization for finding global utilization
    for i in range(len(vectU)): 
        AllSum += vectU[i]

    return AllSum, vectU


def uunifasts(N, n, U):
    # if there is a file at the moment, overwrite on it 
    setList = []
    # will be used for configuration propose
    counter = 1
    while(counter <= N):
        Sum, Vect = uunifast(n, U)
        # Because of rounding errors, utilization may not be same as given U
        # for example, 0.9999 is unacceptable when utilization(U) is equal to 1
        if(Sum == U):
            # call function that makes the
            taskSet = generateTaskFromUtilization(Vect)
            setList.append(taskSet)
            #counters seperates outputs of each runs

            counter += 1
    return setList

# run 1000 time , make 100 job in each list and with 1 utilization
# set proper values here 
'''RUN = 10   # how many times we run unifast algorithm
JOB_NUMBERS = 6 #task number in each list 
UTILIZATION = 1 #Utilization
uunifasts(RUN, JOB_NUMBERS, UTILIZATION)'''

def generateTaskSet(taskQuantity:int,ImplicitDeadline:bool):
    taskSet = []
    i = 1
    t = random.randint(2,50)
    while i <= taskQuantity:
        T = t
        C = random.randint(1,T)
        D = random.randint(C,T)

        task = Task(C, T ,D)

        if(ImplicitDeadline == True):
            task.setImplicitDeadline()

        taskSet.append(task)

        i += 1
    
    return taskSet