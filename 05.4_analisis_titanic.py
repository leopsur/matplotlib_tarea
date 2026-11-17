import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("titanic.csv")

tabla_clase_sup = pd.crosstab(df['Pclass'], df['Survived'])
tabla_clase_sup.columns = ["Fallecidos", "Supervivientes"]

# 5.4. Diagrama de barras agrupadas (fallecidos y supervivientes en cada clase)
fig4, ax4 = plt.subplots()
tabla_clase_sup.plot(kind="bar", ax=ax4, color=["salmon", "mediumseagreen"], rot=0)
ax4.set_title("Fallecidos y supervivientes por clase")
ax4.set_xlabel("Clase")
ax4.set_ylabel("Número de personas")
plt.show()