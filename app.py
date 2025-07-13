from pathlib import Path

# Código Python do app com base nas instruções do usuário
app_code = """
import streamlit as st

st.set_page_config(page_title="🚀 HighFlyer - Previsão Inteligente", layout="centered")

st.title("🚀 HighFlyer - Previsão Inteligente")
st.markdown("Previsão da próxima vela com base nas **6 últimas**.")

# Botões para facilitar o input rápido
st.subheader("Selecione os últimos resultados:")
col1, col2, col3, col4, col5, col6 = st.columns(6)

vela = []

with col1:
    vela1 = st.text_input("1ª vela", "")
    if vela1: vela.append(float(vela1.replace(",", ".")))
with col2:
    vela2 = st.text_input("2ª vela", "")
    if vela2: vela.append(float(vela2.replace(",", ".")))
with col3:
    vela3 = st.text_input("3ª vela", "")
    if vela3: vela.append(float(vela3.replace(",", ".")))
with col4:
    vela4 = st.text_input("4ª vela", "")
    if vela4: vela.append(float(vela4.replace(",", ".")))
with col5:
    vela5 = st.text_input("5ª vela", "")
    if vela5: vela.append(float(vela5.replace(",", ".")))
with col6:
    vela6 = st.text_input("6ª vela", "")
    if vela6: vela.append(float(vela6.replace(",", ".")))

def analisar(ultimas):
    if len(ultimas) < 5:
        return "⚠️ Insira ao menos 5 velas para analisar."

    abaixo_2 = sum(1 for x in ultimas if x < 2)
    acima_5 = sum(1 for x in ultimas if x >= 5)
    media = sum(ultimas) / len(ultimas)

    if abaixo_2 >= 4:
        return "🔴 Risco alto de crash! Provável abaixo de 2x."
    elif acima_5 >= 2:
        return "🟢 Boa chance de vela acima de 3x!"
    elif media > 2.5:
        return "🟢 Tendência positiva. Pode passar 2x."
    else:
        return "🟡 Zona neutra. Melhor observar."

if len(vela) >= 5:
    st.subheader("🔮 Previsão:")
    resultado = analisar(vela)
    st.success(resultado)
"""

# Salvar o código em um arquivo Python
app_path = Path("/mnt/data/highflyer_app.py")
app_path.write_text(app_code)

app_path.name  # Retornar o nome do arquivo para o usuário baixar ou usar no Streamlit Cloud

