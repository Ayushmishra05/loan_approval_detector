from src.logging import logger 
import pandas as pd 
from src.config.entity import DataTransfromationArtifacts , DataValidationArtifacts
from src.config.configuration import DataTransformationConfig
from sklearn.preprocessing import OneHotEncoder 
from sklearn.model_selection import train_test_split 
import numpy as np
import os  
from src.utils.common import create_file




class DataTransformation:
    def __init__(self, data_validation_artifacts : DataValidationArtifacts , data_transformation_config : DataTransformationConfig):
        self.config = data_transformation_config
        self.artifacts = data_validation_artifacts
    
    @staticmethod
    def get_data(data):
        return pd.read_csv(data)
    def initiate_data_transformation(self) -> DataTransfromationArtifacts:
        try:
            logger.info("Initiated Data Transformation")
            data = self.get_data(self.artifacts.validated_data_path)
            os.makedirs(self.config.data_transformation_dir, exist_ok= True)
            os.makedirs(self.config.transformed_train_data , exist_ok=True)
            os.makedirs(self.config.transformed_test_data , exist_ok=True)
            os.makedirs(self.config.transformed_valid_data , exist_ok=True)
            data =self.ohe_data(data=data)
            logger.info("OHE Completed for the data")
            self.split_data_and_save(data)
            logger.info("Data has been Splitted and has been stored ")
            return DataTransfromationArtifacts(
                train_data_path=self.config.train_path, 
                test_data_path=self.config.test_path, 
                valid_test_path=self.config.valid_path
            )
        except Exception as e:
            raise e
        
    
    def ohe_data(self, data : pd.DataFrame):
        try:
            data = pd.get_dummies(data, columns= ['person_gender', 'person_education', 'person_home_ownership', 'loan_intent', 'previous_loan_defaults_on_file'], drop_first=True)
            for col in data:
                if data[col].dtype == 'bool':
                    data[col] = np.where(data[col] == False , 0 , 1)
            return data
        except Exception as e:
            raise e
    
    def split_data_and_save(self, data : pd.DataFrame):
        try:
            train_data, test_data = train_test_split(data, test_size=0.2 , random_state=42)
            train_data , valid_data = train_test_split(train_data , test_size=0.3 , random_state=42)

            create_file(self.config.train_path)
            create_file(self.config.test_path)
            create_file(self.config.valid_path)
            train_data.to_csv(self.config.train_path , index = False)
            test_data.to_csv(self.config.test_path , index = False)
            valid_data.to_csv(self.config.valid_path , index = False)
        except Exception as e:
            raise e



