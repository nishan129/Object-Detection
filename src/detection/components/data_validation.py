from src.detection.logger import logging
from src.detection.exception import ModelException
from src.detection.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
import os , sys, shutil
from src.detection.entity.config_entity import DataValidationConfig
from src.detection.constant.training_pipeline import *


class DataValidation:
    def __init__(self,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise ModelException(e,sys)
        
    def validate_all_file_exist(self) -> bool:
        try:
            validation_status = None
            all_file = os.listdir(self.data_ingestion_artifact.feature_store_path+"/archive (9)")
            
            for file in all_file:
                if file not in  self.data_validation_config.data_validation_required_file:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_data_file_dir, 'w') as f:
                        f.write(f"Validation status {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_data_file_dir, 'w') as f:
                        f.write(f"Validation status {validation_status}")
            
            return validation_status  
        except Exception as e:
            raise ModelException(e,sys)
        
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Entered initiate_data_validation method of Datavalidation class")
        try:
            status = self.validate_all_file_exist()
            data_validation_artifacts = DataValidationArtifact(
                validation_status=status
            )
            logging.info("Exited initiate_data_ingestion method of DataIngestion class")
            logging.info(f"Data ingestion artifacts: {data_validation_artifacts}")
            
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
            
            return data_validation_artifacts
        except Exception as e:
            raise ModelException(e,sys)