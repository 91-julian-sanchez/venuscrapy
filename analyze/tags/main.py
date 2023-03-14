# Importamos las librerías necesarias
import argparse
import pandas as pd
from analyze.filter import filter_dataframe
from most_popular import run
from plots import build_plot
# Se define el objeto para procesar los argumentos de línea de comandos.
parser = argparse.ArgumentParser()
parser.add_argument("--tag", type=str, required=True,
                    help="Tag to filter on")
parser.add_argument("--hours", type=str, 
                        default=4000,
                    help="Tag to filter on")

args = parser.parse_args()
# Se asignan los valores de los argumentos a las variables correspondientes.
tag = args.tag
hours = args.hours
# Leemos el archivo CSV en un DataFrame
df = filter_dataframe(pd.read_csv(f'../../output/load/chaturbate-{tag}.csv'), hours=hours)
new_df = run(df)
build_plot(new_df)
