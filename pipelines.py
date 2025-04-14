#Usando pipelines para limpieza de datos
import pandas as pd
import numpy as np

#Implementar pipelines
#df = pd.read_csv("dataset_1.csv", index_col = 0)

#remover nulos usando funcion
def remove_negative_Values(df,column):
    df[column] = df[column].apply(lambda x: np.nan if x <0 else x)
    return df

#remover outlayers usndo funcion
def remove_outliers_with_zscore(df,column,threshold=2):
    column_mean = df[column].mean()
    column_std = df[column].std()
    df[column] =  df[column].mask(((df[column] - column_mean)/ column_std).abs()>threshold, column_mean)
    return df

#funcion para mapear datos
def map_column_values(df,column, mapping_dict):
    df[column] = df[column].apply(lambda value: mapping_dict.get(value.lower().strip(),np.nan) if value is not np.nan else np.nan)
    return df

#funcion para rellenar vacíos
def fill_na_in_column(df,column,fill_value):
    df[column].fillna(fill_value, inplace=True)
    return df

def preprocess_data(df):
    # Mapeo de datos
    education_mapping = {
        "Bachelors":"Bachelor",
        "mastre":"Master",
        "pHd":"PhD",
        "no education":"NE"
    }

    #mapeo de generos
    gender_mapping = {
        "m" : "M",
        "f":"F"
    }
    #TUBERÍA
    return(
        #remover negativos
        df.pipe(remove_negative_Values,"Edad")
        .pipe(remove_negative_Values,"Ingresos")
        .pipe(remove_negative_Values,"Hijos")
        #remover outliers
        .pipe(remove_outliers_with_zscore,"Edad")
        .pipe(remove_outliers_with_zscore,"Ingresos")
        .pipe(remove_outliers_with_zscore,"Altura")
        .pipe(remove_outliers_with_zscore,"Hijos")
        #mapear
        .pipe(map_column_values,"Nivel_Educación", education_mapping)
        .pipe(map_column_values,"Género", gender_mapping)
        #rellenar nulos
        .pipe(fill_na_in_column,"Ciudad", "Desconocido")
        .pipe(fill_na_in_column,"Nivel_Educación", "Desconocido")
        .pipe(fill_na_in_column,"Género", "Desconocido")
        .pipe(fill_na_in_column,"Edad", df["Edad"].median())
        .pipe(fill_na_in_column,"Hijos", df["Hijos"].median())
        .pipe(fill_na_in_column,"Ingresos", df["Ingresos"].mean())
        .pipe(fill_na_in_column,"Edad", df["Edad"].mean())
    )
    
#instanciar    
df = pd.read_csv("datasets/dataset_1.csv", index_col = 0)
print(df)

df = preprocess_data(df)
print(df)