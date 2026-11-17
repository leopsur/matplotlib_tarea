import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("titanic.csv")

# 5.3. Diagrama de barras con el número de personas en cada clase
fig3, ax3 = plt.subplots()
conteo_clases = df['Pclass'].value_counts().sort_index()
ax3.bar(conteo_clases.index.astype(str), conteo_clases.values, color="slateblue")
ax3.set_title("Número de pasajeros por clase")
ax3.set_xlabel("Clase")
ax3.set_ylabel("Número de personas")
plt.show()