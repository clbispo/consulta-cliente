import streamlit as st
import pandas as pd
def get_data():
    return pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQgTePsE_mQ-SIEK3iOr6fZTKpz8614h4j6Me9eGvw1DqEy6ttd10CRfaiODG3n1e-JkJNKn94hgLLM/pub?output=csv')

df = get_data()

st.set_page_config(page_title="Consulta Atendente", page_icon="🐍", layout="wide")
st.title("Consulta atendente responsável pelo Cliente")

text_search = st.text_input("Pesquise pelo CNPJ ou CPF", value="").strip()

m1 = df["CNPJ/CPF"].str.contains(text_search)
df_search = df[m1]

st.write(df_search)