#Data encoding - usando OneHotEncoder para One-Hot encoding
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({
    "Cargo": ["gerente","analista","asistente", "gerente","analista","asistente"],
    "Departamento":["ventas","marketing","RRHh","vetnas","markting","RRHh"],
    "Ubicacion":["norte","sir","este","oeste","norte","sur"]
})
print(df)

#llamando OneHot
model = OneHotEncoder()
df_model = pd.DataFrame(model.fit_transform(df).toarray(),columns=model.get_feature_names_out(df.columns))
print(df_model)

#usando pandas
df__pandas = pd.get_dummies(df)
print(df__pandas)