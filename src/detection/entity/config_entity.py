from src.detection.constant.training_pipeline import *
import os
from src.detection.exception import ModelException
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    artifact_dir: str = os.path.join(ARTIFACTS_DIR,TIMESTAMP)
    
        
training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingenstion_dir: str = os.path.join(
        training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME
    )
    
    feature_store_file_path: str = os.path.join(
        data_ingenstion_dir, DATA_INGESTION_FEATURES_STORE_DIR
    )
    data_download_url: str = DATA_DOWNLOAD_URL
    
    
@dataclass
class DataValidationConfig:
    data_validation_dir : str = os.path.join(
        training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME
    )
    
    valid_data_file_dir: str = os.path.join(data_validation_dir,DATA_VALIDATION_STATUS_FILE)
    
    data_validation_required_file = DATA_VALIDATION_ALL_REQUIRED_FILE 
    
@dataclass
class ModelTrainerConfig:
    model_trainer_dir : str = os.path.join(
        training_pipeline_config.artifact_dir , MODEL_TRAINER_DIR_NAME
    )
    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    
    no_epochs = MODEL_TRAINER_NO_EPOCHS
    
    batch_size = MODEL_TRAINER_BATCH_SIZE
    
    