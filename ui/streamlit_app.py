import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.data import generar_datos
from app.model import entrenar_modelo, detectar_anomalias, preparar_datos

st.title("MONI-INT-S")
st.write("simulacion de sensores industriales con machine laerning")

n = st.slider("cantidad de datos", 100, 2000, 1000 )
contamination = st.slider("nivel de anomalias(%)", 1, 10, 2) / 1000

data, reales = generar_datos(n, contamination)

x = preparar_datos(data)

modelo = entrenar_modelo(x, contamination)
anomalias = detectar_anomalias(modelo, x)

fig, ax = plt.subplots()

ax.plot(data, label="temperatura")
ax.scatter(anomalias, data[anomalias], color="red" , label="anomalias detectadas")

ax.set_title("deteccion de anomalias")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Temperatura (ºC)")
ax.legend()

st.pyplot(fig)

st.subheader("resultados")

st.write(f"anomalias detectadas: {len(anomalias[0])}")
st.write(f"anomalias reales: {len(reales)}")