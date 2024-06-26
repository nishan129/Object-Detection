from src.detection.components.data_ingestion import DataIngestion
from src.detection.components.data_validation import DataValidation
from src.detection.components.model_trainer import ModelTrainer
from src.detection.components.model_pusher import ModelPusher
from src.detection.configuration.s3_operations import S3Operation
from src.detection.logger import logging
from src.detection.exception import ModelException
import sys, os

from src.detection.entity.config_entity import (DataIngestionConfig, DataValidationConfig, ModelTrainerConfig, ModelPusherConfig)

from src.detection.entity.artifact_entity import (DataIngestionArtifact, DataValidationArtifact, ModelTrainerArtifact, ModelPusherArtifact)


class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
            self.data_validation_config = DataValidationConfig()
            self.model_trainer_config = ModelTrainerConfig()
            self.model_pusher_config = ModelPusherConfig()
            self.s3_operations = S3Operation()
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
        
    def start_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Enterd the start_model_trainer method of TrainingPipeline class")
        try:
            model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            logging.info("Exited the start_data_validation method of TrainingPipeline class")
            return model_trainer_artifact
        except Exception as e:
            raise ModelException(e,sys)
        
    def start_model_pusher(self, model_trainer_articat: ModelTrainerArtifact) ->ModelPusherArtifact:
        logging.info("Enterd the start_model_pusher method of TrainingPipeline class")
        try:
            model_pusher = ModelPusher(model_pusher_config=self.model_pusher_config,
                                       model_trainer_artifact=model_trainer_articat,
                                       s3=self.s3_operations)
            model_pusher_artifacts =model_pusher.initiate_model_pusher()
            logging.info("Exist the start_model_pusher method of TrainingPipeline class")
            return model_pusher_artifacts
        except Exception as e:
            raise ModelException(e,sys)
        
        
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validtion_artifacts = self.start_data_validation(data_ingenstion_artifact=data_ingestion_artifacts)
            
            if data_validtion_artifacts.validation_status == True:
                model_trainer_artifacts = self.start_model_trainer()
            
                model_pusher = self.start_model_pusher(model_trainer_articat=model_trainer_artifacts)
        except Exception as e:
            raise ModelException(e,sys)