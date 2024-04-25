import os

ARTIFACTS_DIR : str = "artifacts"


"""
Data ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DATA_NAME: str = "object_detection"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURES_STORE_DIR : str = "features_store"
DATA_DOWNLOAD_URL : str = "https://drive.google.com/file/d/1xkkSKgu9Y_AMe4bVp4pParc7zsmrLeha/view?usp=sharing"


"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILE = ["train","val","coco128.yaml"]
