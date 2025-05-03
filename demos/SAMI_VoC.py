import streamlit as st
import pandas as pd

st.title("💬 SAMI VoC Demo")
st.write("Sube un archivo con verbatims de clientes para analizar sentimientos y temas clave.")

uploaded_file = st.file_uploader("Sube un archivo CSV con una columna 'comentario':", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Vista previa:")
    st.dataframe(df.head())
    st.success("Análisis de sentimiento simulado:")
    st.bar_chart({"Positivo": [45], "Negativo": [25], "Neutral": [30]})