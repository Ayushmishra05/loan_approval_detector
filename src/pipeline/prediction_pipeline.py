from src.utils.constants import MODEL_FILE_PATH 
from src.logging import logger
from keras.models import load_model 

class PredictionPipeline:
    def __init__(self):
        self.model = load_model(MODEL_FILE_PATH)
    
    def predict(self, data):
        try:
            logger.info("started Prediction")
            output = self.model.predict(data)
            return output
        except Exception as e:
            raise e