from src.textsummerizer.constants import *
from src.textsummerizer.utils.commman import read_yaml,create_directories
from src.textsummerizer.entity import DataIngestionConfig, DataValidationConfig


class ConfigurationManager:
      def __init__(self,
                 config_path = CONFIG_FILE_PATH,
                 params_path = PARAMAS_FILE_PATH):
            self.config = read_yaml(config_path)
            self.params = read_yaml(params_path)
            create_directories([self.config.artifacts_root])

      def get_data_ingestion_config(self)->DataIngestionConfig:
          config = self.config.data_ingestion

          create_directories([config.root_dir])

          data_ingestion_config = DataIngestionConfig(
                root_dir= config.root_dir,
                source_URL= config.source_URL,
                local_data_file= config.local_data_file,
                unzipped_dir= config.unzipped_dir
          )

          return data_ingestion_config

      
      def data_validation(self)->DataValidationConfig:
            config = self.config.data_validation

            create_directories([config.root_dir])

            data_validation = DataValidationConfig(
                  root_dir=config.root_dir,
                  STATUS_FILE=config.STATUS_FILE,
                  ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
            )

            return data_validation
                              