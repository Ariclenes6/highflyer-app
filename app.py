import streamlit as st

st.set_page_config(page_title="HighFlyer Seguro", layout="centered")
st.title("🧠 HighFlyer - Sistema de Entrada Segura")

st.write("Cole as últimas 20 a 30 velas (ex: `1.21, 1.35, 2.10, 10.34`)")

entrada = st.text_area("🔢 Resultados recentes")

def calcular_score(velas):
    ultimas_5 = velas[-5:]
    ultimas_10 = velas[-10:]
    ultimas_20 = velas[-20:]

    media_5 = sum(ultimas_5) / len(ultimas_5)
    abaixo_2x = sum(1 for x in ultimas_10 if x < 2.0)
    ult_explosao_5x = next((i for i, v in enumerate(reversed(velas)) if v >= 5), None)
    ult_explosao_10x = next((i for i, v in enumerate(reversed(velas)) if v >= 10), None)
    velas_frias = sum(1 for x in ultimas_10 if x <= 1.20)

    score = 0
    if media_5 >= 2.0:
        score += 25
    if abaixo_2x >= 7:
        score += 25
    if ult_explosao_5x is not None and ult_explosao_5x >= 6:
        score += 20
    if ult_explosao_10x is not None and ult_explosao_10x >= 10:
        score += 15
    if velas_frias >= 4:
        score += 15

    return score, media_5, abaixo_2x, velas_frias, ult_explosao_5x, ult_explosao_10x

if entrada:
    try:
        velas = [float(x.strip()) for x in entrada.split(",") if x.strip()]
        score, media, abaixo, frias, last5x, last10x = calcular_score(velas)

        st.subheader("📊 Análise detalhada")
        st.write(f"🔹 Média das últimas 5 velas: **{media:.2f}**")
        st.write(f"🔹 Velas abaixo de 2x (últimas 10): **{abaixo}**")
        st.write(f"🔹 Velas muito baixas (≤ 1.20): **{frias}**")
        st.write(f"🔹 Última explosão 5x: {last5x if last5x is not None else 'N/A'} velas atrás")
        st.write(f"🔹 Última explosão 10x: {last10x if last10x is not None else 'N/A'} velas atrás")

        st.subheader("📈 Score de entrada segura:")
        if score >= 70:
            st.success(f"✅ Entrada recomendada! Score: {score}%")
            st.balloons()
        elif 40 <= score < 70:
            st.warning(f"⚠️ Entrada neutra. Score: {score}%")
        else:
            st.error(f"❌ Evite entrar agora. Score: {score}%")

    except Exception as e:
        st.error(f"Erro ao processar dados: {e}")
