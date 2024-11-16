from src.logging import logger 
from src.config.configuration import DataValidationConfig
from src.config.entity import DataIngestionArtifacts, DataValidationArtifacts
import pandas as pd 
from src.utils.constants import PARAMS_FILE_PATH
from src.utils.common import load_yaml , save_json, create_file
import os 
import numpy as np 
class DataValidation:
    def __init__(self, ingestion_artifact : DataIngestionArtifacts , validation_config : DataValidationConfig):
        self.config = validation_config 
        self.artifacts = ingestion_artifact 

    @staticmethod
    def load_csv(data):
        return pd.read_csv(data)
    def initiate_data_validation(self) -> DataValidationArtifacts:
        try:
            os.makedirs(self.config.data_validation_dir , exist_ok=True)
            os.makedirs(self.config.valid_root_dir, exist_ok= True)
            os.makedirs(self.config.invalid_root_dir, exist_ok=True)
            logger.info('Initiating Data Validation')
            data_path = self.artifacts.data_path 
            data = DataValidation.load_csv(data_path)
            logger.info('Loaded Data')
            validation_report = self.validating_column(data)
            logger.info('Tested Validation Report')
            datatype_report = self.validating_dtype(data)
            logger.info('Tested Datatype Report')
            is_null = np.array(data.isnull().sum()).sum()
            report = {
                'Columns' : str(validation_report), 
                'DataType' : str(datatype_report), 
                'Null Values' : str(is_null)
            }
            logger.info('Generated Report')

            
            if validation_report and datatype_report and is_null== 0:
                create_file(self.config.valid_data_path)
                create_file(self.config.valid_report_path)
                data.to_csv(self.config.valid_data_path , index=False)
                logger.info('Validation File Updated')
                save_json(report, self.config.valid_report_path)
                logger.info('Metrics File Updated')
                return DataValidationArtifacts(
                    validated_data_path= self.config.valid_data_path, 
                    validation_report_path=self.config.valid_report_path, 
                    invalidated_data_path=None, 
                    invalidated_report_path=None
                )
            
            else:
                create_file(self.config.invalid_report_path)
                create_file(self.config.invalid_data_path)
                data.to_csv(self.config.invalid_data_path , index = False)
                logger.info('Invalid File Updated')
                save_json(report , self.config.invalid_report_path )
                logger.info('Invalid Report Updated')
                return DataValidationArtifacts(
                    validated_data_path=None, 
                    validation_report_path=None, 
                    invalidated_data_path=self.config.valid_data_path, 
                    invalidated_report_path=self.config.invalid_report_path
                )
        except Exception as e:
            raise e    
    

    def validating_column(self, data : pd.DataFrame):
        try:
            data_columns = list(data.columns)
            actual_columns = load_yaml(PARAMS_FILE_PATH)
            column_report = True 
            for cols in data_columns:
                if cols not in actual_columns.columns:
                    column_report = False 
            
            return column_report 
        except Exception as e:
            raise e
    
    def validating_dtype(self, data: pd.DataFrame):
        try:
            cols = list(data.columns) 
            actual_dtypes = list(load_yaml(PARAMS_FILE_PATH).columns.values())
            report = True 
            for col in cols:
                data_dtype = str(data[col].dtype)
                if data_dtype not in actual_dtypes:
                    report = False 
            return report 
        except Exception as e:
            raise e
        


        

        

        
        
