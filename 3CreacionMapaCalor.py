import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Carga de la matriz de correlación de Spearman desde el CSV generado previamente
df_corr = pd.read_csv("matriz_correlacion_spearman.csv")

# Crear la matriz de correlación para el mapa de calor
heatmap_data = df_corr.pivot(index='Variable_1', columns='Variable_2', values='Correlacion_Spearman')

# Se setea la diagonal a 1.0 para que se muestre correctamente en el mapa de calor 
for col in heatmap_data.columns:
    heatmap_data.loc[col, col] = 1.0

# Configurar el tamaño de la figura
plt.figure(figsize=(10, 8))

# Dibujar el mapa de calor
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f",
            linewidths=.5, cbar_kws={"shrink": .8})

plt.title('Matriz de Correlación de Spearman (Variables STEAM)', pad=20)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('heatmap_correlacion.png')
print("Heatmap saved as heatmap_correlacion.png")
