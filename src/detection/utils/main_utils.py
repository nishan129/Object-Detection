import os.path
import sys
import yaml
import base64
import uuid
import csv
import cv2
from src.detection.logger import logging
from src.detection.exception import ModelException

def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path, 'r') as file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(file)
    except Exception as e:
        raise ModelException(e,sys)
    
def write_yaml_file(file_path:str , contant:object, replace:bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(file_path, exist_ok=True)
        
        with open(file_path, 'w') as file:
            yaml.safe_dump(contant,file)
            logging.info("Successfully write yaml file")
            
    except Exception as e:
        raise ModelException(e,sys)
    
    
def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open("./data/"+filename, 'wb') as f:
        f.write(imgdata)
        f.close()
        
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())
    
    
def save_result(text, region, csv_filename, folder_path):
    image_name = f"{format(uuid.uuid1())}.jpg"
    
    cv2.imwrite(os.path.join(folder_path, image_name), region)
    with open(csv_filename, mode='a',newline="") as f:
        Csv_writer = csv.writer(f,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        Csv_writer.writerow([image_name,text])