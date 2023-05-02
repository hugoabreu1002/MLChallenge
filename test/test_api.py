import requests
import json


def test():
    with open('./test/api_test.json') as f:
        json_data = json.load(f)

    prediction = requests.post("http://127.0.0.1:8000/predict", json=json_data)
    print(prediction.json())


if __name__ == "__main__":
    test()
