import streamlit as st
import pandas as pd

censo2020 = pd.read_csv("data\censo2020_filtrado.CSV")
censo2021 = pd.read_csv("data\censo2021_filtrado.CSV")


st.title("Censo 2020")
st.write(censo2020.describe())
st.title("Censo 2021")
st.write(censo2021.describe())


st.title("Streamlit")
