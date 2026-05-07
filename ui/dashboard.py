import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from streamlit_option_menu import option_menu

from app.data import generar_datos
from app.model import preparar_datos, entrenar_modelo,detectar_anomalias, predecir

from ui.components import metric_card, alerta_critica


st.set_page_config(
    page_title="SIMPI",
    layout="wide"
)

with open("ui/styles.css") as f:
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

st.title("SIMPI")
st.subheader("Sistema Inteligente de Monitoreo Predictivo Industrial")

datos, anomalias_reales = generar_datos()

sensor = st.selectbox(
    "Selecciona un sensor",
    datos.columns
)

X = preparar_datos(datos)

modelo = entrenar_modelo(X)

predicciones = predecir(modelo, X)

anomalias = detectar_anomalias(predicciones)


col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card("Sensores Activos", "12")

with col2:
    metric_card("Anomalías", len(anomalias[0]))

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
        anomalias[0],
        datos[sensor].iloc[anomalias[0]],
        color="red",
        label="Anomalías"
    )

    ax.set_title(f"Monitoreo de {sensor}")

    ax.legend()

    st.pyplot(fig)

    """fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(datos, label="Temperatura")
    ax.scatter(
        anomalias[0],
        datos[anomalias[0]],
        color="red",
        label="Anomalías"
    )

    ax.legend()

    st.pyplot(fig)"""

with col2:

    st.subheader("Alertas")

    alerta_critica("Temperatura crítica detectada")

    st.warning("Vibración fuera del rango")

    st.success("Sistema operativo")

with col2:
    metric_card(
        "Anomalías",
        len(anomalias[0])
    )
    