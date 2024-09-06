from .base import Observer
import logging

class JobObserver(Observer):
    def __init__(self, etl_job):
        self.etl_job = etl_job

    def update(self, job_status, thread_name):
        logging.info(f"{thread_name}: JobObserver - Starting ETL job...")
        data = self.etl_job.extract()
        transformed_data = self.etl_job.transform(data)
        self.etl_job.load(transformed_data)
        logging.info(f"{thread_name}: JobObserver - Job status updated: {job_status}")
