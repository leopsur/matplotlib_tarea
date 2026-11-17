import pandas as pd
import matplotlib.pyplot as plt

def graficar_bancos(ruta_fichero):
    """Lee bancos.csv y dibuja las series temporales de cierre de cada banco."""
    df = pd.read_csv(ruta_fichero)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Si el CSV contiene columna 'Fecha', la convertimos a formato datetime para el eje X
    if 'Fecha' in df.columns:
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        for empresa, datos in df.groupby('Empresa'):
            datos_ord = datos.sort_values('Fecha')
            ax.plot(datos_ord['Fecha'], datos_ord['Cierre'], label=empresa)
        ax.set_xlabel("Fecha")
    else:
        for empresa, datos in df.groupby('Empresa'):
            ax.plot(datos['Cierre'].values, label=empresa)
        ax.set_xlabel("Sesión")
        
    ax.set_title("Evolución de cotizaciones al cierre por banco")
    ax.set_ylabel("Precio de cierre (€)")
    ax.legend(title="Bancos")
    ax.grid(True)
    plt.tight_layout()
    
    return ax

# Llamada a la función (asegúrate de tener bancos.csv en la misma carpeta)
graficar_bancos("bancos.csv")
plt.show()