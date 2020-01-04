# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:19:35 2020

@author: Asus
"""

import pandas as pd
import math
import numpy as np

path_guardar_bin ="C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//artwork_data_completo.pikle"

df = pd.read_pickle(path_guardar_bin)

seccion_df=df.iloc[49980:50019,:].copy()

df_agrupado= seccion_df.groupby('artist')
type(df_agrupado)

for acquisitionYear, registros in df_agrupado:
    print(registros)
    

for a,b in df_agrupado:
    print(a)

a=seccion_df['units'].value_counts()
a.empty
def llenar_valores_vacios(series,tipo):
    lista_valores= series.value_counts()
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
            
            suma=0
            numero_valores=0
            for valor_serie in series:
                
                if(isinstance(valor_serie,str)):
                    valor= int(valor_serie)
                    numero_valores = numero_valores+1
                    suma= suma+valor
                else:
                    pass
                    
            promedio= suma/numero_valores
            
            series_valores_llenos= series.fillna(promedio)
            return series_valores_llenos
        if(tipo == 'repite'):
            valor_cambia=series.value_counts()
            series_valores_llenos= series.fillna(valor_cambia.index[0])
            return series_valores_llenos
                
                     
        
def transformar_df(df):
    df_artist= df.groupby('artist')
    lista_df=[]
    for artista,df in df_artist:
        copia = df.copy()
        serie_w=copia['width']
        serie_h=copia['height']
        serie_u=copia['units']
        serie_i=copia['inscription']
        copia.loc[:,'width']=llenar_valores_vacios(serie_w,'promedio')
        copia.loc[:,'height']=llenar_valores_vacios(serie_h,'promedio')
        copia.loc[:,'units']=llenar_valores_vacios(serie_u,'repite')
        copia.loc[:,'inscription']=llenar_valores_vacios(serie_i,'repite')
        lista_df.append(copia)
    df_completo_con_valores=pd.concat(lista_df)
    return df_completo_con_valores
        
df_valores_llenos=transformar_df(seccion_df)
        
                
            
        
    


