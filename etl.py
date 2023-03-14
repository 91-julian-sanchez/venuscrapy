import pandas as pd
import argparse
import os
# Se define el objeto para procesar los argumentos de línea de comandos.
parser = argparse.ArgumentParser()
parser.add_argument("--tag", type=str, required=True,
                    help="Tag to filter on")
parser.add_argument("--timestamp", type=str, required=True,
                    help="Timestamp of the data in the input file")
args = parser.parse_args()

# Se asignan los valores de los argumentos a las variables correspondientes.
tag = args.tag
timestamp = args.timestamp

# Función para ordenar los datos según la cantidad de espectadores y la edad de los modelos.
def sort(df):
    df = df.sort_values(by=[ 'viewers','age'], ascending=False)
    return df
 
# Función para agrupar los datos por las columnas especificadas, obteniendo el máximo valor de 'time' y 'viewers', y uniendo los hashtags.
def group_by(df, columns):
    return df.groupby(columns).agg({ 'time': 'max', 'viewers': 'max', 'tags': lambda x: ','.join(set(str(i) for i in x)), "page": lambda x: tuple(x) })

# Función para agregar una columna con el número de páginas vistas para cada modelo.
def group_pages(df):
    df = df.rename(columns={"page":"pages"})
    df["pages"] = df["pages"].apply(lambda x: str(x))
    df["impression"] = df["pages"].apply(lambda x: len(x.split(",")))
    return df
  
# Leer el archivo CSV
df = pd.read_csv(f'output/extract/chaturbate-{tag}-{timestamp}.csv')
df = group_by(df, ["model","age","gender","link"])
df = group_pages(df)
df = sort(df)
df['tags'] = df['tags'].str.replace('#', '')
df['date'] = timestamp

# Se guarda el DataFrame resultante en un archivo CSV.
output_dir = 'output/transform'
os.makedirs(output_dir, exist_ok=True)
df.to_csv(f'output/transform/chaturbate-{tag}-{timestamp}.csv')