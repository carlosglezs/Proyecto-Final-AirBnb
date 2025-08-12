import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer



def procesar_df(df, fecha_inicio_str, columna_fecha):
    """
    Filtra los datos para que no colapesen con los del dataframe siguiente y sean trimestrales y además calcula:
    el ingreso medio por día que está ocupado, el porcentaje de ocupación y los ingresos totales durante el trimestre
    df: DataFrame de pandas a analizar.
    fecha_inicio_str: el primer registro del dataset
    columna_fecha: tres meses después del primer registro del dataset

    """
    fecha_inicio = pd.Timestamp(fecha_inicio_str)
    fecha_fin = fecha_inicio + pd.DateOffset(months=3)
    dias_trimestre = (fecha_fin - fecha_inicio).days

    # Convertir la columna de fecha a datetime estándar
    df['date'] = pd.to_datetime(df[columna_fecha], errors='coerce')

    # Filtrar al trimestre exacto
    df = df[(df['date'] >= fecha_inicio) & (df['date'] < fecha_fin)].copy()

    # Limpieza básica
    df['available'] = df['available'].astype(str).str.lower()
    df['price'] = (
        df['price'].astype(str)
          .str.replace(r'[^0-9.]', '', regex=True)
          .replace('', '0')
          .astype(float)
    )

    trimester = fecha_inicio.to_period('Q').strftime('%YQ%q')
    df['trimester'] = trimester

    # Filtrar ocupados
    df_ocupado = df[df['available'] == 'f'].copy()

    # Resumen por ID
    resumen = df_ocupado.groupby(['listing_id', 'trimester']).agg(
        busy_days=('available', 'count'),
        income=('price', 'sum')
    ).reset_index()

    resumen['avg_day'] = (resumen['income'] / resumen['busy_days']).round(2)
    resumen['occupancy_rate'] = (resumen['busy_days'] / dias_trimestre * 100).round(2)
    resumen['income'] = resumen['income'].round(2)

    print(f"✅ Resumen generado ({trimester}): {len(resumen)} registros, desde {fecha_inicio.date()} hasta {(fecha_fin - pd.Timedelta(days=1)).date()}")

    return resumen


def eda_preliminar(df):
    """
    Realiza un análisis exploratorio preliminar del DataFrame.
    df: DataFrame de pandas a analizar.
    """

    import pandas as pd
    
    # Mostrar todas las columnas temporalmente
    with pd.option_context('display.max_columns', None):
        display(df.sample(5))

        print('-----------------')

        print('INFO')
        display(df.info())

        print('-----------------')

        print('NULOS')
        display(round(df.isnull().sum() / df.shape[0] * 100, 2))

        print('-----------------')

        print('DUPLICADOS')
        print(df.duplicated().sum())

        print('-----------------')

        print('VALUE COUNTS')
        for col in df.select_dtypes(include='O').columns:
            print(df[col].value_counts())
            print('----------------------------')

def valores_minus(df):
    """
    Convierte todos los valores en columnas categóricas a minúsculas."
    df: "DataFrame con columnas tipo objeto.
    """
    for col in df.select_dtypes(include='O').columns:
        df[col] = df[col].str.lower()

def calcular_nulos(df):
    """
    Calcula el número y porcentaje de valores nulos por columna."
    df: DataFrame a evaluar.
    """
    numero_nulos = df.isnull().sum() 
    porcentaje_nulos = (df.isnull().sum() / df.shape[0]) * 100
    return numero_nulos, porcentaje_nulos

def subplot_col_num(dataframe, col):
    """
    Genera histogramas y boxplots para columnas numéricas.
    Muestra líneas y etiquetas de los límites de outliers, ajustando el eje X para mejor visualización.
    dataframe: DataFrame a evaluar.
    col: columnas que van a ser afectadas
    """
    num_graph = len(col)
    num_rows = (num_graph + 2) // 2

    fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows * 5))

    for i, column in enumerate(col):
        sns.histplot(data=dataframe, x=column, ax=axes[i, 0], bins=200)
        axes[i, 0].set_title(f"Distribución de {column}")
        axes[i, 0].set_ylabel("Frecuencia")

        sns.boxplot(data=dataframe, x=column, ax=axes[i, 1])
        axes[i, 1].set_title(f"Boxplot de {column}")

        # Cálculo de límites de outliers
        Q1 = dataframe[column].quantile(0.25)
        Q3 = dataframe[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Cantidad de outliers
        outliers = dataframe[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound)][column]
        num_outliers = outliers.count()

        # Línea y etiqueta de límites
        axes[i, 1].axvline(lower_bound, color='red', linestyle='--')
        axes[i, 1].axvline(upper_bound, color='red', linestyle='--')

        axes[i, 1].text(lower_bound, 0.02, f"{lower_bound:.2f}", color='red', rotation=90,
                        ha='right', va='bottom', transform=axes[i, 1].get_xaxis_transform())
        axes[i, 1].text(upper_bound, 0.02, f"{upper_bound:.2f}", color='red', rotation=90,
                        ha='left', va='bottom', transform=axes[i, 1].get_xaxis_transform())

        # Mostrar número total de outliers
        axes[i, 1].text(Q3, 0.2, f"Outliers: {num_outliers}", color='darkred', fontsize=10,
                        transform=axes[i, 1].get_xaxis_transform())

        # Ajustar eje X para no mostrar outliers extremos que aplastan la escala
        p99 = dataframe[column].quantile(0.99)
        axes[i, 1].set_xlim(left=dataframe[column].min(), right=p99)

    plt.tight_layout()
    plt.show()

def print_outlier_limits(dataframe, col):
    """
    Imprime los límites inferiores y superiores de outliers para cada columna numérica.
    dataframe: DataFrame a evaluar.
    col: columnas que van a ser afectadas
    """
    print("Límites de outliers por variable:\n")
    for column in col:
        Q1 = dataframe[column].quantile(0.25)
        Q3 = dataframe[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        print(f"- {column}:")
        print(f"   Límite inferior: {lower_bound:.2f}")
        print(f"   Límite superior: {upper_bound:.2f}\n")

def outliers_derecha(data,columnas):
    """
    Muestra la cantidad y porcentaje de outliers por columna (valores superiores a un umbral).
    data: DataFrame de entrada.
    columnas: Diccionario con nombre de columna como clave y umbral como valor.
    """
    for col, out in columnas.items():
        outliers = data[col] [data[col]>out].count()
        print(f"para la columna {col.upper()} tenemos {outliers}, lo que representa un {round(outliers/data.shape[0]*100,4)}%")   

def outliers_izquierda(data,columnas):
    """
    Muestra la cantidad y porcentaje de outliers por columna (valores inferiores a un umbral).
    data: DataFrame de entrada.
    columnas: Diccionario con nombre de columna como clave y umbral como valor.
    """
    for col, out in columnas.items():
        outliers = data[col] [data[col]<out].count()
        print(f"para la columna {col.upper()} tenemos {outliers}, lo que representa un {round(outliers/data.shape[0]*100,4)}%") 

def calcular_solo_col_nul(dataframe, umbral = 10):
    """
    Identifica columnas con valores nulos y las separa por umbral.
    dataframe: DataFrame a evaluar.
    umbral: Porcentaje límite para diferenciar columnas con pocos o muchos nulos.
    """
    columns_with_nulls = dataframe.columns[dataframe.isnull().any()]
    nulls_columns_info = pd.DataFrame({
        "Column":columns_with_nulls,
        "Datatype":[dataframe[col].dtype for col in columns_with_nulls],
        "NullCount":[dataframe[col].isnull().sum() for col in columns_with_nulls],
        "Null%":[((dataframe[col].isnull().sum() / dataframe.shape[0]) * 100)for col in columns_with_nulls]
    })

    display (nulls_columns_info)
    high_nulls_cols = nulls_columns_info[nulls_columns_info['Null%']> umbral] ['Column'].tolist()
    low_nulls_cols = nulls_columns_info[nulls_columns_info['Null%']<= umbral] ['Column'].tolist()
    return high_nulls_cols, low_nulls_cols

def subplot_col_num(dataframe,col):
    """
    Genera histogramas y boxplots para columnas numéricas.
    dataframe: DataFrame de entrada.
    col: Lista de columnas numéricas a graficar.
    """

    num_graph = len(col)
    num_rows = (num_graph + 2) // 2

    fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows*5 ))

    for i, col in enumerate(col):
        sns.histplot(data=dataframe, x=col, ax = axes[i,0], bins = 200)
        axes[i,0].set_title(f"Distriucion de {col}")
        axes[i,0].set_ylabel("frecuencia")

        sns.boxplot(data=dataframe, x=col, ax = axes[i,1])
        axes[i,1].set_title(f"Boxplot de {col}")

    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

def imputar_iterative(data, lista_columnas):
    """
    Imputa valores nulos con imputación iterativa y agrega columnas con sufijo '_iterative'."
    data: DataFrame con valores faltantes.
    lista_columnas: Columnas a imputar.
    """
    iter_imputer = IterativeImputer(max_iter=50, random_state=42)
    data_imputed = iter_imputer.fit_transform(data[lista_columnas])
    new_col = [col + "_iterative" for col in lista_columnas]

    data[new_col] = data_imputed
    display(data[new_col].describe().T)
    return data, new_col        


def plot_boolean_vars_impact(df, bool_vars, target='price_person'):
    """
    Muestra gráfico de barras comparando el promedio del target ('price_person') y
    la cantidad de registros cuando cada variable booleana es True o False.
    
    df : DataFrame que contiene los datos.
    bool_vars : Lista de columnas booleanas (True/False).
    target : Columna numérica a analizar (default='price_person').
    """
    summary = []

    for col in bool_vars:
        # Verificamos que la columna exista y tenga valores booleanos
        if col in df.columns and df[col].dropna().isin([True, False]).all():
            grouped = df.groupby(col)[target].agg(['mean', 'count']).reset_index()
            grouped['variable'] = col
            grouped['value'] = grouped[col]
            summary.append(grouped[['variable', 'value', 'mean', 'count']])
        else:
            print(f"Omitida: '{col}' no existe o no es booleana.")

    if not summary:
        print("⚠️  Ninguna variable válida para graficar.")
        return

    result = pd.concat(summary)

    plt.figure(figsize=(14, len(result['variable'].unique()) * 0.65 + 3))
    ax = sns.barplot(data=result, x='mean', y='variable', hue='value', palette='Set2')

    for bar in ax.patches:
        width = bar.get_width()
        y = bar.get_y() + bar.get_height() / 2
        ax.text(width + 1, y, f"{width:.0f} €", va='center', ha='left', fontsize=9, color='black')

    plt.title("Promedio de 'price_person' por variable booleana", fontsize=14)
    plt.xlabel("Promedio de price_person (€)")
    plt.ylabel("Variable booleana")
    plt.legend(title='Valor')
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def boolean_summary_table(df, bool_vars, target='price_person'):
    """
    Devuelve una tabla con:
    - Cantidad y porcentaje de True y False por variable.
    - Promedio del target ('price_person') para cada grupo.
    
    df : DataFrame con los datos.
    bool_vars : Lista de columnas booleanas.
    target : Columna numérica para el cálculo del promedio.
    """

    rows = []

    for col in bool_vars:
        if col in df.columns and df[col].dropna().isin([True, False]).all():
            counts = df[col].value_counts()
            total = counts.sum()
            percents = counts / total * 100
            means = df.groupby(col)[target].mean()
            rows.append({
                'Variable': col,
                'True (n)': counts.get(True, 0),
                'True (%)': round(percents.get(True, 0), 1),
                'False (n)': counts.get(False, 0),
                'False (%)': round(percents.get(False, 0), 1),
                'Promedio True (€)': round(means.get(True, 0), 2),
                'Promedio False (€)': round(means.get(False, 0), 2)
            })

    return pd.DataFrame(rows)

