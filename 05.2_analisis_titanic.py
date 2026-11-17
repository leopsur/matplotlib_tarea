import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("titanic.csv")

# 5.2. Histograma con las edades
fig2, ax2 = plt.subplots()
ax2.hist(df['Age'].dropna(), bins=20, color="skyblue", edgecolor="black")
ax2.set_title("Distribución de edades de los pasajeros")
ax2.set_xlabel("Edad")
ax2.set_ylabel("Frecuencia (nº de pasajeros)")
plt.show()
