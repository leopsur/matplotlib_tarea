import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# Filtramos el DataFrame por género
hombres = df[df['sex'] == 'Male']
mujeres = df[df['sex'] == 'Female']

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(hombres['total_bill'], hombres['tip'], color='blue', label='Hombres (Male)', alpha=0.7)
ax.scatter(mujeres['total_bill'], mujeres['tip'], color='red', label='Mujeres (Female)', alpha=0.7)

ax.set_title("Relación entre total de la cuenta y propina según género")
ax.set_xlabel("Total de la cuenta ($)")
ax.set_ylabel("Propina ($)")
ax.legend(title="Género")
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()