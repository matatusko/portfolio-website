import os
import json
from pathlib import Path
from flask import current_app

def get_files_from_path(path:Path, ext:str='') -> list:
    full_path = current_app.root_path/path
    return [x for x in os.listdir(full_path) if x.endswith(ext)]

def load_json(path:Path, key:str=None) -> dict:
    with current_app.open_resource(path, 'r') as f:
        data = json.load(f)

    if key: 
        return data.get(key, None)
    
    return data