import joblib
import numpy as np

MODEL = None


def load_model():
    with open("./models/best_xgboost.pickle", "rb") as f:
        global MODEL
        MODEL = joblib.load(f)


def make_prediction(data_in: np.array):
    prediction = MODEL.predict(data_in)
    return prediction
