import os,sys
from src.detection.logger import logging
from src.detection.exception import ModelException
from src.detection.configuration.s3_operations import S3Operation
from src.detection.entity.artifact_entity import ModelTrainerArtifact, ModelPusherArtifact
from src.detection.entity.config_entity import ModelPusherConfig



class ModelPusher:
    def __init__(self,model_pusher_config:ModelPusherConfig, model_trainer_artifact:ModelTrainerArtifact, s3:S3Operation):
        
        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifact = model_trainer_artifact
        self.s3 = s3
        
    def initiate_model_pusher(self) -> ModelPusherArtifact:
        """
        Method Name: initiate_model_pusher
        
        Description: This method intiates model pusher
        
        Output : Model Pusher Artifacts
        """
        
        logging.info("Enterd initate_model_pusher method of ModelPusher class")
        try:
            self.s3.upload_file(
                self.model_trainer_artifact.trainer_model_file_path,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME,
                remove=False
            )
            
            logging.info("Uploaded best model to s3 bucket ")
            logging.info("Exited initiate_model_pusher method of ModelPusher class")
            
            model_pusher_artifact = ModelPusherArtifact(
                bucket_name=self.model_pusher_config.BUCKET_NAME,
                s3_model_path= self.model_pusher_config.S3_MODEL_KEY_PATH
            )
            
            return model_pusher_artifact
        except Exception as e:
            raise ModelException(e,sys)