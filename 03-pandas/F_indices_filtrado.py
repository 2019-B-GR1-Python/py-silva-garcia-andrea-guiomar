# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:54 2019

@author: Asus
"""

import pandas as pd

path_guardar_bin ="C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//03-pandas//Data//artwork_data_completo.pikle"

df = pd.read_pickle(path_guardar_bin)

serie_artistas_repetidos=df["artist"]

artistas= pd.unique(serie_artistas_repetidos)

artistas.size
len(artistas)

blake=df["artist"] == "Blake, William"

df["artist"].value_counts()

df_blake= df[blake]