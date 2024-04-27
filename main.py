from src.detection.logger import logging 
from src.detection.pipeline.training_pipeline import TrainingPipeline
from src.detection.constant.training_pipeline import *
from src.detection.configuration.s3_operations import S3Operation


if __name__ == '__main__':
    obj = TrainingPipeline()
    obj.run_pipeline()


    