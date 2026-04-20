# utils/preprocessor.py

import numpy as np

def encode_yes_no(value):
    return 1 if value.lower() == "yes" else 0

def normalize_input(values):
    return np.array(values).reshape(1, -1)

def load_model(path):
    import joblib
    return joblib.load(path)
