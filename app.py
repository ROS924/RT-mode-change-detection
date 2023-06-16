from uunifast import uunifasts, generateTaskSet
from classes.task import Task

tarefa1 = generateTaskSet(5,1)
tarefa1_1 = tarefa1[0]

tarefa2 = generateTaskSet(5,1)
tarefa2_1 = tarefa2[0]

tarefa3 = generateTaskSet(5,1)
tarefa3_1 = tarefa3[0]

print("TAREFA 1")
for i in tarefa1:
    task = Task(i.executionTime,i.period,i.deadline)
    executionTime = task.getExecutionTime()
    deadline = task.getDeadline()

    par = [executionTime, deadline]

    print(f"{par}\n")


print("TAREFA 2")
for i in tarefa2:
    task = Task(i.executionTime,i.period,i.deadline)
    executionTime = task.getExecutionTime()
    deadline = task.getDeadline()

    par = [executionTime, deadline]

    print(f"{par}\n")


print("TAREFA 3")
for i in tarefa3:
    task = Task(i.executionTime,i.period,i.deadline)
    executionTime = task.getExecutionTime()
    deadline = task.getDeadline()

    par = [executionTime, deadline]

    print(f"{par}\n")