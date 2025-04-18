#Preprocesamiento de datos Normalizado
from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[3],[7],[5],[10]])
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data)
print(normalized_data)