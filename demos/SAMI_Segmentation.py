import streamlit as st

st.title("🧬 SAMI Segmentación Demo")
st.write("Ejemplo de segmentación de consumidores.")

segments = [
    {"Segmento": "Líderes Digitales", "Descripción": "Adoptan tecnología rápidamente, valoran innovación."},
    {"Segmento": "Ahorro Familiar", "Descripción": "Sensibles al precio, buscan valor y tradición."},
    {"Segmento": "Impulsivos Urbanos", "Descripción": "Consumo guiado por emociones, prefieren marcas visuales."}
]

for seg in segments:
    st.subheader(seg["Segmento"])
    st.write(seg["Descripción"])