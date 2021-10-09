from model import Paises
#from model2 import Paises1
#Controller do Modulo Paises. 

#recebe os dados do .csv
def getpaises():
    return Paises.getPaisesNome()

#recebe os dados do usuario para o csv 1
def getData(paises, anoI, anoF):
    return Paises.getData(paises, anoI, anoF)
#recebe os dados do usuario para o csv 2
def getData1(paises, anoI, anoF):
    return Paises.getData1(paises, anoI, anoF)
#recebe os dados do usuario para o csv 3
def getData2(paises, anoI, anoF):
    return Paises.getData2(paises, anoI, anoF)