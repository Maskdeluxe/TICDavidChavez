import pandas as pd
import numpy as np
from scipy.stats import spearmanr
file_path = "/Users/dc/Downloads/respuestasEncuesta.csv"
df = pd.read_csv(file_path)

# Eliminación de la primera fila con registro vacío
df = df.dropna(how='all', subset=['1. Edad en años', '2. Género'])

# Selección de las columnas numéricas
likert_cols = [
    '13. ¿Sientes la suficiente confianza al resolver ejercicios de matemáticas, razonamiento o lógica en general?',
    '14. ¿Crees que las habilidades artísticas o las habilidades blandas pueden generar influencia en el aprendizaje en carreras de ciencias o tecnología?',
    '15. ¿Crees tener el conocimiento para poder seguir una carrera que involucre la ciencia y la matemática?',
    '20. ¿Tus maestros te han animado a explorar temas relacionados con la ciencia o la tecnología?',
    '22. ¿Qué tanto apoyo recibes de tu familia para estudiar temas relacionados con las matemáticas o la ciencia?',
    '25. ¿Qué tan optimista te sientes sobre tu futuro en una carrera que involucre tecnología o ciencia?',
    '28. ¿Crees que las innovaciones tecnológicas y la ciencia están mejorando la calidad de vida de las personas?',
    '30. ¿Cuál es la probabilidad de que selecciones una carrera relacionada con Ciencia, Tecnología, Ingeniería, Arte o Matemáticas (STEAM)?',
    '31. ¿Qué tan informado/a te sientes sobre las diferentes opciones de carrera STEAM?'
]

short_names = {
    '13. ¿Sientes la suficiente confianza al resolver ejercicios de matemáticas, razonamiento o lógica en general?': 'Confianza_Matematicas',
    '14. ¿Crees que las habilidades artísticas o las habilidades blandas pueden generar influencia en el aprendizaje en carreras de ciencias o tecnología?': 'Influencia_Arte_Blandas',
    '15. ¿Crees tener el conocimiento para poder seguir una carrera que involucre la ciencia y la matemática?': 'Conocimiento_Ciencia_Mat',
    '20. ¿Tus maestros te han animado a explorar temas relacionados con la ciencia o la tecnología?': 'Animo_Maestros',
    '22. ¿Qué tanto apoyo recibes de tu familia para estudiar temas relacionados con las matemáticas o la ciencia?': 'Apoyo_Familiar',
    '25. ¿Qué tan optimista te sientes sobre tu futuro en una carrera que involucre tecnología o ciencia?': 'Optimismo_Futuro',
    '28. ¿Crees que las innovaciones tecnológicas y la ciencia están mejorando la calidad de vida de las personas?': 'Impacto_Innovacion',
    '30. ¿Cuál es la probabilidad de que selecciones una carrera relacionada con Ciencia, Tecnología, Ingeniería, Arte o Matemáticas (STEAM)?': 'Probabilidad_STEAM',
    '31. ¿Qué tan informado/a te sientes sobre las diferentes opciones de carrera STEAM?': 'Nivel_Informacion'
}

df_likert = df[likert_cols].rename(columns=short_names)

# Calculo de la matriz de correlación de Spearman y los valores p
cols = df_likert.columns
corr_data = []

for var1 in cols:
    for var2 in cols:
        if var1 != var2:
            # Drop na for the pair
            valid_data = df_likert[[var1, var2]].dropna()
            if len(valid_data) > 1:
                corr, pval = spearmanr(valid_data[var1], valid_data[var2])
                corr_data.append({
                    'Variable_1': var1,
                    'Variable_2': var2,
                    'Correlacion_Spearman': corr,
                    'P_Valor': pval,
                    'Significativo': 'Si' if pval < 0.05 else 'No'
                })

df_corr = pd.DataFrame(corr_data)

# exportar a CSV
df_likert_full = df.rename(columns=short_names)
# limpieza de columnas para Looker Studio
df_likert_full.columns = df_likert_full.columns.str.replace(r'^\d+\.\s*', '', regex=True).str.replace('?', '').str.replace('¿', '').str.strip()

df_likert_full.to_csv("datos_limpios_looker.csv", index=False)
df_corr.to_csv("matriz_correlacion_spearman.csv", index=False)

print("Archivos generados: datos_limpios_looker.csv y matriz_correlacion_spearman.csv")
print(df_corr.head())
