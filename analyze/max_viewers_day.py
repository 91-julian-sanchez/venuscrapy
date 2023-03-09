import pandas as pd

# Leer el conjunto de datos desde el archivo CSV
df = pd.read_csv("../output/load/latina.csv")

# Convertir la columna 'date' en tipo datetime y extraer la columna 'viewers'
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d_%H-%M-%S')
df['viewers'] = pd.to_numeric(df['viewers'], errors='coerce')

# Calcular el número total de espectadores para cada día
df['day'] = df['date'].dt.date
daily_viewers = df.groupby('day')['viewers'].sum()
print(daily_viewers)

# Encontrar el día con la mayor cantidad de espectadores en total
max_viewers_day = daily_viewers.idxmax()

print(f"El día con más espectadores en total fue {max_viewers_day} con {daily_viewers[max_viewers_day]} espectadores en total.")
