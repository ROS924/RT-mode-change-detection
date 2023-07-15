from dga import DGA
from classes import par

def maximo(parList,serverList):
    Max = None
    somaU = 0

    for serv in serverList:
        somaU += serv.modeList[0].utilizacao
    
    condicao1 = 1 - somaU

    for pair in parList:
        if Max == None:
            Max = pair
        else:
            deltaAMax = Max.mode.beneficio - Max.server.modeList[0].beneficio

            beneficio1 = pair.server.modeList[0].beneficio
            utilizacao1 = pair.server.modeList[0].utilizacao

            deltaA = pair.mode.beneficio - beneficio1
            deltaU = pair.mode.utilizacao - utilizacao1
            
            if deltaU <= condicao1:
                if deltaA > deltaAMax:
                    Max = pair

    return Max


def createParSet(serverList):
    parSet = []
    idCont = 1

    for serv in serverList:
        for mode in serv.modeList:
            if mode.id > 1:
                estePar = par.PAR(idCont, serv, mode)
                parSet.append(estePar)
                idCont += 1

    return parSet

def M_DGA(serverList):

    parSet = createParSet(serverList)

    parLinha = maximo(parSet,serverList)

    wLinha = []
    wLId = 1
    for serv in serverList:
        if serv != parLinha.server:
            wLinha.append(par.PAR(wLId,serv,serv.modeList[0]))
            wLId += 1
    
    wLinha.append(parLinha)

    w = DGA(serverList)  
    
      
    pass