import streamlit as st

# Configurações iniciais
st.set_page_config(
    page_title="Analisador de Velas",
    page_icon="📊",
    layout="centered"
)

# Título e instrução
st.title("📊 Analisador de Velas")
st.markdown("⚡ *Digite os valores das últimas 6 velas assim que elas fecharem. O sistema vai analisar automaticamente!*")
st.markdown("---")

# Layout em colunas
col1, col2 = st.columns(2)

with col1:
    v1 = st.number_input("1ª vela", step=0.01, format="%.2f")
    v2 = st.number_input("2ª vela", step=0.01, format="%.2f")
    v3 = st.number_input("3ª vela", step=0.01, format="%.2f")

with col2:
    v4 = st.number_input("4ª vela", step=0.01, format="%.2f")
    v5 = st.number_input("5ª vela", step=0.01, format="%.2f")
    v6 = st.number_input("6ª vela", step=0.01, format="%.2f")

# Lógica simples de exemplo
velas = [v1, v2, v3, v4, v5, v6]
media = sum(velas) / 6

st.markdown("---")
st.subheader("🔍 Resultado da Análise")

# Exemplo de lógica: se a média das velas for maior que 1.5, probabilidade de vela verde
if media > 1.5:
    st.success("🔥 Alta probabilidade de **vela verde**!")
elif media < 1.0:
    st.error("🔻 Alta probabilidade de **vela vermelha**!")
else:
    st.warning("⚠️ Possível **vela de indecisão** (Doji)")

# Explicação adicional
st.markdown("✅ Essa previsão é baseada na média dos valores inseridos. Quanto mais precisos os dados, melhor o resultado.")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido por Ariclenes com Streamlit 🚀")
