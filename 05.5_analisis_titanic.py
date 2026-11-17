import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("titanic.csv")

tabla_clase_sup = pd.crosstab(df['Pclass'], df['Survived'])
tabla_clase_sup.columns = ["Fallecidos", "Supervivientes"]

# 5.5. Diagrama de barras apiladas/acumuladas en cada clase
fig5, ax5 = plt.subplots()
tabla_clase_sup.plot(kind="bar", stacked=True, ax=ax5, color=["salmon", "mediumseagreen"], rot=0)
ax5.set_title("Fallecidos y supervivientes acumulados por clase")
ax5.set_xlabel("Clase")
ax5.set_ylabel("Número de personas")
plt.show()