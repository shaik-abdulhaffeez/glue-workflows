from .base import ETLJob
import logging

class LogETLJob(ETLJob):
    def extract(self):
        # Simulate log extraction
        return "log data"

    def transform(self, data):
        # Simulate log transformation
        return data.lower()

    def load(self, data):
        # Simulate log loading
        logging.info(f"Logs loaded: {data}")
