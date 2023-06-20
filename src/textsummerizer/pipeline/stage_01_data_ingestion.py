from src.textsummerizer.components.data_ingestion import DataIngestion
from src.textsummerizer.config.configuration import ConfigurationManager
from src.textsummerizer.logging import logger
from box.exceptions import BoxValueError

class DataIngestionTrainingsPipeline:
    def __init__(self):
        pass
    def init_data_ingestion_pipeline(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info("Data ingestion Pipeline Initiated Success")
        except BoxValueError as e:
            raise ValueError(e)  