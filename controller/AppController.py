import view.EscolherQuantidade as eq
import view.ListarCidade as lc
import controller.PaisesController as PaisesController
import util.MontarGrafico as MontarGrafico
import util.FunçãoIDH as FuncIdh

def start():                          # "Main" do aplicativo  
    paises = PaisesController.getpaises()
    #variaveis com os dados recebidos na primeira janela da interface
    quant, ano1, ano2, escolha, escolha1 = eq.EscolherQuantidade()# pylint: disable=unbalanced-tuple-unpacking

    titulo = ["PIB dos Paises", "Espectativa de Vida", "Anos de Estudo", "IDH- PAISES"]
    eixo_Y = ["Bilhões/Trilhões(US$)", "Idade", "Anos Estudados", "Idh"]
    #coleta e armazena os dados para a 2° janela da interface
    paisesescolhidos, cores= lc.mostrarlistagemCidades(paises, quant)
    #veficação para os temas
    VerifTema(escolha, escolha1, paisesescolhidos, ano1, ano2, cores, titulo, eixo_Y)

def VerifTema(escolha, escolha1, paisesescolhidos, ano1, ano2, cores, titulo, eixo_Y):      #verifica qual foi o tema escolhido
    if escolha1 == 1:
        #variavel que armazena os dados de entrada do usuario
        dados = PaisesController.getData(paisesescolhidos, ano1, ano2)
        VerifGraf(escolha,paisesescolhidos, dados, ano1, ano2, cores,titulo[0],eixo_Y[0])
    elif escolha1 == 2:
        #variavel que armazena os dados de entrada do usuario para o .csv1
        dados = PaisesController.getData1(paisesescolhidos, ano1, ano2)
        VerifGraf(escolha,paisesescolhidos, dados, ano1, ano2, cores,titulo[1],eixo_Y[1])
    elif escolha1 == 3:
        #variavel que armazena os dados de entrada do usuario para o .csv2
        dados = PaisesController.getData2(paisesescolhidos, ano1, ano2)
        VerifGraf(escolha,paisesescolhidos, dados, ano1, ano2, cores, titulo[2], eixo_Y[2])
    elif escolha1 == 4:
        #variavel que armazena os dados de entrada do usuario para o .csv3
        dados = PaisesController.getData(paisesescolhidos, ano1, ano2)
        dados1 = PaisesController.getData1(paisesescolhidos, ano1, ano2)
        dados2 = PaisesController.getData2(paisesescolhidos, ano1, ano2)
        if escolha == 5:         #verificação para graficos
            MontarGrafico.MontarGraficoBarra(paisesescolhidos, FuncIdh.CalcularIDH(dados1, dados2, dados), ano1, ano2, cores, titulo[3],eixo_Y[3])
        elif escolha == 6:
            MontarGrafico.MontarGraficoCurva(paisesescolhidos, FuncIdh.CalcularIDH(dados1, dados2, dados), ano1, ano2, cores, titulo[3],eixo_Y[3])

def VerifGraf(escolha,paisesescolhidos, dados, ano1, ano2, cores,titulo,eixo_Y): #verifica qual o tipo de grafico
    if escolha == 5:         #verificação para graficos
        MontarGrafico.MontarGraficoBarra(paisesescolhidos, dados, ano1, ano2, cores, titulo, eixo_Y)
    elif escolha == 6:
        MontarGrafico.MontarGraficoCurva(paisesescolhidos, dados, ano1, ano2, cores, titulo, eixo_Y)