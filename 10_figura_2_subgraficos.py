import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# Figura de 1 fila y 2 columnas
fig, axs = plt.subplots(1, 2, figsize=(13, 5))

# Primer subgráfico: Barras (day vs total_bill)
ventas_dia = df.groupby('day', observed=False)['total_bill'].sum()
axs[0].bar(ventas_dia.index, ventas_dia.values, color='mediumseagreen', edgecolor='black')
axs[0].set_title("Total de cuenta acumulado por día")
axs[0].set_xlabel("Día de la semana")
axs[0].set_ylabel("Total cuenta ($)")

# Segundo subgráfico: Circular (distribución de total_bill por sex)
ventas_sexo = df.groupby('sex', observed=False)['total_bill'].sum()
axs[1].pie(
    ventas_sexo.values,
    labels=ventas_sexo.index,
    autopct='%1.1f%%',
    colors=['cornflowerblue', 'salmon'],
    startangle=90
)
axs[1].set_title("Distribución del total de cuenta por género")
axs[1].set_xlabel("Género")

# Ajuste de espacio entre subgráficos
plt.tight_layout()
plt.show()