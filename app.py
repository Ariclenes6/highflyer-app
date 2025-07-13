import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Analisador de Velas", layout="centered")

# Barra lateral de instrução
with st.sidebar:
    st.title("📊 Instruções")
    st.markdown("""
    - Digite os valores das **6 últimas velas** o mais rápido possível.
    - O sistema vai calcular o **resultado automaticamente**.
    - Ideal para quem opera com **tempo de 5 segundos entre velas**.
    """)

st.markdown("<h2 style='text-align: center;'>⚡ Analisador de Velas Rápido</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Preencha os valores e o resultado será mostrado automaticamente.</p>", unsafe_allow_html=True)
st.markdown("---")

# Função de análise
def analisar_velas(valores):
    media = sum(valores) / len(valores)
    if valores[-1] > media:
        return "verde", "🔥 Alta probabilidade de vela VERDE!"
    elif valores[-1] < media:
        return "vermelha", "🔻 Alta probabilidade de vela VERMELHA!"
    else:
        return "neutra", "⚠️ Vela neutra ou indefinida."

# Captura dos valores
valores = []
for i in range(1, 7):
    valor = st.number_input(f"{i}ª vela", min_value=0.0, step=0.01, format="%.2f", key=f"vela_{i}")
    valores.append(valor)

# Mostrar resultado apenas se todos forem preenchidos (> 0)
if all(v > 0 for v in valores):
    cor, resultado = analisar_velas(valores)

    # Cor de fundo dinâmica
    if cor == "verde":
        st.success(resultado)
        st.markdown("<audio autoplay><source src='https://actions.google.com/sounds/v1/alarms/beep_short.ogg' type='audio/ogg'></audio>", unsafe_allow_html=True)
    elif cor == "vermelha":
        st.error(resultado)
        st.markdown("<audio autoplay><source src='https://actions.google.com/sounds/v1/alarms/beep_short.ogg' type='audio/ogg'></audio>", unsafe_allow_html=True)
    else:
        st.info(resultado)
else:
    st.info("Preencha todos os valores acima.")
