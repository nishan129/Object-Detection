import os

ARTIFACTS_DIR : str = "artifacts"


"""
Data ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DATA_NAME: str = "object_detection"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURES_STORE_DIR : str = "features_store"
DATA_DOWNLOAD_URL : str = "https://drive.google.com/file/d/1WR9UJP8CRWaGCBvNz7Httqr6Mhp_B06Z/view?usp=sharing"


"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILE = ["train","val","coco128.yaml"]


"""
Model Trainer related constant start with MODEL_TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16



"""
Model Pusher related constant start with MODEL_PUSHER var name
"""

BUCKET_NAME = "object-halmate-2024"
S3_MODEL_NAME = 'best.pt'