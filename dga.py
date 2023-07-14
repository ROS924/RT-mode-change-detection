from classes import par, server, opmode
from operator import attrgetter

def createParSet(serverList):
    parSet = []
    idCont = 1

    for serv in serverList:
        for mode in serv.modeList:
            estePar = par.PAR(idCont, serv, mode)
            parSet.append(estePar)
            idCont += 1

    return parSet

def DGA(serverList):

    parSet = createParSet(serverList)
    ordenedParSet = sorted(parSet, key = attrgetter('mode.utilizacao'), reverse = True)
    finalOrdParSet = sorted(ordenedParSet, key=attrgetter('mode.beneficio'),reverse = True)

