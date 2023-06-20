import os
import zipfile
from pathlib import Path
import urllib.request as request
from src.textsummerizer.logging import logger
from src.textsummerizer.utils.commman import get_size
from src.textsummerizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url= self.config.source_URL,
                filename= self.config.local_data_file
            )    
            logger.info("Downloading the file \n {}".format(header))
        else:
            logger.info("File already exists: {}".format(get_size(Path(self.config.local_data_file))))

    def extract_zip_file(self):
        unzip_path = self.config.unzipped_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
