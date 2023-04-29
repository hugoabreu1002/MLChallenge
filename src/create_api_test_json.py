"""
This is a helper script to create a JSON file from the test data.
It is used to test the API. It's not part of the code challenge.
"""
import json
import pandas as pd


def create_json(test_data_frame_path, json_file_path):
    """
    Create a JSON file from the test data.
    """
    df = pd.read_parquet(test_data_frame_path)
    data = df.iloc[0].to_dict()
    with open(json_file_path, 'w') as f:
        json.dump(data, f)


def main():
    test_data_frame = './data/bd_involuntary_turnover_test.parquet'
    json_file_path = './test/api_test.json'
    create_json(test_data_frame, json_file_path)


if __name__ == '__main__':
    main()
