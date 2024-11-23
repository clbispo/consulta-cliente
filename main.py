import streamlit as st
import pandas as pd

# Função para carregar os dados
def get_data():
    return pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQgTePsE_mQ-SIEK3iOr6fZTKpz8614h4j6Me9eGvw1DqEy6ttd10CRfaiODG3n1e-JkJNKn94hgLLM/pub?output=csv')

# Carregar dados
df = get_data()

# Configuração da página
st.set_page_config(page_title="Consulta Atendente", page_icon="🐍", layout="wide")
st.title("Consulta atendente responsável pelo Cliente")

# Campo de entrada para pesquisa
text_search = st.text_input("Pesquise pelo CNPJ ou CPF", value="").strip()

# Verificar se algo foi pesquisado
if text_search:
    # Filtrar dados com base na pesquisa
    m1 = df["CNPJ/CPF"].str.contains(text_search, na=False)
    df_search = df[m1]

    if not df_search.empty:
        # Exibir resultados se houver correspondências
        st.write(df_search)
    else:
        # Mensagem caso não haja resultados
        st.warning("Nenhum resultado encontrado para a pesquisa.")
else:
    # Mensagem para incentivar a pesquisa
    st.info("Digite um CNPJ ou CPF para realizar a pesquisa.")
