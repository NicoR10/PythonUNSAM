# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:59:14 2020

@author: valer
"""

import os
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
directorio='C:/Users/nykko_000/Desktop/Programacion/PythonUNSAM/ejercicios_python/Data' #elijo el directorio

#armos el dataframe para los arboles de los parques
archivo='arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio, archivo)
dv = pd.read_csv(fname)
cols_sel = ['nombre_cientifico','diametro_altura_pecho','altura_arbol']#selecciono las columnas deseadas
dTTv = dv[dv['nombre_cientifico']=='Tipuana tipu'][cols_sel].copy()#elijo la especie
dTTv.rename(columns={'altura_arbol': 'altura', 'diametro_altura_pecho': 'DAP'}, inplace=True)
dTTv['Ambiente']='vereda'

#armos el dataframe para los arboles de las veredas
parque='arbolado.csv'
file = os.path.join(directorio,parque)
dp = pd.read_csv(file)
cols_sel = ['nombre_cie','diametro','altura_tot']#selecciono las columnas deseadas
dTTp = dp[dp['nombre_cie']=='Tipuana Tipu'][cols_sel].copy()#elijo la especia
dTTp.rename(columns={'altura_tot': 'altura', 'diametro': 'DAP'}, inplace=True)
dTTp['Ambiente']='parque'

#junto los dataframes
dTT = pd.concat([dTTv, dTTp])
#%%
#grafico boxplot para los diametros
sns.boxplot(data=dTT,y='DAP',x='Ambiente',palette="pastel").set_title("DAP para Tipuana Tipu")
plt.figure()
#grafico boxplot para las alturas
sns.boxplot(data=dTT,y='altura',x='Ambiente',palette="pastel").set_title("Altura para Tipuana Tipu")



#Para cambiar de especie deberia modificar dos lineas de código, conviene hacer una f(x)
