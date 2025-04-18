#
import numpy as np
import matplotlib.pyplot as plt #libreria para graficar

data = np.random.rand(1000) * 100 - 50
#plt.plot(data)
#plt.show()

def min_max_scaler(data):
    data_min = np.min(data)
    data_max = np.max(data)
    return(data - data_min) / (data_max-data_min)

norm_Data = min_max_scaler(data)
plt.plot(norm_Data)
plt.show()

def standard_scaler(data):
    mean = np.mean(data)
    std = np.std(data)
    return(data - mean) / std

std_data = standard_scaler(data)
plt.plot(std_data)
plt.show()
