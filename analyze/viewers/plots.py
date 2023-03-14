
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn

def build_table(df):
    # Ordenar el DataFrame por la columna 'viewers' en orden descendente
    df = df.sort_values('viewers', ascending=False)

    # Crear una fuente de datos a partir del DataFrame
    source = ColumnDataSource(df)

    # Crear las columnas de la tabla
    columns = [TableColumn(field="hour", title="Hour"), TableColumn(field="viewers", title="Viewers"),]
    
    # Crear la tabla utilizando DataTable
    return DataTable(source=source, columns=columns, width=400, height=400)
    
def build_plot(df):
   return build_table(df)

    