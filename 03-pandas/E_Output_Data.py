# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:58:00 2019

@author: Asus
"""

import pandas as pd
import os
import numpy as np
import sqlite3

path_guardar_bin ="C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//artwork_data_completo.pikle"

df5 = pd.read_pickle(path_guardar_bin)
df= df5.iloc[49980:50019,:].copy()

### EXCEL##
path_guardado2='C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//mi_df_completo.xlsx'
df.to_excel(path_guardado2,index=False) #execede 
columnas=['artist','title','year']
df.to_excel(path_guardado2,columns=columnas)

##multiples hojas de trabajo

path_multiple='C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//mi_df_multiples.xlsx'

writer= pd.ExcelWriter(path_multiple, engine= 'xlsxwriter') #engine el motor

df2.to_excel(writer, sheet_name='Primera')
df2.to_excel(writer, sheet_name='Segunda',index=False)
df2.to_excel(writer, sheet_name='Tercera',columns= columnas)

#para que se sobrescriba ahora se encuentra solo en memoria
writer.save()


##multiples hojas de trabajo

num_artistas=df['artist'].value_counts()
path_colores='C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//mi_df_colores.xlsx'

writer= pd.ExcelWriter(path_colores, engine= 'xlsxwriter') #engine el motor

num_artistas.to_excel(writer,sheet_name='Artistas')
#seleccionar la hoja con sheets
hoja_artistas=writer.sheets['Artistas']
#sintaxis especial meter un string
rango_celdas= 'B2:B{}'.format(len(num_artistas.index)+1)
#dar el formato se trabaja con un diccionario
formato_artistas={
        "type":"2 color scale",
        "min_value":"10",
        "max_value":"99",
        "max_type":"percentile",
        "min_type":"percentile"}

hoja_artistas.conditional_format(rango_celdas,formato_artistas)

writer.save()


###graficas
num_artistas=df['artist'].value_counts()
hoja_artistas=writer.sheets['Artistas']
path_grafica='C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//mi_df_grafica.xlsx'

writer= pd.ExcelWriter(path_grafica, engine= 'xlsxwriter') #engine el motor
data=df['artist']


chart=hoja_artistas.add_chart({'type':'line'})
chart.add_series({'values':rango_celdas})
hoja_artistas.insert_chart('C1',chart)
writer.save()