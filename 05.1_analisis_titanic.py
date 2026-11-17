import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("titanic.csv")

# 5.1. Diagrama de sectores con los fallecidos y supervivientes
fig1, ax1 = plt.subplots()
conteo_supervivencia = df['Survived'].value_counts().sort_index()
ax1.pie(
    conteo_supervivencia,
    labels=["Fallecidos", "Supervivientes"],
    autopct="%1.1f%%",
    colors=["lightcoral", "lightgreen"],
    startangle=90
)
ax1.set_title("Porcentaje de fallecidos y supervivientes")
plt.show()