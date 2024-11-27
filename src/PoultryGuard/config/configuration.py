from PoultryGuard.constants import *
from PoultryGuard.utils.common import read_yaml, create_directories
from PoultryGuard.entity.config_entity import DataIngestionConfig

# Configuration
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ):
        # Read the YAML configuration files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        # Create directories as specified in the configuration
        create_directories([self.config.data_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
