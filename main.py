import json
import numpy as np
import uvicorn
from fastapi import FastAPI
from src.predictor import make_prediction, load_model

app = FastAPI()


@app.on_event("startup")  # new
def app_startup():
    load_model()


@app.post("/predict")
def predict(data: dict):
    array_data = np.array(list(data.values())).reshape(1, -1)
    print(array_data.shape)
    prediction = make_prediction(array_data)
    print(prediction)
    return {"prediction": bool(prediction)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
