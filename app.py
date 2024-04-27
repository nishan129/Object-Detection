from src.detection.exception import ModelException
from src.detection.logger import logging
from src.detection.constant.training_pipeline import *
import os, sys
from src.detection.pipeline.training_pipeline import TrainingPipeline
from src.detection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from src.detection.constant.application import APP_HOST, APP_PORT
from src.detection.configuration.s3_operations import S3Operation

import shutil
import pathlib
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
        
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 320 --conf 0.5 --source ../data/inputImage.jpg")
        
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