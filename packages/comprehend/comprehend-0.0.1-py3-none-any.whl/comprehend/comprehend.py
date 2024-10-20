import json
from types import SimpleNamespace

def load_config(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return SimpleNamespace(**data)

def save_config(config, path):
    with open(path, 'w') as file:
        json.dump(vars(config), file, indent=4)