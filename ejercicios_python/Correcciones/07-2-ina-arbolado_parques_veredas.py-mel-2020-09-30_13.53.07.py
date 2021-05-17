# -*- coding: utf-8 -*-
""" Created on Tue Sep 29 13:33:27 2020 @author: Melina P. Bordone """

import pandas as pd
import os

directorio = 'Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'

parques_path = os.path.join(directorio, archivo_parques)
veredas_path = os.path.join(directorio, archivo_veredas)

#Abrimos las dataframes
df_parques = pd.read_csv(parques_path)
df_veredas = pd.read_csv(veredas_path)

#Copiamos y armamos un df de las tipas y sus diametros a la altura del pecho
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu']['diametro'].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu']['diametro_altura_pecho'].copy()

#Renombramos diametro del df_tipas_parques para que se llame igual que en el df_tipas_veredas
df_tipas_parques = df_tipas_parques.rename("diametro_altura_pecho")  

#Agregar una columna llamada 'ambiente' 
#1ro. Creo una nueva serie para cada dataframe con la cantidad de filas adecuada para cada una
    #Para saber la cantidad de filas puedo hacer
#df_tipas_parques.describe()
#df_tipas_veredas.describe()
#    #Otra forma 
#len(df_tipas_parques) #Res: 4031  que es igual al len(df_tipas_parques.index)
#len(df_tipas_veredas) #Res:9330

serie_parque = pd.Series(['parque']*len(df_tipas_parques.index), index = df_tipas_parques.index) #seteo los indices para que se mantengan
serie_vereda = pd.Series(['vereda']*len(df_tipas_veredas.index), index = df_tipas_veredas.index)

#2do. Renombro la serie creada
serie_parque = serie_parque.rename('ambiente')
serie_vereda = serie_vereda.rename('ambiente')

#3ro. Concatenar las series creadas a df_tipas_parques o df_tipas_veredas
df_tipas_parques = pd.concat([df_tipas_parques, serie_parque], axis=1) #axis = 1 para que concatene horizontalmente en columnas
df_tipas_veredas = pd.concat([df_tipas_veredas, serie_vereda], axis=1)

#Juntamos ambos datasets
df_tipas = pd.concat([df_tipas_parques, df_tipas_veredas], axis=0)

#Creamos boxplot
df_tipas.boxplot('diametro_altura_pecho', by = 'ambiente')

#-------------------------------------------------------------------------------------
#Lo mismo para las alturas
df_tipas_parques = df_parques[df_parques['nombre_cie']== 'Tipuana Tipu']['altura_tot'].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico']== 'Tipuana tipu']['altura_arbol'].copy()

df_tipas_parques = df_tipas_parques.rename("altura_arbol")

serie_parque = pd.Series(['parque']*len(df_tipas_parques.index), index = df_tipas_parques.index) #seteo los indices para que se mantengan
serie_vereda = pd.Series(['vereda']*len(df_tipas_veredas.index), index = df_tipas_veredas.index)
serie_parque = serie_parque.rename('ambiente')
serie_vereda = serie_vereda.rename('ambiente')
df_tipas_parques = pd.concat([df_tipas_parques, serie_parque], axis=1) #axis = 1 para que concatene horizontalmente en columnas
df_tipas_veredas = pd.concat([df_tipas_veredas, serie_vereda], axis=1)

df_tipas = pd.concat([df_tipas_parques, df_tipas_veredas], axis=0)
df_tipas.boxplot('altura_arbol', by = 'ambiente')
  
#---------------------------------------------------------------------------------------
# Si se quisiera repetir para otras especies se podria definir una funcion

def hacer_boxplot(df_1, df_2, columna_1, columna_2, filtro):
    '''Genera un boxplot comparando la columna_1 de dos df (filtrada con filtro) en funcion de la columna 2.
    Precondicion: columna 1: cualitativa y columna 2: cuantitativa. 
                  Ambas columnas deben llamarse igual en los dos df, se pasan como str.
                  Filtro a aplicar en columna_1: filtro (pasado como str) debe llamarse igual en los dos df
                  Ej: hacer_boxplot(df_parques, df_veredas, 'nombre_cientifico', 'altura_arbol', 'Tipuana Tipu') 
    Postcondicion: devuelve un grafico tipo boxplot.'''
    df_arbol_parques = df_1[df_1[columna_1]== filtro][columna_2].copy()
    df_arbol_veredas = df_veredas[df_veredas[columna_1]== filtro][columna_2].copy()
    serie_parque = pd.Series(['parque']*len(df_arbol_parques.index), index = df_arbol_parques.index) #seteo los indices para que se mantengan
    serie_vereda = pd.Series(['vereda']*len(df_arbol_veredas.index), index = df_arbol_veredas.index)
    serie_parque = serie_parque.rename('ambiente')
    serie_vereda = serie_vereda.rename('ambiente')
    df_arbol_parques = pd.concat([df_arbol_parques, serie_parque], axis=1) #axis = 1 para que concatene horizontalmente en columnas
    df_arbol_veredas = pd.concat([df_arbol_veredas, serie_vereda], axis=1)
    df_arbol = pd.concat([df_arbol_parques, df_arbol_veredas], axis=0)
    df_arbol.boxplot(columna_2, by = 'ambiente')
    
    

