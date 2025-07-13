import streamlit as st

st.set_page_config(page_title="HighFlyer", layout="centered")
st.title("🚀 Bem-vindo ao HighFlyer")

st.write("Toque nos valores das últimas velas para prever a próxima.")

# Lista de botões de valores comuns em jogos como HighFlyer
valores_possiveis = [
    "1x", "1.5x", "2x", "3x", "5x", "10x", "20x+"
]

# Inicializa o histórico se não existir ainda
if "historico" not in st.session_state:
    st.session_state.historico = []

col1, col2, col3, col4 = st.columns(4)

# Organiza os botões em colunas
for i, valor in enumerate(valores_possiveis):
    col = [col1, col2, col3, col4][i % 4]
    if col.button(valor):
        if len(st.session_state.historico) >= 6:
            st.session_state.historico.pop(0)
        st.session_state.historico.append(valor)

# Mostra as últimas 6 velas
st.subheader("Últimas 6 velas:")
st.write(" ➤ ", " | ".join(st.session_state.historico))

# Previsão simples (lógica inicial)
if len(st.session_state.historico) == 6:
    conta_acima_2x = sum(1 for v in st.session_state.historico if v in ["2x", "3x", "5x", "10x", "20x+"])
    if conta_acima_2x >= 3:
        st.success("🔮 Previsão: Próxima vela pode bater 2x ou mais!")
    else:
        st.warning("⚠️ Previsão: Provável abaixo de 2x")
else:
    st.info("Digite 6 velas para gerar previsão.")

# Botão para limpar
if st.button("Limpar Histórico"):
    st.session_state.historico = []
