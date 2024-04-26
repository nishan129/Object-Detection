import os, sys
import yaml
from src.detection.logger import logging
from src.detection.exception import ModelException

from src.detection.entity.artifact_entity import  DataIngestionArtifact, ModelTrainerArtifact
from src.detection.entity.config_entity import ModelTrainerConfig
from src.detection.constant.training_pipeline import *
from src.detection.utils.main_utils import read_yaml_file


class ModelTrainer:
    def __init__(self,
                 model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config
        
    
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Enterd initiate_model_trainer method of ModelTrainer class")
        
        try:
            logging.info("Unzipping data")
            os.system("unzip object_detection")
            os.system("rm object_detection")
            
            with open("coco128.yaml", 'r') as strem:
                num_classes = str(yaml.safe_load(strem)['nc'])
                
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)
            
            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            
            config['nc'] = int(num_classes)
            
            with open(f"yolov5/models/custom_{model_config_file_name}.yaml", 'w') as f:
                yaml.dump(config, f)
            
            os.system(f"cd yolov5/ && python train.py --img 320 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../coco128.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.py {self.model_trainer_config.model_trainer_dir}")
            
            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            
            model_trainer_artifact = ModelTrainerArtifact(
                trainer_model_file_path="yolov5/best.pt"
            )
            
            logging.info("Exited initiate_model_trainer metho of ModelTrainer class")
            logging.info(f"Model Trainer artifact: {model_trainer_artifact}")
            
            return model_trainer_artifact
        except Exception as e:
            raise ModelException(e,sys)