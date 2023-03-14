# Importamos las librerías necesarias
import argparse
import pandas as pd

# Se define el objeto para procesar los argumentos de línea de comandos.
parser = argparse.ArgumentParser()
parser.add_argument("--tag", type=str, required=True,
                    help="Tag to filter on")

args = parser.parse_args()
# Se asignan los valores de los argumentos a las variables correspondientes.
tag = args.tag

# Leer el conjunto de datos desde el archivo CSV
df = pd.read_csv(f"../../output/load/chaturbate-{tag}.csv")