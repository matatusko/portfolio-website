import os, json

def load_json(path:str, key:str=None) -> dict:
    with open(path, 'r') as f:
        data = json.load(f)

    if key: 
        return data.get(key, None)
    
    return data