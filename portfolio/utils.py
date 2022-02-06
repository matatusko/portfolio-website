import json
from flask import current_app

def load_json(path:str, key:str=None) -> dict:
    with current_app.open_resource(path, 'r') as f:
        data = json.load(f)

    if key: 
        return data.get(key, None)
    
    return data