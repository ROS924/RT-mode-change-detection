import time
import numpy as np
from os import system, name
from time import sleep
from classes import server, task
from m_dga import M_DGA


class EDF:

    ExecutingServer = None

    def __init__(self, Quantum=0, Overload=0):
        self.Quantum = Quantum
        self.Overload = Overload

    
    
    def Edf(self, ServerArray:server.SERVER, maxTime = 1000000,ativar = True):
        
        """This function implement the earliest deadline first algorithm
        It's a dynamic priority algorithm in which there's a priority queue based on the closeness to each servidor' deadline.
        Args:
            ServerArray (_type_): _description_
        """
        WorkingArray = np.array([]) # lista de servidores que serão executados, mas talvez ainda não esteja prontos

        for servidor in ServerArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, servidor.clone() )

        CopyArray = np.array(WorkingArray)

        ReadyList = np.array([]) # lista de prontos
        TotalTime = 0 # tempo decorrido
        #ServerCount = WorkingArray.size
        ExecutingServer = None # processo no estado executando

        Overloading = False
        OverloadTime = self.Overload


        #execuçao dos processos
        while TotalTime <= maxTime :

            for servidor in WorkingArray:# so coloca na lista de prontos se já chegou
                if servidor.getStartTime() <= TotalTime:
                    ReadyList = np.append(ReadyList, servidor)
                    WorkingArray = np.delete(WorkingArray, np.where(WorkingArray == servidor))
                             

            if ExecutingServer == None: # so escolhe o proximo se nenhum estiver sendo executado
                for servidor in ReadyList:
                    if servidor.getStartTime() <= TotalTime : # so escolhe o proximo caso alguem ja tenho chegado
                        if ExecutingServer == None: # escolhe o 1 para comparação
                            ExecutingServer = servidor
                        else: # encontra o deadline mais ceda dos que ja chegaram
                            if (servidor.getDeadline() - (TotalTime - servidor.getStartTime()))  < (ExecutingServer.getDeadline() - (TotalTime - ExecutingServer.getStartTime())):
                                ExecutingServer = servidor


            TotalTime += 1

            if (len(ReadyList) == 0):
                break

            # Executando
            if (Overloading == False) :
                if (ExecutingServer != None):
                    ExecutingServer.executedTime += 1
                    ExecutingServer.executionTimePerQuantum += 1
                    


                    #if ExecutingServer != None:
                        #self.progress_table.loc[int(ExecutingServer.ProcessId),TotalTime-1].configure({"background":'Green'}) #Ao ler o processo marca ele como verde                       
                        #print(f"Executando servidor {ExecutingServer.getId()} no tempo {TotalTime}")
                        #print(ExecutingServer.getExecutedTime(), ExecutingServer.getTaskExecTime(), ExecutingServer.getTaskDeadline())

                        
                        
                    
                    if ( ExecutingServer.getExecutedTime() > ExecutingServer.getDeadline() ):
                        ExecutingServer.metDeadline = False
                    

                    if ExecutingServer.getExecutedTime() == ExecutingServer.getTaskExecTime(): # Remove o processo caso tenha terminado
                        sinal = False
                        tempoEspera = TotalTime - ExecutingServer.getStartTime()


                        if ativar == True:
                            for serv in ReadyList:
                                if (ExecutingServer.getId() == serv.getId()):
                                    c = ExecutingServer.getTaskExecTime()
                                    serv.completedTasks.append(c)
                                    #print(serv.completedTasks)
                                    #print("\nPARA\n")
                                    mudanca = serv.checkChange()
                                    print(ExecutingServer.getId(), mudanca)

                                    if (mudanca == True):
                                        parSet = M_DGA(CopyArray)
                                        
                                        for par in parSet:
                                            if (par.server.id == serv.getId()):
                                                serv.changeCurrentMode(par)
                                                print(f"Par -> servidor: {par.server.id}, modo: {par.mode.id}")
                                                break
                                    break

                        if(tempoEspera <= ExecutingServer.getTaskDeadline()):
                            a=1
                            #print(f"servidor {ExecutingServer.getId()}, Deadline: OK")
                        else:
                            #print(f"servidor {ExecutingServer.getId()}, Deadline: PERDIDO")
                            for serv in CopyArray:
                                if(ExecutingServer.getId() == serv.getId()):
                                    serv.deadlineLost += 1
                        
                        for servidor in ReadyList:
                            if(ExecutingServer.getId() == servidor.getId()):
                                if(servidor.changeTask()):
                                    #print(f"Servidor {servidor.getId()} foi para a próxima instância da tarefa")
                                    tempoChegada = servidor.getStartTime()
                                    proximaChegada = tempoChegada + servidor.getTaskDeadline()
                                    servidor.startTime = proximaChegada
                                    servidor.executedTime = 0
                                    servidor.executionTimePerQuantum = 0
                                else:
                                    sinal = True
                                    break

                        if (sinal == True):
                            #print(f"fim da série temporal do servidor {ExecutingServer.getId()}")
                            ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingServer))            

                        ExecutingServer = None     

                    elif ExecutingServer.getExecutionTimePerQuantum() == ExecutingServer.getBudget(): # Chega se acabou o tempo dele 
                        ExecutingServer.ExecutionTimePerQuantum = 0
                        Overloading = True        
  
            else:
                print(f"Overloading server {ExecutingServer.getId()} at time {TotalTime} ")
                if ExecutingServer != None:
                    parSet = M_DGA(CopyArray)

                    for serv in ReadyList:
                        if (ExecutingServer.getId() == serv.getId()):
                            for par in parSet:
                                if (par.server.id == serv.getId()):
                                    serv.changeCurrentMode(par)
                                    print(f"Par -> servidor: {par.server.id}, modo: {par.mode.id}")
                                    break
                        break
                    #print(f'TotalTime: {TotalTime}') #Codigo de debug
                    #print(f'ServerId: {int(ExecutingServer.getId())}') #Codigo de debug
                               
                ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingServer))
                ReadyList = np.append(ReadyList, ExecutingServer)

                ExecutingServer = None
                Overloading = False

                #print("Fim Overloading")
                
        for serv in CopyArray:
            perdidos = serv.deadlinesPerdidos()            
            print(f"\nServidor {serv.getId()} perdeu {perdidos*100}% dos seus deadlines")
        return
    
    