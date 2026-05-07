from sklearn.ensemble import IsolationForest
import numpy as np

def preparar_datos(data):
    return data.values if hasattr(data, 'values') else data

def entrenar_modelo(X, contamination=0.02):
    modelo = IsolationForest(contamination=contamination, random_state=42)
    modelo.fit(X)

    return modelo

def predecir(modelo, x):
    return modelo.predict(x)

def detectar_anomalias(predicciones):
    # Returns the indices where the prediction is -1 (anomaly)
    indices = np.where(predicciones == -1)
    return indices