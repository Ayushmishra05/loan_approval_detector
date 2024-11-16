"""This is the Artifact File, where we will be defining our Artifacts 

We are a making a class here, using dataclasses 
"""


from dataclasses import dataclass 
from src.logging import logger 
from ensure import ensure_annotations

@dataclass
class DataIngestionArtifacts:
    data_path : str 

@dataclass
class DataValidationArtifacts:
    validated_data_path : str 
    validation_report_path : str 
    invalidated_data_path : str 
    invalidated_report_path : str 

@dataclass 
class DataTransfromationArtifacts:
    train_data_path : str 
    test_data_path : str 
    valid_test_path : str 

@dataclass 
class ModelTrainingArtifacts:
    model_path : str 

@dataclass 
class ModelEaluationArtifacts:
    model_metrics : str 
    evaluation_report : str 


    



    
