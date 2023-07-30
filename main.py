from text_summarizer.logging import logger
from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline




STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"---------- {STAGE_NAME} ----------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"====={STAGE_NAME} completed =====")

except Exception as e:
    logger.exception(e)
    raise e