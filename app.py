from src.detection.exception import ModelException
from src.detection.logger import logging
from src.detection.constant.training_pipeline import *
import os, sys
from src.detection.pipeline.training_pipeline import TrainingPipeline
from src.detection.utils.main_utils import decodeImage, encodeImageIntoBase64 , save_result
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from src.detection.constant.application import APP_HOST, APP_PORT
from src.detection.configuration.s3_operations import S3Operation
import cv2
import shutil
import pathlib
import easyocr
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/train")
def trainRoute():
    obj = TrainingPipeline()
    obj.run_pipeline()
    return "Training Successfull"


@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 320 --conf 0.5 --source ../data/inputImage.jpg --save-txt")
        
        # Read the resulting image
        result_image = cv2.imread("yolov5/runs/detect/exp/inputImage.jpg")

        # Read the output text file containing object coordinates
        with open("yolov5/runs/detect/exp/labels/inputImage.txt", "r") as file:
            lines = file.readlines()

        # Initialize a variable to store the class IDs
        class_id = []
        reader = easyocr.Reader(['en'])
        # Parse the coordinates and find the class IDs
        for line in lines:
            data = line.strip().split(" ")
            class_id.append(int(data[0]))
        
        # Check if class 1 and class 3 are present in the detected objects
        if 1 in class_id and 3 in class_id:
            for line in lines:
                data = line.strip().split(" ")
                class_id = int(data[0])
                confidence = float(data[1])
                x_center = float(data[1]) * result_image.shape[1]
                y_center = float(data[2]) * result_image.shape[0]
                width = float(data[3]) * result_image.shape[1]
                height = float(data[4]) * result_image.shape[0]
                if class_id == 3:  # Check if the class ID is 3
                    x1 = int(x_center - width / 2)
                    y1 = int(y_center - height / 2)
                    x2 = int(x_center + width / 2)
                    y2 = int(y_center + height / 2)
                    cropped_image = result_image[y1:y2, x1:x2]
                    ocr_result = reader.readtext(cropped_image)
                    save_result(text=ocr_result[0][1],region=cropped_image,csv_filename="number_plate_data.csv",folder_path='run')
            
            
            
        opencodedbase64 = encodeImageIntoBase64(f"yolov5/runs/detect/exp/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        #os.rmdir("yolov5/runs")
        shutil.rmtree("yolov5/runs") 
    except ValueError as val:
        print(val)
        return Response("value not found inside json data")

    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"
    
    return jsonify(result)


@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:

        os.system("cd yolov5/ && python detect.py --weights best.pt --img 320 --conf 0.5 --source 0")
        shutil.rmtree("yolov5/runs") 
        return "Camera starting"
    except ValueError as val:
        print(val)
        return Response("value not found inside json data")
        


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST,port=APP_PORT)