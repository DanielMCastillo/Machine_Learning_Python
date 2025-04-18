#Preprocesamiento de datos Escalado
from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = np.array([[12000],[50000],[70000]])
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)
print(scaled_data)