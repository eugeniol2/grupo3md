import streamlit as st
import pandas as pd

censo2020 = pd.read_csv("data\censo2020.CSV")
censo2021 = pd.read_csv("data\censo2021.CSV")
censo2020_2021_merged = pd.read_csv("data\merged_censo.CSV")

st.write("censo2020")
st.write(censo2020_2021_merged.head())
st.write("Merged Censo Data")
