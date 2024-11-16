from src.logging import logger 
from src.utils.constants import (
    DB_NAME, COLLECTION_NAME, ROOT_ARTIFACT_NAME, DATA_INGESTION_DIR_NAME, DATA_INGESTION_DATA_PATH_NAME, 
    DATA_VALIDATION_DIR, VALID_DATA_PATH, VALID_ROOT_DIR , 
    INVALID_DATA_PATH , INVALID_ROOT_DIR, VALID_REPORT_PATH, INVALID_REPORT_PATH, 
    DATA_TRANSFORMATION_ROOT_DIR, TRANSFORMED_TEST_DATA, TRANSFORMED_TRAIN_DATA,
    TRANSFORMED_VALID_DATA, TRANSFORMED_TEST_PATH, TRANSFORMED_TRAIN_PATH, TRANSFORMED_VALID_PATH, 
    MODEL_PATH, MODEL_ROOT_DIR, SCHEMA_FILE_PATH, MODEL_EVALUATION_ROOT, MODEL_METRICS, EVALUATION_REPORT, 
    MODEL_FILE_PATH)
from dotenv import load_dotenv 
load_dotenv()
import os 
MONGO_URL = os.environ['MONGO_CLIENT']
from datetime import datetime 


class TrainingPipelineConfig:
    def __init__(self):

        self.root_artifact_name = ROOT_ARTIFACT_NAME
        self.inside_root_artifact_name = f"{datetime.now().strftime("%d_%m_%Y_%M_%H")}/"
        self.artifact_dir = f"{self.root_artifact_name}/{self.inside_root_artifact_name}"
        os.makedirs(self.artifact_dir, exist_ok= True)
        logger.info('Created Artifacts Directory')


class DataIngestionConfig:
    def __init__(self, training_pipeline : TrainingPipelineConfig):
        self.ingestion_dir = os.path.join(training_pipeline.artifact_dir , DATA_INGESTION_DIR_NAME)
        self.ingestion_path_name = os.path.join(self.ingestion_dir, DATA_INGESTION_DATA_PATH_NAME)
        self.mongo_client = MONGO_URL
        self.collection_name = COLLECTION_NAME
        self.db_name = DB_NAME
        

class DataValidationConfig:
    def __init__(self, training_pipeline : TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeline.artifact_dir, DATA_VALIDATION_DIR)
        self.valid_root_dir = os.path.join(self.data_validation_dir, VALID_ROOT_DIR)
        self.invalid_root_dir = os.path.join(self.data_validation_dir, INVALID_ROOT_DIR)
        self.valid_data_path = os.path.join(self.valid_root_dir , VALID_DATA_PATH)
        self.invalid_data_path = os.path.join(self.invalid_root_dir , INVALID_DATA_PATH)
        self.valid_report_path = os.path.join(self.valid_root_dir , VALID_REPORT_PATH)
        self.invalid_report_path = os.path.join(self.invalid_root_dir , INVALID_REPORT_PATH)


class DataTransformationConfig:
    def __init__(self, trainign_pipeline : TrainingPipelineConfig):
        self.data_transformation_dir = os.path.join(trainign_pipeline.artifact_dir , DATA_TRANSFORMATION_ROOT_DIR)
        self.transformed_train_data = os.path.join(self.data_transformation_dir , TRANSFORMED_TRAIN_DATA)
        self.transformed_test_data = os.path.join(self.data_transformation_dir , TRANSFORMED_TEST_DATA)
        self.transformed_valid_data = os.path.join(self.data_transformation_dir, TRANSFORMED_VALID_DATA)
        self.train_path = os.path.join(self.transformed_train_data , TRANSFORMED_TRAIN_PATH)
        self.test_path = os.path.join(self.transformed_test_data , TRANSFORMED_TEST_PATH)
        self.valid_path = os.path.join(self.transformed_valid_data , TRANSFORMED_VALID_PATH)

class ModelTrainerConfig:
    def __init__(self, training_pipeline : TrainingPipelineConfig):
        self.model_root_dir = os.path.join(training_pipeline.artifact_dir , MODEL_ROOT_DIR)
        self.model_root_path = os.path.join(self.model_root_dir , MODEL_PATH)
        self.params = SCHEMA_FILE_PATH 

class ModelEvaluationConfig:
    def __init__(self, training_pipeline : TrainingPipelineConfig):
        self.model_evaluation_root_dir = os.path.join(training_pipeline.artifact_dir , MODEL_EVALUATION_ROOT)
        self.model_metrics = os.path.join(self.model_evaluation_root_dir , MODEL_METRICS)
        self.evaluation_report = os.path.join(self.model_evaluation_root_dir , EVALUATION_REPORT)
        self.params = SCHEMA_FILE_PATH 
        self.models_path = MODEL_FILE_PATH


