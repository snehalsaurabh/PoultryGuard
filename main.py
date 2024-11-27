from PoultryGuard import logger
from PoultryGuard.pipeline.stage_01_data_ingestion import DataIngesionTrainingPipeline

STAGE_NAME = DataIngesionTrainingPipeline

try:
    logger.info(f">>>>> {STAGE_NAME} has started <<<<<")
    obj = DataIngesionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} has completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e