import streamlit as st

st.set_page_config(page_title="HighFlyer Previsão Rápida", layout="centered")
st.title("🚀 HighFlyer - Previsão Instantânea de Vela Segura")

st.write("Cole os últimos multiplicadores (20 a 30 velas):\n\nExemplo: `1.21, 1.18, 2.10, 1.05, 10.20`")

entrada = st.text_area("🔢 Resultados recentes")

def analisar_velas(velas):
    ult_5 = velas[-5:]
    ult_10 = velas[-10:]
    ult_20 = velas[-20:]

    media_5 = sum(ult_5) / 5
    abaixo_2 = sum(1 for x in ult_10 if x < 2)
    frias = sum(1 for x in ult_10 if x <= 1.20)
    sem_5x = next((i for i, v in enumerate(reversed(velas)) if v >= 5), len(velas))
    sem_10x = next((i for i, v in enumerate(reversed(velas)) if v >= 10), len(velas))

    score = 0
    if media_5 >= 2.0: score += 20
    if abaixo_2 >= 6: score += 20
    if frias >= 3: score += 20
    if sem_5x >= 7: score += 20
    if sem_10x >= 10: score += 20

    return score, media_5, abaixo_2, frias, sem_5x, sem_10x

if entrada:
    try:
        velas = [float(x.strip()) for x in entrada.split(",") if x.strip()]
        score, media, abaixo, frias, no5x, no10x = analisar_velas(velas)

        st.subheader("📊 Análise")
        st.write(f"🔹 Média últimas 5: **{media:.2f}**")
        st.write(f"🔹 Velas abaixo de 2x (10 últimas): **{abaixo}**")
        st.write(f"🔹 Velas muito frias (≤1.20): **{frias}**")
        st.write(f"🔹 Sem vela 5x há: **{no5x}** velas")
        st.write(f"🔹 Sem vela 10x há: **{no10x}** velas")
        
        st.subheader("🧠 Previsão da PRÓXIMA vela")

        if score >= 80:
            st.success(f"✅ Entrada altamente recomendada! Score: {score}%")
            st.balloons()
            st.markdown("💥 Provável explosão acima de 2x na próxima vela!")
        elif 60 <= score < 80:
            st.warning(f"⚠️ Entrada possível com cautela. Score: {score}%")
        else:
            st.error(f"❌ Não entre agora. Score: {score}%")

    except Exception as e:
        st.error("Erro ao processar os dados. Verifique os números colados.")
