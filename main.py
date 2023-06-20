from src.textsummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingsPipeline
from src.textsummerizer.logging import logger
from src.textsummerizer.pipeline.satge_02_data_validation import DataValidationPipeline


if __name__ == '__main__':
    logger.info('Starting Data Validation Trainings Pipeline')
    DataValidationPipeline().init_data_validation()
