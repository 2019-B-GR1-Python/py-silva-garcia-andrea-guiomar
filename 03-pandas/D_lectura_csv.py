# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:41 2019

@author: Asus
"""

import pandas as pd
import os

#archivos que estan definidos por text como jason html xml csv...
#el siguiente grupo de archivos son los binarios
# tambien se puede leer directamente de una base de datos relacionales

path ="C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//artwork_data.csv"

df1 = pd.read_csv(path, nrows=10)

#seleccion de columnas
columnas=['id','artist','title','medium','year','acquisitionYear','height','width','units']

df2= pd.read_csv(path,nrows=10,usecols=columnas)

#definir cierta columna como el indice

df3= pd.read_csv(path,nrows=10,usecols=columnas, index_col='id')

#guardar el dateframe en formato binario pikle para volverlo a leer

path_guardar ="C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//artwork_data.pikle"

df3.to_pickle(path_guardar)
df4 = pd.read_csv(path)
path_guardar_bin ="C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//artwork_data_completo.pikle"

df4.to_pickle(path_guardar_bin)

df5 = pd.read_pickle(path_guardar_bin)



