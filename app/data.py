import numpy as np

def generar_datos(n=1000, contamination=0.02):
    np.random.seed(42)

    data = np.random.normal(25, 0.5, n)

    num_anomalias = int(n* contamination)
    indices = np.random.choice(np.arange(n), size=num_anomalias, replace=False)
    data[indices] += np.random.uniform(5, 10, size=num_anomalias)

    return data, indices