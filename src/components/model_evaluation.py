from src.logging import logger 
from src.config.entity import ModelEaluationArtifacts, ModelTrainingArtifacts, DataTransfromationArtifacts
from src.config.configuration import ModelEvaluationConfig 
import os 
import mlflow 
from keras.models import load_model
import pandas as pd 
from src.utils.common import read_yaml, store_json, create_file
from sklearn.metrics import accuracy_score, precision_score, recall_score
from src.utils.constants import TARGET_COLUMN

class DataEvaluation:
    def __init__(self, model_trainer_artifacts : ModelTrainingArtifacts, model_evaluation_config : ModelEvaluationConfig, transformed_artifacts : DataTransfromationArtifacts):
        self.artifacts = model_trainer_artifacts
        self.config = model_evaluation_config 
        self.data = transformed_artifacts
    
    def load_data(path : str):
        return pd.read_csv(path)
    
    def initiate_model_evaluation(self):
        try:
            logger.info("Inside model Evaluation")
            os.makedirs(self.config.model_evaluation_root_dir)
            test_data = DataEvaluation.load_data(self.data.valid_test_path)
            get_params = read_yaml(self.config.params)
            logger.info("storing the Test data")
            model = load_model(self.artifacts.model_path)
            x = test_data.drop(columns = [TARGET_COLUMN])
            y = test_data[TARGET_COLUMN]
            pred = self.testondata(x , y , model)
            self.store_scores(y , pred)
            self.store_params(self.config.params)
            logger.info("Model Evaluation Completed")
        except Exception as e:
            raise e

    
    def testondata(self, x , y  , model):
        logger.info("Starting Model Prediction")
        return model.predict(x, verbose = False)
    
    def store_scores(self, y , pred):
        try:
            logger.info("Storing model's performance")
            accuracy = accuracy_score(y , pred)
            precision = precision_score(y , pred)
            recall = recall_score(y , pred)
            data = {
                "accuracy" : accuracy, 
                "precision" : precision, 
                "recall" : recall
            }
            create_file(self.config.model_metrics)
            store_json(data, self.config.model_metrics)
        except Exception as e:
            raise e

    
    def store_params(self , path):
        try:
            logger.info("Storing Model's Metrics")
            data = read_yaml(path)
            create_file(self.config.evaluation_report)
            store_json(data, self.config.evaluation_report)
        except Exception as e:
            raise e
        
        

        
        



