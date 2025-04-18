#Label encoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.DataFrame({
    "Cargo": ["gerente","analista","asistente", "gerente","analista","asistente"],
    "Departamento":["ventas","marketing","RRHh","vetnas","markting","RRHh"],
    "Ubicacion":["norte","sir","este","oeste","norte","sur"]
})
print(df)

model = LabelEncoder()
df["Cargo"]=model.fit_transform(df["Cargo"])
df["Departamento"]=model.fit_transform(df["Departamento"])
df["Ubicacion"]=model.fit_transform(df["Ubicacion"])
print(df)

#Encoder similar usando de manera Ordinal - simple line
from sklearn.preprocessing import OrdinalEncoder

model = OrdinalEncoder()
df_oe = df.copy()
df_oe[["Cargo","Departamento","Ubicacion"]] = model.fit_transform(df_oe[["Cargo","Departamento","Ubicacion"]])
print(df_oe)

#label encode
def label_encode(df,columns):
    for column in columns:
        unique_values = df[column].unique()
        value_to_int = {value: i for i, value in enumerate(unique_values)}
        df[column + "_encoded"]= df[column].replace(value_to_int)
    return df

df_label_custom = label_encode(df,["Cargo","Departamento","Ubicacion"])
print(df_label_custom)