import pandas as pd
import os

directorio = 'Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
parques_path = os.path.join(directorio, archivo_parques)
veredas_path = os.path.join(directorio, archivo_veredas)
df_parques = pd.read_csv(parques_path)
df_veredas = pd.read_csv(veredas_path)

df_tipas_parques = df_parques[df_parques['nombre_com'] == 'Tipa blanca'].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'].copy()

df_tipas_parques = df_tipas_parques.rename(columns={"altura_tot": "altura"})
df_tipas_veredas = df_tipas_veredas.rename(columns={"altura_arbol": "altura", "diametro_altura_pecho": "diametro"})

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura',by = 'ambiente')