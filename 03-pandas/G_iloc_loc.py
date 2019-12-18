# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:05:09 2019

@author: Asus
"""

import pandas as pd

path_guardar_bin ="C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//artwork_data_completo.pikle"

df = pd.read_pickle(path_guardar_bin)
primero= df.loc[1035,'artist']

primero_todo= df.loc[0]

primero_iloc=df.iloc[0]

df2=df.set_index('id')

segundo_todo= df.loc[0]

segundo_iloc=df.iloc[0]

arr_notas=['7','8','9']

df3=pd.DataFrame(arr_notas,columns=['nota1'], index=['Pepito','Juanita','Maria'])

datos= {
        "nota1":{
                "Pepito":7,
                "Juanita":8,
                "Maria":9},
        "disciplina":{
                "Pepito":5,
                "Juanita":9,
                "Maria":2}}
notas=pd.DataFrame(datos)

notas.loc["Pepito"] #se filtra con los labels de los indices 

notas.iloc[0] #se filtra con indices

notas.loc["Pepito","disciplina"] 

notas.loc["Pepito",["disciplina","nota1"]] 

notas.loc[["Pepito","Juanita"]] 
notas.loc[["Pepito","Juanita"],"nota1"] 

notas.loc[[True,False,True]] 
condicion_nota=notas["nota1"] > 7
mayores_siete=notas.loc[condicion_nota] 

