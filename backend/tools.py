import json
def load_data():
    # open and read raw data
    with open("backend/data.json") as f:
        # return all data
        return json.load(f)
def get_complaints():
    # call the previous function and extract only the complaint text
    data = load_data()
    return [item["complaint"] for item in data]