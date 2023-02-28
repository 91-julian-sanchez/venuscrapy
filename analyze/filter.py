# Importamos las librerías necesarias
import pandas as pd
from datetime import datetime, timedelta

# Definimos una función para generar el rango de fechas
# Por defecto, el rango es de 0 horas (es decir, el momento actual)
# strftime es el formato en el que se devolverá la fecha
def generate_date_range(hours, strftime='%Y-%m-%d_%H-%M-%S'):
    # Obtenemos la fecha y hora actuales
    now = datetime.today()
    # Calculamos la fecha y hora de inicio restando las horas indicadas en la función
    date_range_start = now - timedelta(hours=hours)
    # Devolvemos la fecha y hora de inicio y la fecha y hora actuales en el formato indicado
    return date_range_start.strftime(strftime), now.strftime(strftime)

def filter_dataframe(df, hours=24):
    # Llamamos a la función para generar el rango de fechas de las últimas 24 horas
    date_range_start, date_range_end = generate_date_range(hours)

    # Imprimimos el mensaje con el rango de fechas que se utilizará para filtrar los datos
    print(f"Traer registros para date: (df['date'] >= {date_range_start}) & (df['date'] < {date_range_end})")

    # Filtramos los datos por el rango de fechas
    return df.loc[(df['date'] >= date_range_start) & (df['date'] < date_range_end) ]
