from src.textsummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingsPipeline
from src.textsummerizer.logging import logger


if __name__ == '__main__':
    logger.info('Starting Data Ingestion Trainings Pipeline')
    DataIngestionTrainingsPipeline().init_data_ingestion_pipeline()
