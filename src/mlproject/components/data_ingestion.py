import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd

from dataclasses import dataclass


@dataclass
class DataingestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataingestionConfig()

    def initiate_data_ingestion(self):
        try:
            #reading code
            logging.info("Reading from mysql database")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
        except Exception as e:
            raise CustomException(e.sys)