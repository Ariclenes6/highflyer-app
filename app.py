import streamlit as st

st.set_page_config(page_title="Analisador de Velas", page_icon="🔥", layout="centered")
st.markdown("""
    <style>
    input[type="number"] {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
# 🔥 Analisador de Velas Rápido
Digite os valores das velas rapidamente. O resultado será exibido automaticamente após a 6ª vela.
""")

valores = []
resultado = ""

def analisar(velas):
    media = sum(velas) / len(velas)
    ultima = velas[-1]
    if ultima > media:
        return "🔥 Alta probabilidade de vela **verde**!"
    else:
        return "🔴 Alta probabilidade de vela **vermelha**!"

cols = st.columns(6)
for i in range(6):
    with cols[i]:
        valor = st.number_input(f"{i+1}ª vela", key=f"vela_{i}", step=0.01, format="%.2f")
        valores.append(valor)

# Só mostra resultado quando todas estão preenchidas
if all(v > 0 for v in valores):
    resultado = analisar(valores)
    st.markdown(f"### Resultado: {resultado}")
else:
    st.markdown("<small>Preencha todos os valores para ver o resultado.</small>", unsafe_allow_html=True)

st.markdown("""
<hr>
<small>⏱ Otimizado para digitação rápida durante jogos como FlaBet.</small>
""")
