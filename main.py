from text_summarizer.logging import logger
from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from text_summarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline



STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"---------- {STAGE_NAME} ----------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"====={STAGE_NAME} completed =====")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f"---------- {STAGE_NAME} ----------")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"====={STAGE_NAME} completed =====")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation"
try:
    logger.info(f"---------- {STAGE_NAME} ----------")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"====={STAGE_NAME} completed =====")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer"
try:
    logger.info(f"---------- {STAGE_NAME} ----------")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"====={STAGE_NAME} completed =====")

except Exception as e:
    logger.exception(e)
    raise e