

from src.textsummerizer.components.data_validation import DataValidation
from src.textsummerizer.config.configuration import ConfigurationManager


class DataValidationPipeline:
    def __init__(self):
        pass

    def init_data_validation(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.data_validation()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exists()
    
        except Exception as e:
                raise e  