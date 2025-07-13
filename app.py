importar streamlit como st

st.set_page_config(page_title="ðŸš€ HighFlyer - Visão Inteligente", layout="centered")

st.title("ðŸš€ HighFlyer - Previsão Inteligente")
st.markdown("Previsão da próxima vela com base nas **6 últimas**.")

# Botões para facilitar a entrada rápida
st.subheader("Selecione os últimos resultados:")
col1, col2, col3, col4, col5, col6 = st.columns(6)

vela = []

com col1:
    vela1 = st.text_input("1ª vela", "")
    se vela1: vela.append(float(vela1.replace(",", ".")))
com col2:
    vela2 = st.text_input("2ª vela", "")
    se vela2: vela.append(float(vela2.replace(",", ".")))
com col3:
    vela3 = st.text_input("3ª vela", "")
    se vela3: vela.append(float(vela3.replace(",", ".")))
com col4:
    vela4 = st.text_input("4ª vela", "")
    se vela4: vela.append(float(vela4.replace(",", ".")))
com col5:
    vela5 = st.text_input("5ª vela", "")
    se vela5: vela.append(float(vela5.replace(",", ".")))
com col6:
    vela6 = st.text_input("6ª vela", "")
    se vela6: vela.append(float(vela6.replace(",", ".")))

def analisar(últimas):
    se len(ultimas) < 5:
        return "âš ï¸ Insira ao menos 5 velas para analisar."

    abaixo_2 = soma(1 para x em ultimas se x < 2)
    acima_5 = soma(1 para x em ultimas se x >= 5)
    media = soma(últimos) / len(últimos)

    se abaixo_2 >= 4:
        return "ðŸ”´ Risco alto de travamento! Provavel abaixo de 2x."
    elif acima_5 >= 2:
        return "ðŸŸ¢ Boa chance de vela acima de 3x!"
    mídia elif > 2,5:
        return "ðŸŸ¢ Tendência positiva. Pode passar 2x."
    outro:
        return "ðŸŸ¡ Zona neutra. Melhor observar."

se len(vela) >= 5:
    st.subheader("ðŸ”® Previsão:")
    resultado = analisar(vela)
    st.success(resultado)
