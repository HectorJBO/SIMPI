import numpy as np
import pandas as pd

def generar_datos(n=1000, contamination=0.02, seed=42):
    np.random.seed(seed)

    datos = pd.DataFrame({"temperatura": np.random.normal(25, 0.5, n),
                          "vibracion": np.random.normal(50, 5, n),
                           "presion": np.random.normal(30, 2, n),
                            "humedad": np.random.normal(15, 3, n) 
                            })

    anomalias = {}

    for columnas in datos.columns:

        num_anomalias = int(n * contamination)
        indices = np.random.choice(np.arange(n), size=num_anomalias, replace=False)

        datos.loc[indices, columnas] += np.random.uniform(10, 20, size=num_anomalias)

        anomalias[columnas] = indices

    return datos, anomalias