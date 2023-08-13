import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

censo2020 = pd.read_csv("data\censo2020_filtrado.CSV")
censo2021 = pd.read_csv("data\censo2021_filtrado.CSV")



# st.title("Censo 2020")
# st.write(censo2020.describe())
# st.title("Censo 2021")
# st.write(censo2021.describe())

def calcular_taxa_evasao(row, merged_data):
    M_n = row['QT_MAT_2021']
    In_n = row['QT_ING_2021']
    M_n_1 = merged_data[(merged_data['CO_CURSO_2020'] == row['CO_CURSO_2020'])]['QT_MAT_2020'].values[0]
    Eg_n_1 = merged_data[(merged_data['CO_CURSO_2020'] == row['CO_CURSO_2020'])]['QT_CONC_2020'].values[0]
    
    if M_n_1 - Eg_n_1 == 0:
        return None
    
    return (M_n - In_n) / (M_n_1 - Eg_n_1)#falta por o 1 - resultado em algum lugar

# Merge censo2021 data with corresponding censo2020 data
merged_data = censo2021.merge(censo2020, on='CO_CURSO', suffixes=('_2021', '_2020'))

st.title("merged_data")
st.write(merged_data.head())
# Create a Streamlit app
st.title("Abandonment Rate Calculator")

# Display dropdown to select a course
selected_course = st.selectbox("Select a course", merged_data['NO_CURSO_2021'])

# Filter data for the selected course
selected_course_data = merged_data[merged_data['NO_CURSO_2021'] == selected_course]
st.write(selected_course_data)

if len(selected_course_data) == 0:
    st.warning("No data found for the selected course.")
else:
    # Calculate abandonment rate for the selected course
    selected_row = selected_course_data.iloc[0]
    abandonment_rate = calcular_taxa_evasao(selected_row, censo2020)
    
    if abandonment_rate is None:
        st.warning("Abandonment rate cannot be calculated (M(n-1) - Eg(n-1) is zero).")
    else:
        st.write(f"Abandonment Rate for {selected_course} in 2021: {abandonment_rate:.4f}")