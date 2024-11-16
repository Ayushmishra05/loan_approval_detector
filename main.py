from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_evaluation import DataEvaluation
from src.config.configuration import DataIngestionConfig , TrainingPipelineConfig , DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
from src.components.model_training import ModelTraining
from src.config.entity import ModelTrainingArtifacts


trianign = TrainingPipelineConfig()
config = DataIngestionConfig(trianign)
ingestion = DataIngestion(config)
ingestion_artifacts = ingestion.initiate_data_ingestion()

val_config = DataValidationConfig(trianign)
validation = DataValidation(validation_config=val_config , ingestion_artifact=ingestion_artifacts)
validation_artifacts = validation.initiate_data_validation()

tran_config = DataTransformationConfig(trianign)
transformation = DataTransformation(validation_artifacts , tran_config)
transformation_artifacts = transformation.initiate_data_transformation()


model_train = ModelTrainerConfig(trianign)
trainer = ModelTraining(transformation_Artifacts=transformation_artifacts,model_tran_config=model_train )
arts = trainer.initiate_model_training()


model_eval = ModelEvaluationConfig(training_pipeline=trianign)
model_eval_co = DataEvaluation(arts, model_eval, transformation_artifacts)
model_eval_co.initiate_model_evaluation()
