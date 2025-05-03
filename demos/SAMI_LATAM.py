import streamlit as st

st.title("🌎 SAMI LATAM GPT Suite")
st.write("Selecciona un módulo para ver su demo o documentación.")

modules = {
    "SAMI Analyzer": "#",
    "Personas Generator": "#",
    "VoC + Drivers": "#",
    "SAMI LATAM GPT Suite": "https://carlosmsal22.github.io/SAMI-AI-LATAM/"
}

for name, link in modules.items():
    st.markdown(f"[**{name}**]({link})", unsafe_allow_html=True)