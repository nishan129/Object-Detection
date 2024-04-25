from src.detection.logger import logging 
from src.detection.pipeline.training_pipeline import TrainingPipeline


if __name__ == '__main__':
    obj = TrainingPipeline()
    obj.run_pipeline()


    