import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# Crear figura con 2 filas y 3 columnas
fig, axs = plt.subplots(2, 3, figsize=(16, 10))

# 1. Gráfico de barras: total de la cuenta por día
cuenta_dia = df.groupby('day', observed=False)['total_bill'].sum()
axs[0, 0].bar(cuenta_dia.index, cuenta_dia.values, color='cornflowerblue')
axs[0, 0].set_title("Total de cuenta por día")
axs[0, 0].set_xlabel("Día de la semana")
axs[0, 0].set_ylabel("Total cuenta ($)")

# 2. Gráfico de líneas: relación total_bill vs tip + línea de propina media
df_ordenado = df.sort_values('total_bill')
propina_media = df['tip'].mean()
axs[0, 1].plot(df_ordenado['total_bill'], df_ordenado['tip'], label='Propina', color='teal')
axs[0, 1].axhline(propina_media, color='red', linestyle='--', label=f'Media ({propina_media:.2f}$)')
axs[0, 1].set_title("Relación cuenta y propina")
axs[0, 1].set_xlabel("Total cuenta ($)")
axs[0, 1].set_ylabel("Propina ($)")
axs[0, 1].legend()

# 3. Gráfico de dispersión: total_bill vs tip
axs[0, 2].scatter(df['total_bill'], df['tip'], color='darkorange', alpha=0.7)
axs[0, 2].set_title("Dispersión cuenta vs propina")
axs[0, 2].set_xlabel("Total cuenta ($)")
axs[0, 2].set_ylabel("Propina ($)")

# 4. Gráfico circular: distribución del total de la cuenta por sexo
cuenta_sexo = df.groupby('sex', observed=False)['total_bill'].sum()
axs[1, 0].pie(cuenta_sexo.values, labels=cuenta_sexo.index, autopct='%1.1f%%', colors=['lightblue', 'lightpink'])
axs[1, 0].set_title("Distribución de cuenta por sexo")
axs[1, 0].set_xlabel("Sexo")

# 5. Histograma: distribución de total_bill
axs[1, 1].hist(df['total_bill'], bins=15, color='mediumpurple', edgecolor='black')
axs[1, 1].set_title("Histograma del total de la cuenta")
axs[1, 1].set_xlabel("Total cuenta ($)")
axs[1, 1].set_ylabel("Frecuencia")

# 6. Caja y bigotes: propinas (tip) en función del día (day)
dias = df['day'].unique()
datos_propinas_dia = [df[df['day'] == d]['tip'] for d in dias]
axs[1, 2].boxplot(datos_propinas_dia)
axs[1, 2].set_xticklabels(dias)
axs[1, 2].set_title("Propinas por día de la semana")
axs[1, 2].set_xlabel("Día")
axs[1, 2].set_ylabel("Propina ($)")

# Ajustar el espaciado entre subgráficos para evitar solapamientos
plt.tight_layout()
plt.show()