from PoultryGuard.config.configuration import ConfigurationManager
from PoultryGuard.components.data_ingestion import DataIngestion
from PoultryGuard import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngesionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} has started <<<<<")
        obj = DataIngesionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} has completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e