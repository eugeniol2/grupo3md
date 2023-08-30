import streamlit as st

def calcular_taxa_evasao(row):
    M_n = row["QT_MAT_2021"]
    In_n = row["QT_ING_2021"]
    M_n_1 = row["QT_MAT_2020"]
    Eg_n_1 = row["QT_ING_2020"]

    if M_n_1 - Eg_n_1 == 0:
        return None

    return 1-((M_n - In_n) / (M_n_1 - Eg_n_1)) 


def userCalculator():
    st.title("Calculadora de taxa de evasão")
    # User inputs
    M_n = st.number_input("Quantidade matriculados 2021, QT_MAT_2021", min_value=0)
    In_n = st.number_input("Quantidade ingressantes 2021 QT_ING_2021", min_value=0)
    M_n_1 = st.number_input("Quantidade matriculados 2020, QT_MAT_2020", min_value=0)
    Eg_n_1 = st.number_input("Quantidade ingressantes 2020, QT_ING_2020", min_value=0)

    if M_n_1 - Eg_n_1 == 0:
        st.warning("Division by zero. Cannot calculate abandonment rate.")
    else:
        abandonment_rate = 1-((M_n - In_n) / (M_n_1 - Eg_n_1))
        st.subheader(f"Resultado: {abandonment_rate:.2f}%")
