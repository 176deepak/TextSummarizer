from src.config import configuration
from src.components import data_ingestion

try:
    config = configuration.ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = data_ingestion.DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    raise e