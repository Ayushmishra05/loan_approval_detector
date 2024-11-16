from src.logging import logger 
from src.config.entity import ModelTrainingArtifacts, DataTransfromationArtifacts
from src.config.configuration import ModelTrainerConfig 
import pandas as pd 
from sklearn.preprocessing import StandardScaler 
from tensorflow.keras.layers import Dense, Input 
from tensorflow.keras.models import Sequential 
from src.utils.common import read_yaml
from typing import Any 
from src.utils.constants import TARGET_COLUMN
import os 

class ModelTraining:
    def __init__(self, transformation_Artifacts : DataTransfromationArtifacts, model_tran_config : ModelTrainerConfig):
        self.artifacts = transformation_Artifacts
        self.config = model_tran_config
    
    @staticmethod 
    def get_data(path : str):
        return pd.read_csv(path)
    
    def initiate_model_training(self)->ModelTrainingArtifacts:
        try:
            logger.info("Initiated model Training")
            os.makedirs(self.config.model_root_dir)
            train_data = self.get_data(self.artifacts.train_data_path) 
            valid_data = self.get_data(self.artifacts.valid_test_path)
            train_data = self.clean_model(TARGET_COLUMN , train_data)
            valid_data = self.clean_model(TARGET_COLUMN , valid_data)
            x = train_data.drop(columns = [TARGET_COLUMN])
            y = train_data[TARGET_COLUMN]
            xv = valid_data.drop(columns = [TARGET_COLUMN])
            yv = valid_data[TARGET_COLUMN]
            params = read_yaml(self.config.params)
            model = self.train_model(params, x , y , xv , yv)
            logger.info("Model Trained")
            model.save(self.config.model_root_path)
            logger.info("Model has been Saved")
            return ModelTrainingArtifacts(
                model_path= self.config.model_root_path
            )
        except Exception as e:
            raise e




    

    def train_model(self , params : Any, x , y, xv, yv):
        l1 = Dense(units = int(params.model.l1units), activation = params.model.hidden_activation, input_dim = params.model.input_dim)
        l2 = Dense(units = int(params.model.l2units) , activation = params.model.hidden_activation)
        l3 = Dense(units = int(params.model.l3units) , activation = params.model.hidden_activation)
        l4 = Dense(units = int(params.model.l4units) , activation = params.model.hidden_activation)
        l5 = Dense(units = int(params.model.l5units) , activation = params.model.last_activation)
        model = Sequential()
        model.add(l1)
        model.add(l2)
        model.add(l3)
        model.add(l4)
        model.add(l5)
        model.compile(loss = params.model.loss, metrics = [params.model.metrics], optimizer = params.model.optimizer)
        logger.info("Model has been Compiled")
        model.fit(x , y , epochs = params.model.epochs , validation_data = (xv, yv), verbose = False)
        return model 
    
    def clean_model(self, target : str , data : pd.DataFrame):
        scaler = StandardScaler()
        x = data.drop(columns = [target])
        y = data[target]
        x = pd.DataFrame(scaler.fit_transform(x))
        data = pd.concat([x , pd.DataFrame(y)] , axis = 1)
        return data  

     

