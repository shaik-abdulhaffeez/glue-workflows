from .base import ETLJob
import logging

class EmailETLJob(ETLJob):
    def extract(self):
        # Simulate email data extraction
        return "email content"

    def transform(self, data):
        # Simulate email data transformation
        return data.replace(" ", "_")

    def load(self, data):
        # Simulate email data loading
        logging.info(f"Email data loaded: {data}")
