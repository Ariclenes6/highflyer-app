  import streamlit as st
from datetime import datetime

# Inicializar estado se não existir
if 'velas' not in st.session_state:
    st.session_state.velas = []
if 'resultados' not in st.session_state:
    st.session_state.resultados = []

st.set_page_config(page_title="HighFlyer PRO", page_icon="🚁", layout="centered")

st.title(" 🚁 HighFlyer PRO - Previsão Inteligente de Vela")
st.subheader("Clique nos botões abaixo para registrar se a vela foi alta ou baixa (total de 6).")

col1, col2 = st.columns(2)

with col1:
    if st.button(" 📈 Vela Alta", use_container_width=True):
        st.session_state.velas.append('alta')

with col2:
    if st.button(" 📉 Vela Baixa", use_container_width=True):
        st.session_state.velas.append('baixa')

st.markdown("**Velas registradas:** " + str(st.session_state.velas))

# Função de previsão (simples, baseada em contagem)
def prever_vela(velas):
    if len(velas) < 6:
        return "Aguardando mais dados...", "⚪", "Padrão insuficiente"
    altas = velas.count('alta')
    baixas = velas.count('baixa')
    if altas > baixas:
        return "Provável Vela Alta", "📈", "Confiança Alta"
    elif baixas > altas:
        return "Provável Vela Baixa", "📉", "Confiança Alta"
    else:
        return "Padrão Equilibrado", "⚖️", "Confiança Média"

# Prever
if len(st.session_state.velas) == 6:
    previsao, icone, confianca = prever_vela(st.session_state.velas)
    st.markdown(f"### {icone} {previsao}")
    st.markdown(f"**{confianca}**")
    st.session_state.resultados.append({
        'velas': st.session_state.velas.copy(),
        'previsao': previsao,
        'hora': datetime.now().strftime("%H:%M:%S")
    })

# Histórico de previsões
if st.session_state.resultados:
    st.subheader("Histórico de Rodadas")
    for r in reversed(st.session_state.resultados[-10:]):
        st.markdown(f"{r['hora']} - {r['velas']} ➔ **{r['previsao']}**")

# Resetar rodada
if st.button("🔁 Nova Rodada", type="primary"):
    st.session_state.velas = []
      
