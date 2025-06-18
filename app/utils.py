# app/utils.py

import numpy as np

def calcular_impacto(donacion):
    return int(donacion * np.random.uniform(2, 5))
