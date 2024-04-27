import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

projetc_name = 'detection'

list_of_files = [
    ".github/workflow/.gitkeep",
    "data/.gitkeep",
    f"src/{projetc_name}/__init__.py",
    f"src/{projetc_name}/components/__init__.py",
    f"src/{projetc_name}/components/data_ingestion.py",
    f"src/{projetc_name}/components/data_validation.py",
    f"src/{projetc_name}/components/model_trainer.py",
    f"src/{projetc_name}/components/model_pusher.py",
    f"src/{projetc_name}/configuration/__init__.py",
    f"src/{projetc_name}/configuration/s3_operations.py",
    f"src/{projetc_name}/constant/__init__.py",
    f"src/{projetc_name}/constant/training_pipeline/__init__.py",
    f"src/{projetc_name}/constant/application.py",
    f"src/{projetc_name}/entity/__init__.py",
    f"src/{projetc_name}/entity/config_entity.py",
    f"src/{projetc_name}/entity/artifact_entity.py",
    f"src/{projetc_name}/exception/__init__.py",
    f"src/{projetc_name}/logger/__init__.py",
    f"src/{projetc_name}/pipeline/__init__.py",
    f"src/{projetc_name}/utils/__init__.py",
    f"src/{projetc_name}/utils/main_utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    ".dockerignore"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
        
    if not(os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    
    else: 
        logging.info(f"{filename} is already exists")