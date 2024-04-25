from src.detection.constant.training_pipeline import *
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str
    feature_store_path: str