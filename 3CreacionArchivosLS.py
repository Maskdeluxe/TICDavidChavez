import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Load the generated matrix
df_corr = pd.read_csv("matriz_correlacion_spearman.csv")

# Create a pivot table for the heatmap
heatmap_data = df_corr.pivot(index='Variable_1', columns='Variable_2', values='Correlacion_Spearman')

# We want to fill the diagonal with 1s since it's not present in the pairs we kept
for col in heatmap_data.columns:
    heatmap_data.loc[col, col] = 1.0

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f",
            linewidths=.5, cbar_kws={"shrink": .8})

plt.title('Matriz de Correlación de Spearman (Variables STEAM)', pad=20)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('heatmap_correlacion.png')
print("Heatmap saved as heatmap_correlacion.png")