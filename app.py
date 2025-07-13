import streamlit as st

st.set_page_config(page_title="🚀 HighFlyer - Previsão", layout="centered")

st.title("🚀 HighFlyer - Previsão em Tempo Real")
st.markdown("⚡ Digite as velas assim que elas fecharem. O sistema analisa automaticamente!")

# Layout em 2 linhas com 3 colunas cada
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# Inputs separados e rápidos
vela1 = col1.number_input("1ª vela", step=0.01, format="%.2f", key="v1")
vela2 = col2.number_input("2ª vela", step=0.01, format="%.2f", key="v2")
vela3 = col3.number_input("3ª vela", step=0.01, format="%.2f", key="v3")
vela4 = col4.number_input("4ª vela", step=0.01, format="%.2f", key="v4")
vela5 = col5.number_input("5ª vela", step=0.01, format="%.2f", key="v5")
vela6 = col6.number_input("6ª vela", step=0.01, format="%.2f", key="v6")

valores = [vela1, vela2, vela3, vela4, vela5, vela6]

def analisar_velas(valores):
    if any(v == 0.0 for v in valores):
        return "⏳ Aguardando todos os valores..."

    ult_5 = valores[-5:]
    ult_6 = valores[-6:]

    media_5 = sum(ult_5) / 5
    abaixo_2 = sum(1 for x in ult_6 if x < 2.0)
    frias = sum(1 for x in ult_6 if x < media_5 * 0.95)
    sem_repeticao = all(ult_6.count(x) == 1 for x in ult_6)

    if abaixo_2 >= 3:
        return "🔥 Alta probabilidade de vela verde!"
    elif frias >= 3:
        return "⚠️ Pode vir uma vela verde forte!"
    elif sem_repeticao:
        return "🔄 Padrão sem repetição — possível reversão!"
    else:
        return "📉 Sem padrão forte detectado."

resultado = analisar_velas(valores)
st.markdown(f"### Resultado: {resultado}")
