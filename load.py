import pandas as pd
import argparse
import os
# Se define el objeto para procesar los argumentos de línea de comandos.
parser = argparse.ArgumentParser()
parser.add_argument("--tag", type=str, required=True,
                    help="Tag to filter on")
args = parser.parse_args()

# Se asignan los valores de los argumentos a las variables correspondientes.
tag = args.tag

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
output_dir = 'output/load'
os.makedirs(output_dir, exist_ok=True)
df.to_csv(f'output/load/{tag}.csv', index=False)