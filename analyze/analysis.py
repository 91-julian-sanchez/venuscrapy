# El valor de correlación varía entre -1 y 1, donde -1 indica una correlación negativa fuerte, 1 indica una correlación positiva fuerte y 0 indica una falta de correlación.

# Si la correlación es positiva y cercana a 1, significa que a medida que aumenta la edad, también aumentan las impresiones. 
# Si la correlación es negativa y cercana a -1, significa que a medida que aumenta la edad, disminuyen las impresiones. 
# Si la correlación es cercana a 0, significa que no hay una relación clara entre las dos variables.

import pandas as pd

# Cargue su dataframe
df = pd.read_csv("../output/load/latina.csv")

# Calcular la correlación entre las dos columnas
correlation = df['age'].corr(df['impression'])

print("La correlación entre edad e impresiones es:", correlation)

# Calcular la correlación entre las dos columnas
correlation = df['viewers'].corr(df['impression'])

print("La correlación entre espectadores e impresiones es:", correlation)

# Calcular la correlación entre las dos columnas
correlation = df['time'].corr(df['impression'])

print("La correlación entre tiempo de transmisión e impresiones es:", correlation)