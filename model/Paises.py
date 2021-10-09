import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def read_csv():     #Aqui fica o acesso ao banco de dados(arq.csv)
    gdp =  pd.read_csv("data/PibPaises.csv", header= 2, names = ["Country Name","Country Code","Indicator Name","Indicator Code","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    np.array(gdp)
    df = pd.DataFrame(gdp)
    return df

def getPaisesNome(): #Aqui ele encontra os paises determinados pelo usuario caso escolha a opção PIB
    df = read_csv()  #E os armazena em uma lista
    Paises = []
    for i in range(0, len(df["Country Name"])):
        Paises.append(str(df['Country Name'][i]))

    return Paises

def getData(paises, anoI, anoF):   #Recebe como parametro uma lista de paises e ano inicial e o ano final para fazer o grafico
    df = read_csv()
    Data = []
    for pais in paises:
        for i in range(0, len(df["Country Name"])):
            if df["Country Name"][i] == pais:
                data = []
                for ano in range(anoI, anoF+1):
                    data.append(float(df[str(ano)][i]))
                Data.append(data)
    return Data

def read_csv1():     #Aqui fica o acesso ao banco de dados(arq.csv1)
    gdp =  pd.read_csv("data/EspectativadeVidaNascer.csv", header= 2, names = ["Country Name","Country Code","Indicator Name","Indicator Code","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    np.array(gdp)
    df = pd.DataFrame(gdp)
    return df

def getPaisesNome1():  #Aqui ele encontra os paises determinados pelo usuario caso escolha a opção espectativa de vida
    df = read_csv1()   #E os armazena em uma lista para o .csv1
    Paises1 = []
    for i in range(0, len(df["Country Name"])):
        Paises1.append(str(df['Country Name'][i]))

    return Paises1

def getData1(paises, anoI, anoF):   #Recebe como parametro uma lista de paises e ano inicial e o ano final para fazer o grafico
    df = read_csv1()
    Data1 = []
    for pais in paises:
        for i in range(0, len(df["Country Name"])):
            if df["Country Name"][i] == pais:
                data1 = []
                for ano in range(anoI, anoF+1):
                    data1.append(float(df[str(ano)][i]))
                
                Data1.append(data1)
    return Data1

def read_csv2():     #Aqui fica o acesso ao banco de dados(arq.csv2)
    gdp =  pd.read_csv("data/AnosEstudo.csv", header= 2, names = ["Country Name","Country Code","Series","Series Code","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    np.array(gdp)
    df = pd.DataFrame(gdp)
    return df

def getPaisesNome2():   #Aqui ele encontra os paises determinados pelo usuario caso escolha a opção Anos de estudo
    df = read_csv2()    #E os armazena em uma lista para o .csv2
    Paises2 = []
    for i in range(0, len(df["Country Name"])):
        Paises2.append(str(df['Country Name'][i]))

    return Paises2

def getData2(paises, anoI, anoF):   #Recebe como parametro uma lista de paises e ano inicial e o ano final para fazer o grafico
    df = read_csv2()
    Data2 = []
    for pais in paises:
        for i in range(0, len(df["Country Name"])):
            if df["Country Name"][i] == pais:
                data2 = []
                for ano in range(anoI, anoF+1):
                    data2.append(float(df[str(ano)][i]))
                Data2.append(data2)
    return Data2


