from src.detection.components.data_ingestion import DataIngestion
from src.detection.components.data_validation import DataValidation
from src.detection.logger import logging
from src.detection.exception import ModelException
import sys, os

from src.detection.entity.config_entity import (DataIngestionConfig, DataValidationConfig)

from src.detection.entity.artifact_entity import (DataIngestionArtifact, DataValidationArtifact)


class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
            self.data_validation_config = DataValidationConfig()
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
        
    def start_data_validation(self, data_ingenstion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        logging.info("Enterd the start_data_validation method of TrainingPipeline class")
        try:
            
            data_validation = DataValidation(data_ingestion_artifact=data_ingenstion_artifact,data_validation_config=self.data_validation_config)
            data_validation_artifacts = data_validation.initiate_data_validation()
            logging.info("Exited the start_data_validation method of TrainingPipeline class")
            return data_validation_artifacts
        except Exception as e:
            raise ModelException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validtion_artifacts = self.start_data_validation(data_ingenstion_artifact=data_ingestion_artifacts)
        except Exception as e:
            raise ModelException(e,sys)