import time
import numpy as np
from os import system, name
from time import sleep
from classes import server, task


class EDF:

    ExecutingServer = None

    def __init__(self, Quantum=0, Overload=0):
        self.Quantum = Quantum
        self.Overload = Overload

    
    
    def Edf(self, ServerArray:server.SERVER, maxTime = 100):
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
        while maxTime != 0:

            for servidor in WorkingArray:# so coloca na lista de prontos se já chegou
                if servidor.getStartTime() <= TotalTime:
                    ReadyList = np.append(ReadyList, servidor)
                    WorkingArray = np.delete(WorkingArray, np.where(WorkingArray == servidor))
                    '''for i in range(TotalTime):
                        servidor.PrintList.append(" ")'''

            if ExecutingServer == None: # so escolhe o proximo se nenhum estiver sendo executado
                for servidor in ReadyList:
                    if servidor.getStartTime() <= TotalTime : # so escolhe o proximo caso alguem ja tenho chegado
                        if ExecutingServer == None: # escolhe o 1 para comparação
                            ExecutingServer = servidor
                        else: # encontra o deadline mais ceda dos que ja chegaram
                            if (servidor.getDeadline() - (TotalTime - servidor.getStartTime()))  < (ExecutingServer.getDeadline() - (TotalTime - ExecutingServer.getStartTime())):
                                ExecutingServer = servidor


            TotalTime += 1

            # Executando
            if not Overloading:
                try:
                    ExecutingServer.executedTime += 1
                    ExecutingServer.ExecutionTimePerQuantum += 1
                   # ExecutingServer.PrintList.append("X")


                    if ExecutingServer != None:
                        #self.progress_table.loc[int(ExecutingServer.ProcessId),TotalTime-1].configure({"background":'Green'}) #Ao ler o processo marca ele como verde
                        print(f"Executando servidor {ExecutingServer.getId()}")
                        TotalTime-1
                        
                        
                    
                    if (ExecutingServer.getDeadline() - (TotalTime - ExecutingServer.getStartTime())) < 0:
                         ExecutingServer.metDeadline = False
                    # else:
                    #     print(f'TotalTime: {TotalTime}') #Codigo de debug
                    #     print(f'ProcessId: {int(ExecutingServer.ProcessId)}') #Codigo de debug
                    #     self.progress_table.loc[int(ExecutingServer.ProcessId),TotalTime-1].configure({"background":'Green'}) #Ao ler o processo marca ele como verde
                    #     

                    if ExecutingServer.getExecutedTime() == ExecutingServer.getTaskExecutionTime(): # Remove o processo caso tenha terminado
                            if(ExecutingServer.getExecutedTime() <= ExecutingServer.getTaskDeadline()):
                                print(f"servidor {ExecutingServer.getId()}, Deadline: OK")
                            else:
                                print(f"servidor {ExecutingServer.getId()}, Deadline: PERDIDO")
                            
                            if(ExecutingServer.changeTask()):
                                print(f"Servidor {ExecutingServer.getId()} foi para a próxima instância da tarefa")
                            else:
                                print(f"fim da série temporal do servidor {ExecutingServer.getId()}")
                                ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingServer))
                                
                            ExecutingServer = None
                            maxTime -= 1        

                    elif ExecutingServer.getExecutionTimePerQuantum() == ExecutingServer.getBudget(): # Chega se acabou o tempo dele 
                        ExecutingServer.ExecutionTimePerQuantum = 0
                        Overloading = True        

                except:
                    pass

                
            else:
                #print("Overloading")
                if ExecutingServer != None:
                    print(f'TotalTime: {TotalTime}') #Codigo de debug
                    print(f'ProcessId: {int(ExecutingServer.getId())}') #Codigo de debug
                    self.progress_table.loc[int(ExecutingServer.ProcessId),TotalTime-1].configure({"background":'Red'}) #Ao ler o processo marca ele como vermelho
                    
                    
                ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingServer))
                ReadyList = np.append(ReadyList, ExecutingServer)

                
                for servidor in ReadyList:
                    if servidor.StartTime > TotalTime:#não sei se é necessario mas ta funcionando com
                        continue
                    servidor.PrintList.append("#")
                    servidor.WaitTime += 1
                OverloadTime -= 1
                if OverloadTime <= 0: # terminando overload
                    OverloadTime = self.Overload
                    ExecutingServer = None
                    Overloading = False
                
        return
    
    