from classes import par
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
    usable = []
    limite = len(parSet) - len(serverList)

    for i in range(limite):
        usable.append(parSet[i])

    ordenedParSet = sorted(usable, key = attrgetter('mode.utilizacao'), reverse = True)
    finalOrdParSet = sorted(ordenedParSet, key=attrgetter('mode.beneficio'),reverse = True)

    w = []

    somaU = 0

    for serv in serverList:
        U = serv.currentMode.utilizacao
        somaU += U

    b = 1 - somaU
    t = 1

    while (t <= limite) and (len(w) < len(serverList)):
        parId = 1
        Sw = []
        for pair in w:
            Sw.append(pair.server)

        for serv in serverList:
            if serv.id == t:
                if ((serv in Sw) == False):
                    modo = None
                    modoMark = serv.modeList[0]

                    for mdo in serv.modeList:                   
                        if mdo.id == t:
                            modo = mdo
                            break
                    
                    deltaU = modo.utilizacao - modoMark.utilizacao
                    if deltaU <= b:
                        w.append(par.PAR(parId,serv,modo))
                        b = b - deltaU
                
                break
                
        t += 1
    

    sW = []
    for pair in w:
        sW.append(pair.server)

    S_Sw = []
    
    for serv in serverList:
        if (serv in sW) == False:
            S_Sw.append(serv)

    nParId = w[len(w)-1].id + 1

    for servidor in S_Sw:
        w.append(par.PAR(nParId,servidor, servidor.modeList[0]))

    return w