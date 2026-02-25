import pandas as pd
import numpy as np

file_path = "/Users/dc/Downloads/respuestasEncuesta.csv"
df = pd.read_csv(file_path)

print("Columns:")
print(df.columns.tolist())
print("\nInfo:")
df.info()
print("\nHead:")
print(df.head())