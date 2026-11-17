import pandas as pd
import matplotlib.pyplot as plt

def diagrama_cajas(serie_notas):
    """Recibe una Serie de Pandas con notas y devuelve un diagrama de cajas."""
    fig, ax = plt.subplots()
    
    ax.boxplot(serie_notas)
    ax.set_title("Distribución de notas")
    ax.set_ylabel("Calificación")
    ax.set_xticklabels(["Alumnos"])
    
    return ax

# Ejemplo de prueba
notas_alumnos = pd.Series([4.5, 5.0, 6.2, 6.8, 7.0, 7.5, 8.1, 8.9, 9.4, 10.0, 2.0])
grafico_cajas = diagrama_cajas(notas_alumnos)
plt.show()