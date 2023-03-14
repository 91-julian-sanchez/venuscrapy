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

# Convertir la columna 'date' en tipo datetime y extraer la columna 'viewers'
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d_%H-%M-%S')
df['viewers'] = pd.to_numeric(df['viewers'], errors='coerce')

# Crear una nueva columna 'hour' que representa la hora del día para cada fila
df['hour'] = df['date'].dt.hour

# Crear una lista de las horas del día en las que estamos interesados
hours_of_interest = list(range(0, 24))

# Crear un diccionario para almacenar el número total de espectadores para cada hora del día
hourly_viewers = {}

# Iterar sobre las horas del día y calcular el número total de espectadores para cada hora
for hour in hours_of_interest:
    mask = (df['hour'] == hour)
    hourly_viewers[f"{hour:02d}-{hour+1:02d}"] = df[mask]['viewers'].sum()

# Imprimir el resultado
print(hourly_viewers)
max_viewers = max(hourly_viewers.values())
# max_viewers_hour = None
# for hour_range, total_viewers in hourly_viewers.items():
#     print(f"{hour_range}: {total_viewers} viewers.")
#     if total_viewers == max_viewers:
#         max_viewers_hour = hour_range
# print(f"El rango horario {max_viewers_hour} tuvo la máxima cantidad de espectadores: {max_viewers}.")
df = pd.DataFrame(list(hourly_viewers.items()), columns=['Hour', 'viewers'])
# Ordenar el DataFrame por la columna 'viewers' en orden descendente
df = df.sort_values('viewers', ascending=False)
print(df)