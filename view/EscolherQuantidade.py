import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg

def anostr(ano1,ano2):
    try:
        Ano1 = int(ano1)
        Ano2 = int(ano2)
        return Ano1, Ano2
    except ValueError:
        sg.popup('Os anos devem ser escrito de forma numerica')

def EscolhaDados(values,retorno):
    print(values)
    retorno.append(int(values["quantCidades"])) 
    retorno.append(int(values["ano1"])) 
    retorno.append(int(values["ano2"]))
    if values["PIB"] == True:                
        if values["Histograma"] == True:
            retorno.append(5) 
        elif values["Curva"] == True:
            retorno.append(6)
        retorno.append(1)
    elif values["EV"] == True:
        if values["Histograma"] == True:
            retorno.append(5) 
        elif values["Curva"] == True:
            retorno.append(6)
        retorno.append(2)   
    elif values["EE"] == True:
        if values["Histograma"] == True:
            retorno.append(5) 
        elif values["Curva"] == True:
            retorno.append(6)
        retorno.append(3)
    elif values["IDH"] == True:
        if values["Histograma"] == True:
            retorno.append(5) 
        elif values["Curva"] == True:
            retorno.append(6)
        retorno.append(4)
    return retorno, EscolhaDados

def EscolherQuantidade():
    sg.theme('DarkPurple')  
    layout = [
                [sg.Text("Que dados gostaria de ver?")],
                [sg.Radio("PIB", "RADIO1", key="PIB", default=True), sg.Radio("Espectativa de vida",  "RADIO1", key="EV"),sg.Radio("Anos de Estudo",  "RADIO1", key="EE"),sg.Radio("IDH",  "RADIO1", key="IDH")],
                [sg.Text("Escolha os Paises que você quer ver o grafico")],
                [sg.Text("Escolha Quantidade de Paises\nE intervalo de anos que você quer ver o grafico", size = (10,0)),sg.Input(size = (15,0), key = 'quantCidades')],
                [sg.Text("Ano Inicial: ", size = (10,0)),sg.Input(size = (15,0), key = 'ano1')],
                [sg.Text("Ano Final: ", size = (10,0)),sg.Input(size = (15,0), key = 'ano2')],
                [sg.Text("Tipo de Grafico")],
                [sg.Radio("Histograma", "RADIO2", key="Histograma", default=True), sg.Radio("Curva",  "RADIO2", key="Curva")],
                [sg.Button("Ok"), sg.Button("Cancelar")]
            ]
    window = sg.Window('Projeto', layout)
    while True:
        event, values = window.read()
        if event in ("Ok"):
            retorno = [] # pylint: disable=unbalanced-tuple-unpacking
            anostr(values["ano1"],values["ano2"])
            if (values["ano1"] == '') or (values["ano2"] == '') or (values["quantCidades"] == ''):
                sg.popup('Faltam dados')  #Mostra Erro devido a falta de dados
            elif int(values["ano1"]) > 2019 or int(values["ano1"]) < 1970:
                sg.popup('valor não permitido \n   em ano incial')  #Mostra Erro de Entrada no ano 1
            elif int(values["ano2"]) > 2019 or int(values["ano2"]) < 1970:
                sg.popup('valor não permitido\n   em ano final')  #Mostra Erro de Entrada no ano 2
            elif values["quantCidades"] > "5" or values["quantCidades"] < "1":
                sg.popup('valor não permitido\n    quantidade de paises')  #Mostra Erro de Entrada no ano 2
            else:
                window.Close()
                EscolhaDados(values,retorno)
                return retorno
        elif event in ("Cancelar"):
            window.Close()