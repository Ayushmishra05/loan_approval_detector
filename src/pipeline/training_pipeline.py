from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_evaluation import DataEvaluation
from src.config.configuration import DataIngestionConfig , TrainingPipelineConfig , DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
from src.components.model_training import ModelTraining
from src.config.entity import ModelTrainingArtifacts



class TrainingPipeline:
    def __init__(self):
        self.trianign = TrainingPipelineConfig()
    
    def data_ingestion(self, training):
        try:
            config = DataIngestionConfig(training)
            ingestion = DataIngestion(config)
            ingestion_artifacts = ingestion.initiate_data_ingestion()
            return ingestion_artifacts
        except Exception as e:
            raise e
    def data_validation(self,  artifacts, training):
        try:
            val_config = DataValidationConfig(training)
            validation = DataValidation(validation_config=val_config , ingestion_artifact=artifacts)
            validation_artifacts = validation.initiate_data_validation()
            return validation_artifacts
        except Exception as e:
            raise e
    def data_transformation(self,  artifacts, training):
        try:
            tran_config = DataTransformationConfig(training)
            transformation = DataTransformation(artifacts , tran_config)
            transformation_artifacts = transformation.initiate_data_transformation()
            return transformation_artifacts
        except Exception as e:
            raise e
    
    def model_training(self, artifacts, training):
        try:
            model_train = ModelTrainerConfig(training)
            trainer = ModelTraining(transformation_Artifacts=artifacts,model_tran_config=model_train )
            arts = trainer.initiate_model_training()
            return arts 
        except Exception as e:
            raise e
    
    def model_eval(self, transformation_artifacts , arts, training):
        try: 
            model_eval = ModelEvaluationConfig(training_pipeline=training)
            model_eval_co = DataEvaluation(arts, model_eval, transformation_artifacts)
            model_eval_co.initiate_model_evaluation()
        except Exception as e:
            raise e
    
    def train(self):
        training = self.trianign
        ingestion = self.data_ingestion(training=training)
        validation = self.data_validation(ingestion, training)
        transformation = self.data_transformation(validation, training)
        model_trainer = self.model_training(transformation, training)
        model_eval = self.model_eval(transformation, model_trainer, training)
    






















