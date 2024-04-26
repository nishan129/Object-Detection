from src.detection.constant.training_pipeline import *
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str
    feature_store_path: str
    
    
@dataclass
class DataValidationArtifact:
    validation_status : bool
    
@dataclass
class ModelTrainerArtifact:
    trainer_model_file_path: str
    

@dataclass
class ModelPusherArtifact:
    bucket_name: str
    s3_model_path : str