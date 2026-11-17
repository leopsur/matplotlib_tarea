import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = sns.load_dataset('tips')

# Calculamos la regresión lineal entre total_bill (X) y tip (Y)
resultado = linregress(df['total_bill'], df['tip'])
pendiente = resultado.slope
intercepto = resultado.intercept

# Calculamos los valores Y de la recta de tendencia: y = m*x + b
linea_tendencia = pendiente * df['total_bill'] + intercepto

fig, ax = plt.subplots(figsize=(9, 6))

# Puntos de dispersión
ax.scatter(df['total_bill'], df['tip'], color='steelblue', alpha=0.6, label='Observaciones (clientes)')

# Línea de tendencia
ax.plot(
    df['total_bill'],
    linea_tendencia,
    color='red',
    linewidth=2,
    label=f'Línea de tendencia (y = {pendiente:.2f}x + {intercepto:.2f})'
)

ax.set_title("Regresión lineal: Total de la cuenta vs Propina")
ax.set_xlabel("Total de la cuenta ($)")
ax.set_ylabel("Propina ($)")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()