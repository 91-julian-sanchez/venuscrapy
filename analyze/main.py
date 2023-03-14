import argparse
import pandas as pd
from filter import filter_dataframe
from tags.most_popular import run as tags_most_popular
from tags.plots import build_plot
from viewers.hourly_viewers import run as hourly_viewers
from viewers.plots import build_plot as hourly_viewers_plot
from bokeh.io import show
from bokeh.layouts import column

# Se define el objeto para procesar los argumentos de línea de comandos.
parser = argparse.ArgumentParser()
parser.add_argument("--tag", type=str, required=True,
                    help="Tag to filter on")
parser.add_argument("--hours", type=str, 
                        default=3000,
                    help="Tag to filter on")
args = parser.parse_args()
# Se asignan los valores de los argumentos a las variables correspondientes.
tag = args.tag
hours = args.hours

# Cargue su dataframe
df = filter_dataframe(pd.read_csv(f"../output/load/chaturbate-{tag}.csv"), hours=hours)
#tags
tags_most_popular_df = tags_most_popular(df, tag)
tags_most_popular_df_plot= build_plot(tags_most_popular_df)
#viewers
hourly_viewers_df = hourly_viewers(df)
hourly_viewers_df_plot = hourly_viewers_plot(hourly_viewers_df)

#visualizate
show(column(tags_most_popular_df_plot, hourly_viewers_df_plot))

# ****** Calcular la correlación
# El valor de correlación varía entre -1 y 1, donde -1 indica una correlación negativa fuerte, 1 indica una correlación positiva fuerte y 0 indica una falta de correlación.
# Si la correlación es positiva y cercana a 1, significa que a medida que aumenta la edad, también aumentan las impresiones. 
# Si la correlación es negativa y cercana a -1, significa que a medida que aumenta la edad, disminuyen las impresiones. 
# Si la correlación es cercana a 0, significa que no hay una relación clara entre las dos variables.

correlation = df['age'].corr(df['impression'])
print("La correlación entre edad e impresiones es:", correlation)

correlation = df['viewers'].corr(df['impression'])
print("La correlación entre espectadores e impresiones es:", correlation)

correlation = df['time'].corr(df['impression'])
print("La correlación entre tiempo de transmisión e impresiones es:", correlation)