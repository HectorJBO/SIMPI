from sklearn.ensemble import IsolationForest
import numpy as np

def preparar_datos(data):
    return data.values

def entrenar_modelo(X, contamination=0.02):
    modelo = IsolationForest(contamination=contamination, random_state=42)
    modelo.fit(X)
    return modelo

def predecir(modelo, X):
    return modelo.predict(X)

def detectar_anomalias(predicciones):
    return np.where(predicciones == -1)[0]