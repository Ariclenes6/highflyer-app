import streamlit as st

st.set_page_config(page_title="HighFlyer Predictor", layout="centered")

st.title("🛩️ HighFlyer - Previsão de Vela")
st.markdown("Clique nos botões abaixo para registrar se a vela foi alta ou baixa (total de 6).")

# Lista de velas registradas
if "velas" not in st.session_state:
    st.session_state.velas = []

# Botões
col1, col2 = st.columns(2)
with col1:
    if st.button("📈 Vela Alta"):
        if len(st.session_state.velas) < 6:
            st.session_state.velas.append("alta")
with col2:
    if st.button("📉 Vela Baixa"):
        if len(st.session_state.velas) < 6:
            st.session_state.velas.append("baixa")

# Mostrar velas registradas
st.markdown(f"**Velas registradas:** {st.session_state.velas}")

# Prever próxima vela (lógica simples)
if len(st.session_state.velas) == 6:
    alta = st.session_state.velas.count("alta")
    baixa = st.session_state.velas.count("baixa")

    if alta > baixa:
        previsao = "📈 Provável Vela Alta"
        cor = "green"
    elif baixa > alta:
        previsao = "📉 Provável Vela Baixa"
        cor = "red"
    else:
        previsao = "⚖️ Tendência neutra"
        cor = "gray"

    st.markdown(f"<h2 style='color:{cor}; text-align:center'>{previsao}</h2>", unsafe_allow_html=True)

# Botão para limpar
if st.button("🔄 Nova Rodada"):
    st.session_state.velas = []
