import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# Agrupamos por día y sexo sumando las propinas, y desapilamos 'sex' en columnas
tabla = df.groupby(['day', 'sex'], observed=False)['tip'].sum().unstack()

fig, ax = plt.subplots(figsize=(8, 6))

# Dibujamos la primera serie (Male) y encima (bottom) la segunda serie (Female)
ax.bar(tabla.index, tabla['Male'], label='Hombres (Male)', color='#3498db')
ax.bar(tabla.index, tabla['Female'], bottom=tabla['Male'], label='Mujeres (Female)', color='#e74c3c')

ax.set_title("Distribución acumulada de propinas por día y sexo")
ax.set_xlabel("Día de la semana")
ax.set_ylabel("Total de propinas ($)")
ax.legend(title="Sexo")

plt.tight_layout()
plt.show()