
from bokeh.models import ColumnDataSource
from bokeh.io import show
from bokeh.layouts import column
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.io import show
from bokeh.models import Div
from bokeh.layouts import column

def build_table(df):
    # Ordenar el DataFrame por la columna 'viewers' en orden descendente
    df = df.sort_values('viewers', ascending=False)

    # Crear una fuente de datos a partir del DataFrame
    source = ColumnDataSource(df)

    # Crear las columnas de la tabla
    columns = [TableColumn(field="hashtag", title="Hashtag"),
            TableColumn(field="viewers", title="Viewers"),
            TableColumn(field="impression", title="Impression"),
            TableColumn(field="age", title="Age")]
    
    # Crear la tabla utilizando DataTable
    return DataTable(source=source, columns=columns, width=400, height=400)
    
# def wordcloud(df):
# from wordcloud import WordCloud
#     # Crear una lista de tuplas (hashtag, viewers) a partir del DataFrame
#     hashtag_viewers = [(row["hashtag"], row["viewers"]) for index, row in df.iterrows()]

#     # Crear la nube de palabras y guardarla en un archivo
#     wordcloud = WordCloud(width=400, height=200, background_color="white").generate_from_frequencies(dict(hashtag_viewers))
#     wordcloud.to_file("wordcloud.png")

#     # Crear una imagen de la nube de palabras
#     image = Div(text='<img src="wordcloud.png">')

#     # Mostrar la imagen en un layout
#     show(column(image))
    

def buildPlot(df):
   table = build_table(df)
   show(column(table))
#    show(column(table, image))

    