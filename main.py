from kidneyDiseasePrediction.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline
)
from kidneyDiseasePrediction.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline
)
from kidneyDiseasePrediction.pipeline.stage_03_model_training import (
    ModelTrainingPipeline
)
from kidneyDiseasePrediction import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = PrepareBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(
        f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x"
    )
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try:
    logger.info("*********************")
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    raise e
