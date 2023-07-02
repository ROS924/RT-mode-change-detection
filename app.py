from classes import opmode,server
from series_temporais_base.tarefas import t1, t2, t3

server1ModeList = [opmode.OPMODE(10,100),opmode.OPMODE(30,20),opmode.OPMODE(10,200),opmode.OPMODE(7,100)]
server2ModeList = [opmode.OPMODE(15,50),opmode.OPMODE(25,100),opmode.OPMODE(8,40),opmode.OPMODE(9,60)]
server3ModeList = [opmode.OPMODE(50,100),opmode.OPMODE(16,40),opmode.OPMODE(21,60),opmode.OPMODE(10,50)]
server4ModeList = [opmode.OPMODE(35,50),opmode.OPMODE(110,200),opmode.OPMODE(30,50),opmode.OPMODE(15,50)]
server5ModeList = [opmode.OPMODE(56,70),opmode.OPMODE(30,40),opmode.OPMODE(65,100),opmode.OPMODE(40,100)]

server1 = server.SERVER(1,t1,server1ModeList)
server2 = server.SERVER(2,t2,server2ModeList)
server3 = server.SERVER(3,t3,server3ModeList)