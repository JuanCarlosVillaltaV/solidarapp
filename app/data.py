# app/data.py

import pandas as pd

def cargar_datos_simulados():
    data = {
        "País": ["Afganistán", "Afganistán", "Etiopía", "India"],
        "Región": ["Baghlan", "Balkh", "Tigray", "Bihar"],
        "MPI": [0.36, 0.32, 0.42, 0.31],
        "Población afectada (%)": [48.5, 45.3, 60.2, 49.8]
    }
    return pd.DataFrame(data)
