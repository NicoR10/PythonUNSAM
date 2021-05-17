import pandas as pd

df = pd.read_csv('Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

dh = df['12-25-2014':].copy()

diferencia = dh['H_SF'] - dh['H_BA']

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
# Calculo el promedio para hallar delta_h
delta_h = diferencia.sum()/len(diferencia) # diferencia de los ceros de escala entre ambos puertos

pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()