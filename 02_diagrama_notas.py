import matplotlib.pyplot as plt

def diagrama_notas(notas, color):
    """Recibe un diccionario {asignatura: nota} y un color, y devuelve el eje con el gráfico."""
    fig, ax = plt.subplots()
    
    asignaturas = list(notas.keys())
    calificaciones = list(notas.values())
    
    ax.bar(asignaturas, calificaciones, color=color)
    ax.set_title("Notas de las asignaturas")
    ax.set_xlabel("Asignaturas")
    ax.set_ylabel("Nota")
    ax.set_ylim(0, 10)  # Escala estándar de 0 a 10
    
    return ax

# Ejemplo de prueba
mis_notas = {"Matemáticas": 8.5, "Física": 7.0, "Programación": 9.5, "Historia": 6.8}
grafico = diagrama_notas(mis_notas, "teal")
plt.show()