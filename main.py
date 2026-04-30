import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

np.random.seed(42)

temperaturas = np.random.normal(loc=25, scale=0.5, size=1000)

indice_anomalias = np.random.choice(np.arange(1000), size=15, replace=False)
temperaturas[indice_anomalias] += np.random.uniform(5, 10, size=15)

x = temperaturas.reshape(-1, 1)

modelo = IsolationForest(contamination=0.02, random_state=42)

modelo.fit(x)

prediccion = modelo.predict(x)

anomalias_detectadas = np.where(prediccion == -1)

plt.figure(figsize=(12, 6))
plt.plot(temperaturas, label="temperaturas")

plt.scatter(
    anomalias_detectadas, 
    temperaturas[anomalias_detectadas],
    color="red",
    label="anomalias detectadas"
)

plt.title("deteccion de anomalias con isolation forest")
plt.xlabel("Tiempo")
plt.ylabel("temperaturas (ºC)")
plt.legend()

plt.show()