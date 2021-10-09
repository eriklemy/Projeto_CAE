import math
#FUNÇÕES PARA CALCULAR O IDH
def ExpVida(Ev):       #Espectativa de Vida
    e = (Ev - 20) / (83.2 - 20)
    return e 

def IndEdu(Ee,Ame):        #Indice de Educação
    ei = math.sqrt((Ee/13.2)*(Ame/20.6))/0.951
    return ei

def IndRen(pib):           #Indice de Renda
    ir = (math.log10(pib) - math.log10(163)) / (math.log10(108.211) - math.log10(163))
    return ir

def Idh(e,ei,ir):           #IDH
    idh = pow((e*ei*ir),1/3)
    return idh

def CalcularIDH(ev, ee, pib):      #Calcula o IDH dos paises no intervalo de ano escolhido pelo usuario
    idh = []

    for i in range(0, len(ev)):
        e, ei, ir, valor = [], [], [], []

        for j in range(0, len(ev[i])):
            e.append(round(ExpVida(ev[i][j]),3))
            ei.append(round(IndEdu(ee[i][j]/5,ee[i][j]),3))
            ir.append(round(IndRen(pib[i][j]),3))
        
        for j in range(0, len(e)):
            valor.append(Idh(e[j], ei[j], ir[j]).real)
        
        idh.append(valor)
    return idh


