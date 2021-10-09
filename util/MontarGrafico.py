import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
import pandas as pd
import math
colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

def MontarGraficoCurva(paises, dados, ano1, ano2, cores,titulo,eixo_Y):  
    #Ele recebe o nome dos paises, e os dados para a criação do grafico em curva
    print("Criou o Grafico dos paises " + str(paises))
    anos = []
    
    #gera o intervalo de anos apartir da entrada do usuario para o eixo x
    for ano in range(ano1, ano2 + 1):
    	anos.append(ano)
    #gera as curvas do grafico
    for i in range(0, len(paises)):
        plt.plot(anos, dados[i], label = str(paises[i]), color = cores[i])

    plt.title(titulo)
    plt.ylabel(eixo_Y)
    plt.xlabel("Anos")
    plt.legend()
    plt.show()
    return


def MontarGraficoBarra(paises, dados, ano1, ano2, cores, titulo,eixo_Y):  
    #Ele recebe o nome dos paises, e os dados para a criação do grafico em curva
    print("Criou o Grafico dos paises " + str(paises))
    anos = []
    #gera o intervalo de anos apartir da entrada do usuario para o eixo x
    for ano in range(ano1, ano2 + 1):
    	anos.append(ano)
    #chama a função com as variações de grafico e em seguida mostra ao usuario
    ax = plt.subplot()
    ax = DefinirAx(ax, np.array(anos), dados, cores, paises)

    plt.title(titulo)
    plt.ylabel(eixo_Y)
    plt.xlabel("anos")
    plt.legend(loc = "best")
    plt.show()
    return

def DefinirAx(ax, a, dados, cores, paises):         #Função para a formatação do grafico de barras
    width = 0.7                                     #de Acordo com a quantidade de dados escolhidos pelo usuario

    if(len(dados) == 1):
        ax.bar(a,dados[0], width/2, align="center", color=cores[0], label = str(paises[0]))

    if(len(dados) == 2):
        ax.bar(a-width/2, dados[0], width/2, align="center", color=cores[0], label = str(paises[0]))
        ax.bar(a,dados[1], width/2, align="center", color=cores[1], label = str(paises[1]))

    if(len(dados) == 3):
        ax.bar(a-width/3, dados[0], width/3, align="center", color=cores[0], label = str(paises[0]))
        ax.bar(a,dados[1], width/3, align="center", color=cores[1], label = str(paises[1]))
        ax.bar(a+width/3, dados[2], width/3, align="center", color=cores[2], label = str(paises[2]))

    if(len(dados) == 4):
        ax.bar(a-width/4, dados[0], width/4, align="center", color=cores[0], label = str(paises[0]))
        ax.bar(a-width/2, dados[1], width/4, align="center", color=cores[1], label = str(paises[1]))
        ax.bar(a+width/2, dados[2], width/4, align="center", color=cores[2], label = str(paises[2]))
        ax.bar(a+width/4, dados[3], width/4, align="center", color=cores[3], label = str(paises[3]))

    if(len(dados) == 5):
        ax.bar(a-width/5, dados[0], width/5, align="center", color=cores[0], label = str(paises[0]))
        ax.bar(a-width/2.5, dados[1], width/5, align="center", color=cores[1], label = str(paises[1]))
        ax.bar(a, dados[2], width/5, align="center", color=cores[2], label = str(paises[2]))
        ax.bar(a+width/2.5, dados[3], width/5, align="center", color=cores[3], label = str(paises[3]))
        ax.bar(a+width/5, dados[4], width/5, align="center", color=cores[4], label = str(paises[4]))
    return ax

