#Metrica ROC
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz


#Establecer semilla aleatoria
np.random.seed(0)
#Generar etiquetas de clase
y = np.random.randint(0,2,1000)

# Generar puntuación de predicción
y_scores_random = np.random.rand(len(y))
#Ordenar puntuaciones y las verdaderas etiquetas en orden descendente de puntuaciones
sort_indices = np.argsort(y_scores_random)[::-1]
y_sorted = y[sort_indices]


#Calcular tasa de verdaderos positivos y falsos positivos acumulados
TP_cumsum = np.cumsum(y_sorted)
FP_cumsum = np.cumsum(1-y_sorted)

#calcular TPR y FPR
TPR = TP_cumsum/TP_cumsum[-1]
FPR = FP_cumsum/ FP_cumsum[-1]

#Area bajo la curva - AUC
AUC = trapz(TPR, FPR)

#graficas
#plot ROC CURVE
plt.plot(FPR,TPR)
plt.plot([0,1],[0,1],'k--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.0])
plt.xlabel("False positive rate")
plt.ylabel("True positive rate")
plt.title("ROC Curve, AUC=:{.2f}".format(AUC))
plt.show()