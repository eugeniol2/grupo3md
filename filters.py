import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


censo = pd.concat([
    pd.read_csv("data\censo2020_filtrado.CSV"),
    pd.read_csv("data\censo2021_filtrado.CSV")
])

st.title("Censo - Evasão dos Cursos")

filtro_opcao = st.selectbox("Selecione um aspecto para analisar a evasão:", 
                            ["Região", "UF", "Cidade", "Curso", "Idade", 
                             "Top 5 Cursos por Estado", "Top 5 Cursos Nordeste"])

dados_filtrados = None
filtro_titulo = ""

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
    

    
elif filtro_opcao == "Idade":
    filtro_valor = st.slider("Selecione uma faixa etária:", min_value=0, max_value=100, value=(0, 100))
    dados_filtrados = censo[(censo["QT_CONC_18_24"] + censo["QT_CONC_25_29"] + 
                            censo["QT_CONC_30_34"] + censo["QT_CONC_35_39"] + censo["QT_CONC_40_49"] + 
                            censo["QT_CONC_50_59"] + censo["QT_CONC_60_MAIS"]).between(*filtro_valor)]
    filtro_titulo = f"Evasão dos Cursos para Faixa Etária {filtro_valor[0]}-{filtro_valor[1]}"
    




elif filtro_opcao == "Top 5 Cursos por Estado":
    estado_selecionado = st.selectbox("Selecione um estado:", censo["SG_UF"].unique())
    dados_estado = censo[censo["SG_UF"] == estado_selecionado]
    ranking_estado = dados_estado.groupby(dados_estado["NO_CURSO"].str.lower())["QT_CONC"].sum().sort_values(ascending=False).head(5)
    st.write(f"Ranking dos 5 cursos com mais evasão em {estado_selecionado}:")
    st.write(ranking_estado)
    fig, ax = plt.subplots()
    ax.bar(ranking_estado.index, ranking_estado.values)
    ax.set_ylabel("Quantidade de Alunos Evasão")
    ax.set_xlabel("Cursos")
    ax.set_title(f"Top 5 Cursos com Mais Evasão em {estado_selecionado}")
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
elif filtro_opcao == "Top 5 Cursos Nordeste":
    estados_nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
    dados_nordeste = censo[censo["SG_UF"].isin(estados_nordeste)]
    ranking_nordeste = dados_nordeste.groupby(dados_nordeste["NO_CURSO"].str.lower())["QT_CONC"].sum().sort_values(ascending=False).head(5)
    st.write("Ranking dos 5 cursos com mais evasão em todos os estados do Nordeste:")
    st.write(ranking_nordeste)
    fig, ax = plt.subplots()
    ax.bar(ranking_nordeste.index, ranking_nordeste.values)
    ax.set_ylabel("Quantidade de Alunos Evasão")
    ax.set_xlabel("Cursos")
    ax.set_title("Top 5 Cursos com Mais Evasão no Nordeste")
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.title(f"Filtro: {filtro_opcao}")
st.header(filtro_titulo)

if dados_filtrados is not None:
    fig, ax = plt.subplots()
    ax.bar(["Evasão", "Permanência"], [dados_filtrados["QT_CONC"].sum(), dados_filtrados["QT_MAT"].sum()])
    ax.set_ylabel("Quantidade de Alunos")
    ax.set_title(f"Evasão vs. Permanência nos Cursos")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    labels = ["Evasão", "Permanência"]
    sizes = [dados_filtrados["QT_CONC"].sum(), dados_filtrados["QT_MAT"].sum()]
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

st.title("Descrição dos Dados")
if dados_filtrados is not None:
    st.write(dados_filtrados.describe())
