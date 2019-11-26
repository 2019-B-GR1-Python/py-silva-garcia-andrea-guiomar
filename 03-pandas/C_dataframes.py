# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:20 2019

@author: Asus
"""
import pandas as pd
import numpy as np


arr_pand = np.random.randint(0, 10, 6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]
nueva_serie = pd.Series([1000,2000])
df1.append(nueva_serie, ignore_index = True)
df1[3] = nueva_serie
df1[4] = s1 * s2

datos_fisicos_uno = pd.DataFrame(arr_pand, columns = ['Estatura (cm)', 'Peso (kg)', 'edad (anios)'])
datos_fisicos_dos = pd.DataFrame(arr_pand,
                                 columns = [
                                         'Estatura (cm)',
                                         'Peso (kg)',
                                         'Edad (anios)'],
                                 index = [
                                         'Andrea',
                                         'Guiomar'])
df1.index=['Andrea','Guiomar']

df1.columns=['A','B','C','D','E']
