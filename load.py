import os
import pandas as pd

# Ruta de la carpeta que contiene los archivos CSV
path = './output/transform'

# Lista para almacenar los dataframes
dfs = []

# Recorremos todos los archivos de la carpeta "transform"
for filename in os.listdir(path):
    # Verificamos que sea un archivo CSV
    if filename.endswith('.csv'):
        # Leemos el archivo CSV y lo agregamos a la lista de dataframes
        df = pd.read_csv(os.path.join(path, filename))
        dfs.append(df)

# Unimos todos los dataframes en uno solo
merged_df = pd.concat(dfs, ignore_index=True)
df = merged_df[['model','age','gender','link','time','viewers','tags','impression','date']]
# Guardamos el dataframe unido en un archivo CSV
df.to_csv('output/load/latina.csv', index=False)