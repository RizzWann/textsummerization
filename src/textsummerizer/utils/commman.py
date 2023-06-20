import os 
from box.exceptions import BoxValueError
import yaml
from src.textsummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path):
    try:
        with open(path_to_yaml, 'r') as f:
            content = yaml.safe_load(f)
            logger.info(f"Yaml file: {path_to_yaml} loaded")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file empty") 
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_dirs:list,verbose=True):
    for path in path_to_dirs:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory: {path} created")

@ensure_annotations
def get_size(path:Path)->str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb}KBs"