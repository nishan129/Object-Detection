from src.detection.components.data_ingestion import DataIngestion
from src.detection.logger import logging
from src.detection.exception import ModelException
import sys, os

from src.detection.entity.config_entity import (DataIngestionConfig)

from src.detection.entity.artifact_entity import (DataIngestionArtifact)


class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
        except Exception as e:
            raise ModelException(e,sys)
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Enterd the start_data_ingestion method of TrainingPipeline class")
        logging.info("Getting data from URL")
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifacts=data_ingestion.initiate_data_ingestion()
            
            logging.info("Get the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainingPipeline class")
            
            return data_ingestion_artifacts
        except Exception as e:
            raise ModelException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
        except Exception as e:
            raise ModelException(e,sys)