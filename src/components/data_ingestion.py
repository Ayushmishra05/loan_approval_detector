from src.logging import logger 
from src.config.configuration import DataIngestionConfig 
from src.config.entity import DataIngestionArtifacts 
import pandas as pd 
from pymongo import MongoClient
import os
from src.utils.common import create_file


class DataIngestion:
    def __init__(self, data_inestion_config : DataIngestionConfig):
        self.config = data_inestion_config 
    

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            os.makedirs(self.config.ingestion_dir, exist_ok=True)
            logger.info('Ingestion Directory Created')
            create_file(self.config.ingestion_path_name)
            logger.info('Ingestion File Created')
            data = self.get_data()
            data.to_csv(self.config.ingestion_path_name , index=False)
            logger.info('Ingestion File Loaded and Saved')
            return DataIngestionArtifacts(
                data_path=self.config.ingestion_path_name
            )
        except Exception as e:
            raise e
    

    def get_data(self):
        try:
            logger.info('Inside Mongo Client')
            client = MongoClient(self.config.mongo_client)
            db = client[self.config.db_name]
            logger.info('Loaded Database')
            collection = db[self.config.collection_name]
            logger.info('Loaded Collections')
            data = [ ]
            for doc in collection.find():
                data.append(doc)
            
            logger.info('Loaded Data')
            df = pd.DataFrame(data)
            logger.info('Loaded DataFrame')
            columns = list(df.columns)
            if '_id' in columns:
                df.drop(columns=['_id'] , inplace=True)
            logger.info('Data converted to DataFrame')
            return df
        except Exception as e:
            raise e  



