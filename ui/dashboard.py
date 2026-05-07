import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from streamlit_option_menu import option_menu

from app.data import generar_datos
from app.model import preparar_datos, entrenar_modelo, predecir, detectar_anomalias

from ui.components import metric_card, alerta_critica


st.set_page_config(
    page_title="SIMPI",
    layout="wide"
)

with open(os.path.join(os.path.dirname(__file__), "styles.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    seleccion = option_menu(
        "SIMPI",
        [
            "Dashboard",
            "Monitoreo",
            "Alertas",
            "Historial"
        ],
        icons=[
            "speedometer2",
            "activity",
            "bell",
            "clock-history"
        ],
        default_index=0
    )

    st.divider()
    n = st.slider("Cantidad de datos", 100, 2000, 1000)
    contamination = st.slider("Nivel de anomalías (%)", 1, 10, 2) / 100

st.title("SIMPI")
st.subheader("Sistema Inteligente de Monitoreo Predictivo Industrial")

if seleccion == "Dashboard":
    datos, anomalias_reales = generar_datos(n, contamination)

    sensor = st.selectbox("Selecciona un sensor", datos.columns)

    X = preparar_datos(datos)
    modelo = entrenar_modelo(X, contamination)
    predicciones = predecir(modelo, X)
    anomalias = detectar_anomalias(predicciones)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Sensores Activos", "12")

    with col2:
        metric_card("Anomalías", len(anomalias))

    with col3:
        metric_card("Estado", "ÓPTIMO")

    with col4:
        metric_card("Riesgo", "72%")

    st.divider()

    col1, col2 = st.columns([3, 1])

    with col1:
        fig, ax = plt.subplots(figsize=(12, 5))

        ax.plot(
            datos[sensor],
            label=sensor.capitalize()
        )

        ax.scatter(
            anomalias,
            datos[sensor].iloc[anomalias],
            color="red",
            label="Anomalías"
        )

        ax.set_title(f"Monitoreo de {sensor}")
        ax.legend()

        st.pyplot(fig)

    with col2:
        st.subheader("Alertas")

        alerta_critica("Temperatura crítica detectada")
        st.warning("Vibración fuera del rango")
        st.success("Sistema operativo")

elif seleccion == "Monitoreo":
    datos, anomalias_reales = generar_datos(n, contamination)

    st.subheader("Monitoreo en Tiempo Real")

    cols = st.columns(2)
    for i, sensor in enumerate(datos.columns):
        with cols[i % 2]:
            fig, ax = plt.subplots(figsize=(8, 3))
            ax.plot(datos[sensor], label=sensor.capitalize())
            ax.set_title(sensor.capitalize())
            ax.legend()
            st.pyplot(fig)

elif seleccion == "Alertas":
    st.subheader("Centro de Alertas")

    datos, anomalias_reales = generar_datos(n, contamination)
    X = preparar_datos(datos)
    modelo = entrenar_modelo(X, contamination)
    predicciones = predecir(modelo, X)
    anomalias = detectar_anomalias(predicciones)

    st.metric("Total de anomalías detectadas", len(anomalias))

    if len(anomalias) > 0:
        for col in datos.columns:
            indices_col = list(set(anomalias_reales[col]))
            if indices_col:
                alerta_critica(f"{col.capitalize()} - {len(indices_col)} anomalía(s) detectada(s)")
    else:
        st.success("No se detectaron anomalías")

elif seleccion == "Historial":
    st.subheader("Historial de Mediciones")
    st.info("Sección en desarrollo")
