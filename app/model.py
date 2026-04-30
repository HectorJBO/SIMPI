from sklearn.ensemble import IsolationForest
import numpy as np

def preparar_datos(data):
    return data.reshape(-1, 1)

def entrenar_modelo(X, contamination=0.02):
    modelo = IsolationForest(contamination=contamination, random_state=42)
    modelo.fit(X)

    return modelo

def detectar_anomalias(modelo, x):
    pred = modelo.predict(x)
    indices = np.where(pred == -1)

    return indices