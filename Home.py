import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

st.set_option('deprecation.showPyplotGlobalUse', False)

censo2020 = pd.read_csv("data/censo2020_filtrado.csv")
censo2021 = pd.read_csv("data/censo2021_filtrado.csv")

st.write("Funcionando")

def calcular_taxa_evasao(row, merged_data):
    M_n = row['QT_MAT_2021']
    In_n = row['QT_ING_2021']
    M_n_1 = row['QT_MAT_2020']  
    Eg_n_1 = row['QT_CONC_2020']  
    
    if M_n_1 - Eg_n_1 == 0:
        return None
    
    return (1-(M_n - In_n) / (M_n_1 - Eg_n_1)) * 100

merged_data = censo2021.merge(censo2020, on='CO_CURSO', suffixes=('_2021', '_2020'))
unique_course_names = merged_data['NO_CURSO_2021'].unique()
course_names_list = np.unique(unique_course_names).tolist()

# #Filtros
# st.subheader("Abaixo é possível regular alguns filtros para obter melhores observações:")
# selected_course = st.selectbox("Escolha um curso", course_names_list)
# selected_course_data = merged_data[merged_data['NO_CURSO_2021'] == selected_course]

# st.title("Taxa de evasão:")
# st.subheader("O calculo é feito em todos as linhas de cursos encontradas de acordo com os filtros selecionados, é então feita uma média para uma melhor observação das taxas. Uma taxa de Z-score também foi aplicada para evitar dados inconsistentes")
# st.write(selected_course_data.head())

# if len(selected_course_data) == 0:
#     st.warning("No data found for the selected course.")
# else:
#     abandonment_rates = selected_course_data.apply(lambda row: calcular_taxa_evasao(row, selected_course_data), axis=1)
#     valid_abandonment_rates = abandonment_rates.dropna()
    
#     if len(valid_abandonment_rates) == 0:
#         st.warning("Não foi possível calcular a taxa de evasão")
#     else:
#         z_scores = np.abs(stats.zscore(valid_abandonment_rates))
#         z_score_threshold = 2
#         valid_abandonment_rates_no_outliers = valid_abandonment_rates[z_scores <= z_score_threshold]
#         mean_abandonment_rate_no_outliers = valid_abandonment_rates_no_outliers.mean()
        
#         st.subheader(f"Taxa de evasão {selected_course} in 2021:")
#         st.subheader(f"Média de evasão (sem outliers): {mean_abandonment_rate_no_outliers:.2f}%")

            