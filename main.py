from src.config import configuration
from src.components import model_trainer

try:
    config = configuration.ConfigurationManager()
    model_trainer_config = config.get_model_trainer_config()
    model_trainer_config = model_trainer.ModelTrainer(config=model_trainer_config)
    model_trainer_config.train()
except Exception as e:
    raise e