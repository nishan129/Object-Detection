from src.detection.logger import logging
from src.detection.exception import ModelException
from src.detection.entity.artifact_entity import DataIngestionArtifact
import os , sys
from src.detection.entity.config_entity import DataIngestionConfig
import zipfile
import gdown
from src.detection.constant.training_pipeline import *


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ModelException(e,sys)
        
    def download_data(self) -> str:
        """This function is to download data from the google drive.

        Returns:
            str: return zipefile path in string format
        """
        try:
            data_set_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingenstion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            zip_file_path = os.path.join(zip_download_dir,DATA_INGESTION_DATA_NAME)
            logging.info(f"Downloading fata from {data_set_url} into file {zip_file_path}")
            file_id = data_set_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_file_path)
            logging.info(f"Downloading fata from {data_set_url} into file {zip_file_path}")
            return zip_file_path
        except Exception as e:
            raise ModelException(e,sys)
        
        
    def extract_zip_file(self,zip_file_path:str)-> str:
        """To this function extract the data from zip file path to zip file to unzip data 

        Args:
            zip_file_path (str): Path of to save download zip file path

        Returns:
            str: To return the extract zip data in file path
        """
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_file_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path,'r') as zip_file:
                zip_file.extractall(feature_store_file_path)
            logging.info(f"Extracting zip file: {zip_file_path} into dir: {feature_store_file_path}")
            
            return feature_store_file_path
        except Exception as e:
            raise ModelException(e,sys)
        
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path=zip_file_path)
            
            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )
            
            logging.info("Exited initiate_data_ingestion method of DataIngestion class")
            logging.info(f"Data ingestion artifacts: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise ModelException(e,sys)