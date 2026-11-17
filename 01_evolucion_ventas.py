import matplotlib.pyplot as plt

# Pedimos al usuario el rango de años
inicio = int(input("Introduce el año inicial: "))
fin = int(input("Introduce el año final: "))

# Creamos un diccionario o listas para almacenar los años y sus ventas
ventas = {}
for anio in range(inicio, fin + 1):
    ventas[anio] = float(input(f"Introduce las ventas del año {anio}: "))

# Creamos el diagrama de líneas
fig, ax = plt.subplots()
ax.plot(list(ventas.keys()), list(ventas.values()), marker='o', linestyle='-', color='b')

# Personalización básica
ax.set_title("Evolución de las ventas")
ax.set_xlabel("Año")
ax.set_ylabel("Ventas")
ax.set_xticks(list(ventas.keys()))  # Asegura que en el eje X salgan los años enteros
ax.grid(True)

plt.show()