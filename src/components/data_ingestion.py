import os
import zipfile
import gdown
from pathlib import Path
from src.logger import logging
from src.utils.common import get_size
from src.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        with open(self.config.local_data_file, 'w') as f:
            pass

        dataset_url = self.config.source_URL

        file_id = dataset_url.split('/')[-2]
        prefix = 'https://drive.google.com/uc?/export=download&id='
        gdown.download(prefix+file_id,self.config.local_data_file)

        logging.info(f"Downloaded data from {dataset_url} into file {self.config.local_data_file}")

        

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
