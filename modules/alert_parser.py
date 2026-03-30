import json

def load_alerts(path):
    with open(path) as f:
        return json.load(f)