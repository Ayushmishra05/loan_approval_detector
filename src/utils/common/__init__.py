from ensure import ensure_annotations
from src.logging import logger
from box import ConfigBox 
import yaml 
import json

@ensure_annotations
def create_file(path : str):
    try:
        with open(path , 'w') as fp:
            pass 
    
    except Exception as e:
        raise e
    

@ensure_annotations 
def load_yaml(path : str):
    try:
        with open(path , 'r') as fp:
            data = yaml.safe_load(fp)
        return ConfigBox(data)
    except Exception as e:
        raise e


@ensure_annotations 
def save_json(data , path):
    try:
        with open(path , 'w') as fp:
            json.dump(data , fp=fp, indent=4)
    except Exception as e:
        raise e
    
@ensure_annotations 
def read_yaml(path: str):
    try:
        with open(path , 'r') as fp:
            data = yaml.safe_load(fp)
            return ConfigBox(data)
    except Exception as e:
        raise e 


@ensure_annotations 
def store_json(data, path):
    try:
        with open(path, 'w') as fp:
            json.dump(obj=data, fp=fp, indent=4)
    except Exception as e:
        raise e