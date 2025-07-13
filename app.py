import streamlit as st

st.set_page_config(page_title="🚀 HighFlyer - Previsão", layout="centered")

st.title("🚀 HighFlyer - Previsão Inteligente")
st.write("Digite os **últimos 6 valores das velas** para prever o próximo movimento.")
st.write("Exemplo: `1.23, 1.01, 2.04, 1.99, 1.55, 1.32`")

entrada = st.text_area("Resultados (separados por vírgula)", height=100)

def analisar_velas(valores):
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

if entrada:
    try:
        lista_valores = [float(x.strip()) for x in entrada.split(",") if x.strip()]
        if len(lista_valores) < 6:
            st.warning("Por favor, insira pelo menos 6 valores.")
        else:
            resultado = analisar_velas(lista_valores)
            st.success(f"🔍 Resultado da análise: {resultado}")
    except ValueError:
        st.error("Erro: Certifique-se de que os valores são números separados por vírgula.")
