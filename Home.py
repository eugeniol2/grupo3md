import streamlit as st
import numpy as np
from scipy import stats
import data_management
import mathFunctions
import pandas as pd
import matplotlib.pyplot as plt

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

perguntas = [
    'Qual a taxa de evasão presente nos cursos?', 
    'Qual é a faixa etária predominante a depender do curso?'
]

opcao_pergunta = st.selectbox(
    'Selecione a pergunta: ',
    (perguntas[0], perguntas[1])
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
    "Qual é a faixa etária predominante a depender do curso?"
    )
    selected_course = st.selectbox("Escolha um curso", course_names_list)

    values = data_management.getValuesForAge(
    "NO_CURSO",
    searchName=selected_course
    )

    if values is not None:
        st.title("Distribuição das Matrículas por Faixas Etárias:")   

        values_df = pd.concat(values, ignore_index=True)

        # Calculate enrollment counts
        qtd_matricula_0_17 = values_df['QT_MAT_0_17'].sum()
        qtd_matricula_18_24 = values_df['QT_MAT_18_24'].sum()
        qtd_matricula_25_29 = values_df['QT_MAT_25_29'].sum()
        qtd_matricula_30_34 = values_df['QT_MAT_30_34'].sum()
        qtd_matricula_35_39 = values_df['QT_MAT_35_39'].sum()
        qtd_matricula_40_49 = values_df['QT_MAT_40_49'].sum()
        qtd_matricula_50_59 = values_df['QT_MAT_50_59'].sum()
        qtd_matricula_60_MAIS = values_df['QT_MAT_60_MAIS'].sum()
        
        # Create a dictionary of age groups and their counts
        age_groups = {
            "0-17": qtd_matricula_0_17,
            "18-24": qtd_matricula_18_24,
            "25-29": qtd_matricula_25_29,
            "30-34": qtd_matricula_30_34,
            "35-39": qtd_matricula_35_39,
            "40-49": qtd_matricula_40_49,
            "50-59": qtd_matricula_50_59,
            "60 MAIS": qtd_matricula_60_MAIS
        }
        # Find the maximum count
        max_count = max(age_groups.values())

        # Find all age groups with the maximum count (ties)
        predominant_age_groups = [age_group for age_group, count in age_groups.items() if count == max_count]

        # Create a pie chart
        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            age_groups.values(),
            labels=age_groups.keys(),
            autopct='%1.1f%%',
            startangle=90,
            pctdistance=0.85,  # Adjust the distance of percentage labels from the center
        )
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Add a legend
        legend_labels = [f'{label} ({count})' for label, count in zip(age_groups.keys(), age_groups.values())]
        ax.legend(wedges, legend_labels, title="Faixas Etarias", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        # Display the pie chart using Streamlit
        st.pyplot(fig)

        # Display the predominant age groups
        st.write('As faixas etárias de maior predominância são:', ', '.join(predominant_age_groups))
        

        
            


    
   


if opcao_pergunta == perguntas[0]:
    taxa_evasao()
elif opcao_pergunta == perguntas[1]:
    faixa_etaria()
