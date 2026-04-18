import json

def load_data():
    with open("data.json") as f:
        return json.load(f)

def get_complaints():
    