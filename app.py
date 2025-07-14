import streamlit as st

st.set_page_config(page_title="HighFlyer Predictor", layout="centered")

# Estilização com CSS
st.markdown("""
    <style>
    .main {
        background-color: #0f1117;
        color: white;
    }
    .big-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .btn {
        display: inline-block;
        width: 100%;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        border: 2px solid #fff;
        margin-bottom: 10px;
    }
    .btn-alta {
        background-color: #0f0f0f;
        color: #00ff99;
        border-color: #00ff99;
    }
    .btn-baixa {
        background-color: #0f0f0f;
        color: #ff4444;
        border-color: #ff4444;
    }
    .previsao {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top: 30px;
    }
    .btn-reset {
        margin-top: 30px;
        background-color: #333;
        color: white;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<div class='big-title'>🛩️ HighFlyer<br>Previsão de Vela</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Clique nos botões para registrar se a vela foi alta ou baixa</p>", unsafe_allow_html=True)

# Velas
if "velas" not in st.session_state:
    st.session_state.velas = []

# Botões estilizados
col1, col2 = st.columns(2)
with col1:
    if st.button("📈 Vela Alta", key="alta"):
        if len(st.session_state.velas) < 6:
            st.session_state.velas.append("alta")
with col2:
    if st.button("📉 Vela Baixa", key="baixa"):
        if len(st.session_state.velas) < 6:
            st.session_state.velas.append("baixa")

# Mostrar velas
st.markdown(f"<p style='text-align:center'><strong>Velas registradas:</strong> {st.session_state.velas}</p>", unsafe_allow_html=True)

# Previsão
if len(st.session_state.velas) == 6:
    alta = st.session_state.velas.count("alta")
    baixa = st.session_state.velas.count("baixa")

    if alta > baixa:
        previsao = "<span style='color:#00ff99'>📈 Provável Vela Alta</span>"
    elif baixa > alta:
        previsao = "<span style='color:#ff4444'>📉 Provável Vela Baixa</span>"
    else:
        previsao = "<span style='color:gray'>⚖️ Tendência Neutra</span>"

    st.markdown(f"<div class='previsao'>{previsao}</div>", unsafe_allow_html=True)

# Botão de reset
if st.button("🔁 Nova Rodada"):
    st.session_state.velas = []
