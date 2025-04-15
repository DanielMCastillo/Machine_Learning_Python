#Exploring Titanic Dataset
import pandas as pd

titanic = pd.read_csv("datasets/train_titanic.csv")
print(titanic)

#¿Cómo se relaciona la edad con la supervivencia?
print(titanic.groupby("Survived")["Age"].mean())
#¿El género tiene alguna relación con la superviviencia?
print(titanic.groupby("Sex")["Survived"].mean())
#¿Cuantos pasajeros sobrevivieron y cuantos no?
print(titanic["Survived"].value_counts())
#¿La clase tiene alguna relación con la supervivencia?
print(titanic.groupby("Pclass")["Survived"].mean())
#¿La tarifa tiene alguna relacion con la supervivencia?
print(titanic.groupby("Survived")["Fare"].mean())
#¿El puerto del embarque tiene alguna relacion con la supérvivencia?
print(titanic["Embarked"].value_counts())
print(titanic.groupby("Embarked")["Survived"].mean())