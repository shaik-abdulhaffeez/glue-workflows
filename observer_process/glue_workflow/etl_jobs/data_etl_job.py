from .base import ETLJob
import logging

class DataETLJob(ETLJob):
    def extract(self):
        # Simulate data extraction
        return "raw data"

    def transform(self, data):
        # Simulate data transformation
        return data.upper()

    def load(self, data):
        # Simulate data loading
        logging.info(f"Data loaded: {data}")
