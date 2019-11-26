# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:54 2019

@author: Asus
"""
import numpy as np
import pandas as pd

lista_numeros= [1,2,3,4]
tupla_numeros=(1,2,3,4)
np_numeros= np.array((1,2,3,4))
serie_a= pd.Series(lista_numeros)
serie_b= pd.Series(tupla_numeros)
serie_c=pd.Series(np_numeros)
serie_d=pd.Series([
        True,
        False,
        12,
        12.12,
        "Andrea",
        None,
        (),
        [],
        {"nombre":"Andrea"}])
serie_d[3]

lista_ciudades=["Ambato","Cuenca",
               "Loja","Quito"]

lista_ciudad= pd.Series(lista_ciudades,
                        index=["A",
                               "C",
                               "L",
                               "Q"])
lista_ciudad["Q"]
lista_ciudad[3]



valores_ciudad={
        "Ibarra":9500,
        "Guayaquil":10000,
        "Quito":8000,
        "Cuenca":7000,
        "Loja":3000}

serie_valor_ciudad= pd.Series(valores_ciudad)
serie_valor_ciudad["Ibarra"]
serie_valor_ciudad[3]

ciudades_menores_5000= serie_valor_ciudad < 5000

s5=serie_valor_ciudad[ciudades_menores_5000]


mas_diez_porceinto=serie_valor_ciudad*1.1

serie_valor_ciudad=serie_valor_ciudad*1.1

multa= serie_valor_ciudad[3]-50
serie_valor_ciudad["Quito"]=serie_valor_ciudad["Quito"]-50


print("Lima"in serie_valor_ciudad)
print("Loja"in serie_valor_ciudad)



respuesta=np.square(serie_valor_ciudad)

resp_sen= np.sin(serie_valor_ciudad)



ciudades_uno=pd.Series({
        "Montañita":300,
        "Guayaqui":1000,
        "Quito":20000})

ciudades_do=pd.Series({
        "Loja":300,
        "Guayaqui":2000})



total_ciudad=ciudades_uno+ciudades_do

ciudades_uno["Loja"]=0

ciudades_do["Quito"]=0
ciudades_do["Montañita"]=0

ciu_add=ciudades_uno.add(ciudades_do)

ciu_concatenadas= pd.concat([ciudades_uno,ciudades_do])

ciu_concatenadas_v= pd.concat([ciudades_uno,ciudades_do],
                              verify_integrity=True)
ciud_append= ciudades_uno.append(ciudades_do,verify_integrity= True)


ciudades_uno.max()

pd.Series.max(ciudades_uno)
np.max(ciudades_uno)


ciudades_uno.min()

pd.Series.min(ciudades_uno)
np.min(ciudades_uno)



ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)




ciudades_uno.head(2)


ciudades_uno.tail(2)


ciudades_uno.sort_values(ascending=False).head(2)
ciudades_uno.sort_values().tail(2)

#funcion map convertir la seie en un arreglo
def calculo(valor):
    if(valor <=1000):
        return valor*1.05
    if(valor >1000 and valor <= 5000):
        return valor* 1.10
    if(valor>5000):
        return valor*1.15
ciudad_calculada=ciudades_uno.map(calculo)














