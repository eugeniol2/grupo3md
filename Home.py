import streamlit as st
import numpy as np
from scipy import stats
import data_management
import mathFunctions
import pandas as pd

st.set_option("deprecation.showPyplotGlobalUse", False)

course_names_list = data_management.getColumUniqueNames("NO_CURSO")
organization_names_list = [
    "Todos",
    "Universidade",
    "Centro universitario",
    "Faculdade",
    "Instituto Federal de Educação, Ciência e Tecnologia",
    "Centro Federal de Educação Tecnológica",
]
course_modality = ["Todos", "Presencial", "Curso a distância"]

course_network = ["Todos", "Pública", "Privada"]

region_names_list= data_management.getColumUniqueNames("NO_REGIAO")

opcao_pergunta = st.selectbox(
    'Selecione a pergunta: ',
    ('Qual a taxa de evasão presente nos cursos?', 'Qual é a faixa etária predominante a depender do curso e região do país?')
)

def taxa_evasao():        
    # Filtros
    st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.write(
    "Qual a taxa de evasão presente nos cursos?, a depender do tipo de organização, tipo de rede(pública ou privada), a distância ou presencial, sexo masculino, ou feminino."
    )
    selected_course = st.selectbox("Escolha um curso", course_names_list)
    selected_organization = st.selectbox("Escolha uma organização", organization_names_list)
    selected_modality = st.selectbox("Escolha a modalidade", course_modality)
    selected_network = st.selectbox("Escolha o tipo rede", course_network)

    values = data_management.find_and_get_matching_courses(
    "NO_CURSO",
    searchName=selected_course,
    org_type=selected_organization,
    modality=selected_modality,
    network_type=selected_network,
    )
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
        amountOfResults = len(abandonment_rates)
        average_abandonment_rate = np.mean(abandonment_rates)
        z_scores = np.abs(stats.zscore(abandonment_rates))
        z_score_threshold = 2
        valid_abandonment_rates_no_outliers = [
            abandonment_rates[i]
            for i, z_score in enumerate(z_scores)
            if z_score <= z_score_threshold
        ]
        mean_abandonment_rate_no_outliers = np.mean(valid_abandonment_rates_no_outliers)

        st.subheader(f"Quantidade de dados encontrados: {amountOfResults}")
        st.subheader(f"Taxa de evasão {selected_course} em 2021:")
        st.subheader(f"Taxa de evasão: {average_abandonment_rate * 100:.2f}%")
        st.subheader(
            f"Taxa de evasão sem outliers: {mean_abandonment_rate_no_outliers*100:.2f}%"
        )

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
        columns_to_display_2020 = ["CO_CURSO", "QT_MAT", "QT_ING"]
        columns_to_display_2021 = ["CO_CURSO", "QT_MAT", "QT_ING"]

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
    


def faixa_etaria():
    # Filtros
    st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.write(
    "Qual é a faixa etária predominante a depender do curso e região do país?"
    )
    selected_course = st.selectbox("Escolha um curso", course_names_list)
    selected_region = st.selectbox("Escolha uma regiao", region_names_list)


    
   


if opcao_pergunta == 'Qual a taxa de evasão presente nos cursos?':
    taxa_evasao()
elif opcao_pergunta == 'Qual é a faixa etária predominante a depender do curso e região do país?':
    faixa_etaria()
