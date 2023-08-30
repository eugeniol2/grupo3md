import streamlit as st
import numpy as np
from scipy import stats
import data_management
import mathFunctions
import pandas as pd

st.set_option("deprecation.showPyplotGlobalUse", False)

course_names_list = data_management.getColumUniqueNames("NO_CURSO")

# Filtros
st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
)
selected_course = st.selectbox("Escolha um curso", course_names_list)

values = data_management.find_and_get_matching_courses("NO_CURSO", selected_course)
matching_rows_2020, matching_rows_2021 = values[1]
abandonment_rates = []
if values is not None:
    st.title("Taxa de evasão:")
    st.subheader(
        "O cálculo é feito com base nos dados do curso selecionado para o ano de 2021."
    )
    
    for row_values in values[0]:
        quantidade_matricula = row_values[0]
        quantidade_ingressante = row_values[1]
        quantidade_matricula2020 = row_values[2]
        quantidade_ingressante2020 = row_values[3]

        abandonment_rate = mathFunctions.calcular_taxa_evasao(
            {
                "QT_MAT_2021": quantidade_matricula,
                "QT_ING_2021": quantidade_ingressante,
                "QT_MAT_2020": quantidade_matricula2020,
                "QT_ING_2020": quantidade_ingressante2020,
            }
        )
        if abandonment_rate != None:
            abandonment_rates.append(abandonment_rate)

    average_abandonment_rate = np.mean(abandonment_rates)
    z_scores = np.abs(stats.zscore(abandonment_rates))
    z_score_threshold = 2
    valid_abandonment_rates_no_outliers = [abandonment_rates[i] for i, z_score in enumerate(z_scores) if z_score <= z_score_threshold]
    mean_abandonment_rate_no_outliers = np.mean(valid_abandonment_rates_no_outliers)

    st.subheader(f"Taxa de evasão {selected_course} em 2021:")
    st.subheader(f"Taxa de evasão: {average_abandonment_rate * 100:.2f}%")
    st.subheader(f"Taxa de evasão sem outliers: {mean_abandonment_rate_no_outliers*100:.2f}%")

    st.latex(
            r"""

    evasão=
    1-\lbrack
    \lbrack
    Matriculas\lparen
    2021
    \rparen
    -Ingressantes
    \lparen
    2021
    \rparen
    \rbrack
    /
    \lbrack
    Matriculas\lparen
    2020
    \rparen
    -Ingressantes
    \lparen
    2020
    \rparen
    \rbrack
    """
        )
    columns_to_display_2020 = ['CO_CURSO','QT_MAT', 'QT_ING']
    columns_to_display_2021 = ['CO_CURSO','QT_MAT', 'QT_ING']

    mathFunctions.userCalculator() 
    
    st.title("Dados utilizados no calculo da média")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Dados de 2021:")
        st.dataframe(matching_rows_2021[columns_to_display_2021])
    with col2:
        st.write("Dados de 2020:")
        st.dataframe(matching_rows_2020[columns_to_display_2020])
else:
    st.warning("Nenhum dado encontrado para o curso selecionado.")
