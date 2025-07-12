import streamlit as st

st.set_page_config(page_title="HighFlyer Previsão Rápida", layout="centered")
st.title("🚀 HighFlyer - Previsão Instantânea da Próxima Vela")

st.write("Digite ou cole os **últimos 6 multiplicadores** do HighFlyer:")
st.write("Exemplo: `1.23, 1.01, 2.10, 1.05, 3.45, 5.12`")

entrada = st.text_area("🔢 Resultados recentes (mínimo 6)", height=100)

def analisar_velas(velas):
    ult_5 = velas[-5:]
    ult_6 = velas[-6:]

    media_5 = sum(ult_5) / 5
    abaixo_2 = sum(1 for x in ult_6 if x < 2)
    frias = sum(1 for x in ult_6 if x <= 1.20)
    sem_5x = next((i for i, v in enumerate(reversed(velas)) if v >= 5), len(velas))
    sem_10x = next((i for i, v in enumerate(reversed(velas)) if v >= 10), len(velas))

    score = 0
    if media_5 >= 2.0: score += 30
    if abaixo_2 >= 4: score += 30
    if frias >= 2: score += 20
    if sem_5x >= 5: score += 10
    if sem_10x >= 6: score += 10

    return score, media_5, abaixo_2, frias, sem_5x, sem_10x

if entrada:
    try:
        velas = [float(x.strip()) for x in entrada.split(",") if x.strip()]
        if len(velas) < 6:
            st.warning("⚠️ Por favor, insira pelo menos 6 multiplicadores.")
        else:
            score, media, abaixo, frias, no5x, no10x = analisar_velas(velas)

            st.subheader("📊 Análise")
            st.write(f"🔹 Média últimas 5: **{media:.2f}**")
            st.write(f"🔹 Velas abaixo de 2x: **{abaixo}**")
            st.write(f"🔹 Velas frias (≤1.20): **{frias}**")
            st.write(f"🔹 Sem vela 5x há: **{no5x}** velas")
            st.write(f"🔹 Sem vela 10x há: **{no10x}** velas")

            st.subheader("🧠 Previsão da PRÓXIMA vela")

            if score >= 70:
                st.success(f"✅ Entrada recomendada! Score: {score}%")
                st.balloons()
                st.markdown("🔥 Alta chance de explosão acima de 2x na próxima vela!")
            elif 50 <= score < 70:
                st.warning(f"⚠️ Entrada com cautela. Score: {score}%")
            else:
                st.error(f"❌ Evite entrada. Score: {score}%")

    except Exception as e:
        st.error(f"Erro ao processar os dados: {e}")
        
