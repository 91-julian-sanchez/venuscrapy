import pandas as pd

def run(df, tag):
    # Imprimimos un resumen de los datos filtrados
    print(df.info())

    # Crear un nuevo DataFrame con las columnas hashtag, viewers, impression y age
    new_df = pd.DataFrame(columns=['hashtag', 'viewers', 'impression', 'age'])
    # Iterar por cada fila del DataFrame original
    for index, row in df.iterrows():
        # Verificar si la columna 'tags' no es nula
        if not pd.isnull(row['tags']):
            # Separar el valor de la columna de etiquetas (tags) en una lista de hashtags
            hashtags = row['tags'].split(',')
            # Iterar por cada hashtag en la lista
            for hashtag in hashtags:
                # Buscar si el hashtag ya está en el nuevo DataFrame
                hashtag_row = new_df.loc[new_df['hashtag'] == hashtag]
                # Si el hashtag no está en el nuevo DataFrame, agregar una nueva fila
                if hashtag_row.empty:
                    new_df = new_df.append({'hashtag': hashtag, 'viewers': row['viewers'], 'impression': row['impression'], 'age': row['age'], 'count': 1}, ignore_index=True)
                # Si el hashtag ya está en el nuevo DataFrame, actualizar las columnas existentes
                else:
                    hashtag_index = hashtag_row.index[0]
                    new_df.at[hashtag_index, 'viewers'] += row['viewers']
                    new_df.at[hashtag_index, 'impression'] += row['impression']
                    new_df.at[hashtag_index, 'age'] += row['age']
                    new_df.at[hashtag_index, 'count'] += 1

    # Calcular el promedio de edad para cada hashtag
    new_df['age'] = new_df['age'] / new_df['count']

    # Eliminar la columna "count" ya que ya no es necesaria
    new_df = new_df.drop(columns=['count'])

    # Eliminar la fila que contiene el hashtag "#happy"
    new_df = new_df.drop(new_df[new_df['hashtag'] == tag].index)

    print(new_df)

    # Seleccionar las columnas de hashtag y viewers del DataFrame
    hashtag_viewer_df = new_df[['hashtag', 'viewers']]

    # Convertir el DataFrame a un array de numpy
    hashtag_viewer_array = hashtag_viewer_df.to_numpy()

    # Imprimir el array
    print(hashtag_viewer_array)
    return new_df