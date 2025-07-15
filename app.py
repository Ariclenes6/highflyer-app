import streamlit as st
from datetime import datetime

st.set_page_config(page_title="HighFlyer - Previsão de Vela", page_icon="✈️")

st.title("✈️ HighFlyer - Previsão de Vela")
st.write("Clique nos botões abaixo para registrar se a vela foi alta ou baixa (total de 6).")

if 'velas' not in st.session_state:
    st.session_state.velas = []

col1, col2 = st.columns(2)

with col1:
    if st.button("📈 Vela Alta"):
        if len(st.session_state.velas) < 6:
            st.session_state.velas.append("alta")

with col2:
    if st.button("📉 Vela Baixa"):
        if len(st.session_state.velas) < 6:
            st.session_state.velas.append("baixa")

st.write(f"**Velas registradas:** {st.session_state.velas}")

if len(st.session_state.velas) == 6:
    altas = st.session_state.velas.count("alta")
    baixas = st.session_state.velas.count("baixa")
    previsao = "Alta" if altas > baixas else "Baixa"
    st.markdown(f"<h1 style='color: red;'>📊 Provável Vela {previsao}</h1>", unsafe_allow_html=True)
    st.write(f"🕒 Previsão gerada em: `{datetime.now().strftime('%H:%M:%S')}`")

if st.button("🔁 Nova Rodada"):
    st.session_state.velas = []
  
