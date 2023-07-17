from classes import opmode,server
#from series_temporais_base.tarefas import t1, t2, t3  usado para testes
from edf import EDF
import edf2
from uunifast import generateTaskSet

server1ModeList = [opmode.OPMODE(1,10,100,0.125),opmode.OPMODE(2,15,50,0.375),opmode.OPMODE(3,50,100,0.625),opmode.OPMODE(4,35,50,0.875),opmode.OPMODE(5,56,70,1.00)]
server2ModeList = [opmode.OPMODE(1,30,200,0.200),opmode.OPMODE(2,25,100,0.333),opmode.OPMODE(3,16,40,0.533),opmode.OPMODE(4,10,200,0.733),opmode.OPMODE(5,30,40,1.00)]
server3ModeList = [opmode.OPMODE(1,10,200,0.076),opmode.OPMODE(2,8,40,0.307),opmode.OPMODE(3,21,60,0.538),opmode.OPMODE(4,30,50,0.923),opmode.OPMODE(5,65,100,1.00)]
server4ModeList = [opmode.OPMODE(1,7,100,0.175),opmode.OPMODE(2,9,60,0.375),opmode.OPMODE(3,10,50,0.500),opmode.OPMODE(4,15,50,0.750),opmode.OPMODE(5,40,100,1.00)]

tarefas1 = generateTaskSet(100,1)
tarefas2 = generateTaskSet(100,1)
tarefas3 = generateTaskSet(100,1)
tarefas4 = generateTaskSet(100,1)


server1 = server.SERVER(1,tarefas1,server1ModeList)
server2 = server.SERVER(2,tarefas2,server2ModeList)
server3 = server.SERVER(3,tarefas3,server3ModeList)
server4 = server.SERVER(4,tarefas4,server4ModeList)

serverArray = [server1, server2, server3, server4]

escalonador = EDF() 
escalonador2 = edf2.EDF()

#escalonador.Edf(serverArray) # sem mudança de modo

escalonador2.Edf(serverArray) # com mudança de modo
