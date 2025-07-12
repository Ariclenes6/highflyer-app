import streamlit as st
import numpy as np

st.set_page_config(page_title="HighFlyer Estratégico", layout="centered")

st.title("🎯 HighFlyer Estratégico - Previsão Manual com Entrada Real")

st.write("Cole abaixo os últimos multiplicadores (ex: `1.22, 1.45, 5.02, 10.12`)")

entrada = st.text_area("📝 Últimos resultados", placeholder="Cole aqui os últimos multiplicadores...")

if entrada:
    try:
        # Processar os dados
        velas = [float(x.strip()) for x in entrada.split(",")]
        ultimas_5 = velas[-5:]
        media = sum(ultimas_5) / len(ultimas_5)
        ult_alta = max(velas)
        abaixo_2x = sum(1 for v in velas[-10:] if v < 2.0)

        st.subheader("📊 Análise do Ciclo Atual")
        st.write(f"Média das últimas 5 velas: **{media:.2f}**")
        st.write(f"Última vela mais alta: **{ult_alta:.2f}x**")
        st.write(f"Velas abaixo de 2x nas últimas 10: **{abaixo_2x}**")

        if abaixo_2x >= 7:
            st.success("🚀 Forte chance de explosão em breve!")
            st.balloons()
        elif media >= 2:
            st.info("📈 Média boa! Possível entrada segura.")
        else:
            st.warning("⚠️ Ciclo fraco. Melhor aguardar.")

    except:
        st.error("❌ Erro: Verifique se você digitou os números corretamente.")
