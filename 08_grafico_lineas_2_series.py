import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# Ordenamos por total_bill para que las líneas sigan una progresión ordenada en el eje X
df_ordenado = df.sort_values('total_bill')

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(df_ordenado['total_bill'], df_ordenado['tip'], label='Propina (tip)', color='green', linewidth=1.5)
ax.plot(df_ordenado['total_bill'], df_ordenado['size'], label='Tamaño de mesa (size)', color='orange', linewidth=1.5)

ax.set_title("Relación del total de la cuenta con la propina y el tamaño de mesa")
ax.set_xlabel("Total de la cuenta ($)")
ax.set_ylabel("Valor (Dólares / Personas)")
ax.legend()
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()