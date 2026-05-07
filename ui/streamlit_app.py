import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.data import generar_datos
from app.model import entrenar_modelo, detectar_anomalias, preparar_datos, predecir

st.title("SIMPI")
st.write("Simulación de sensores industriales con Machine Learning")

n = st.slider("cantidad de datos", 100, 2000, 1000 )
contamination = st.slider("Nivel de anomalías (%)", 1, 10, 2) / 100

data, reales = generar_datos(n, contamination)

x = preparar_datos(data)

modelo = entrenar_modelo(x, contamination)
predicciones = predecir(modelo, x)
anomalias = detectar_anomalias(predicciones)

fig, ax = plt.subplots()

ax.plot(data, label="temperatura")
ax.scatter(anomalias[0], data.iloc[anomalias[0]], color="red" , label="anomalias detectadas")

ax.set_title("deteccion de anomalias")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Temperatura (ºC)")
ax.legend()

st.pyplot(fig)

st.subheader("resultados")

st.write(f"Anomalías detectadas: {len(anomalias[0])}")
st.write(f"Anomalías reales: {sum(len(v) for v in reales.values())}")