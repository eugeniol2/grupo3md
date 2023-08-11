import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

censo = pd.concat([
    pd.read_csv("data\censo2020_filtrado.CSV"),
    pd.read_csv("data\censo2021_filtrado.CSV")
])

st.title("Censo - Evasão dos Cursos")


filtro_opcao = st.selectbox("Selecione um aspecto para analisar a evasão:", 
                            ["Região", "UF", "Cidade", "Curso", "Idade"])


if filtro_opcao == "Região":
    filtro_valor = st.selectbox("Selecione uma região:", censo["NO_REGIAO"].unique())
    dados_filtrados = censo[censo["NO_REGIAO"] == filtro_valor]
    filtro_titulo = f"Evasão dos Cursos na Região {filtro_valor}"
elif filtro_opcao == "UF":
    filtro_valor = st.selectbox("Selecione uma UF:", censo["SG_UF"].unique())
    dados_filtrados = censo[censo["SG_UF"] == filtro_valor]
    filtro_titulo = f"Evasão dos Cursos na UF {filtro_valor}"
elif filtro_opcao == "Cidade":
    filtro_valor = st.selectbox("Selecione uma cidade:", censo["NO_MUNICIPIO"].unique())
    dados_filtrados = censo[censo["NO_MUNICIPIO"] == filtro_valor]
    filtro_titulo = f"Evasão dos Cursos em {filtro_valor}"
elif filtro_opcao == "Curso":
    filtro_valor = st.selectbox("Selecione um curso:", censo["NO_CURSO"].unique())
    dados_filtrados = censo[censo["NO_CURSO"] == filtro_valor]
    filtro_titulo = f"Evasão do Curso {filtro_valor}"
else:
    filtro_valor = st.slider("Selecione uma faixa etária:", min_value=0, max_value=100, value=(0, 100))
    dados_filtrados = censo[(censo["QT_CONC_18_24"] + censo["QT_CONC_25_29"] + 
                            censo["QT_CONC_30_34"] + censo["QT_CONC_35_39"] + censo["QT_CONC_40_49"] + 
                            censo["QT_CONC_50_59"] + censo["QT_CONC_60_MAIS"]).between(*filtro_valor)]
    filtro_titulo = f"Evasão dos Cursos para Faixa Etária {filtro_valor[0]}-{filtro_valor[1]}"

st.title("Descrição dos Dados")
st.write(dados_filtrados.describe())

st.title(f"Filtro: {filtro_opcao}")
st.header(filtro_titulo)
fig, ax = plt.subplots()
ax.bar(["Evasão", "Permanência"], [dados_filtrados["QT_CONC"].sum(), dados_filtrados["QT_MAT"].sum()])
ax.set_ylabel("Quantidade de Alunos")
ax.set_title(f"Evasão vs. Permanência nos Cursos")
st.pyplot(fig)

st.title("Percentual de Evasão vs. Permanência")
fig, ax = plt.subplots()
labels = ["Evasão", "Permanência"]
sizes = [dados_filtrados["QT_CONC"].sum(), dados_filtrados["QT_MAT"].sum()]
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)