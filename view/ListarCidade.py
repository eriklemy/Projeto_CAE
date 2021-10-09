import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.colors import is_color_like

def mostrarlistagemCidades(cidades, quantCidades):    #Gera a Interface Grafica 2
    sg.theme('DarkPurple3')                           #com base nas entradas do usuario 
    layout = [
                [sg.Text("Selecione os Paises que você quer ver no grafico")]
            ]
    for i in range(0,quantCidades):
        layout.append([sg.Text("Selecione a sigla do " + str(i + 1) + "ª Pais:", size = (15,0)),sg.Combo(cidades, key = str("Teste" + str(i)), size = (10,20))])
    layout.append([sg.Text("Diga a cor(ingles):")])
    for i in range(0,quantCidades):
        layout.append([sg.Text(str(i + 1)+ "ª cor:", size = (5,0)),sg.Input(size = (23,0), key = "cores" +str(i))])

    layout.append([sg.Button("Ok"), sg.Button("Cancelar")])
    window = sg.Window('Projeto', layout)
    while True:    #loop de execução
        event, values = window.read()
        if event in ("Ok"):
            if(testarcor(values, quantCidades) == False):
                sg.popup("entrada invalida em cor")
                continue
            window.Close()
            paisesescolhidos, cores = [], []
            for i in range(0, quantCidades):  
                teste = "Teste" + str(i)   #salva os dados em uma lista para ser utilizado na busca e na função geradora do grafico
                cor = "cores" +str(i)
                paisesescolhidos.append(values[teste]), cores.append(values[cor])                               
            return paisesescolhidos,cores
        elif event in ("Cancelar"):
            window.Close()  #fecha a janela
    window.Close()  

def testarcor(values, quant):     #Testar se a cor entrada é valida
    for i in range(0, quant):
        cor = 'cores' + str(i)
        if is_color_like(values[cor]) == False:
            return False
        
    return True