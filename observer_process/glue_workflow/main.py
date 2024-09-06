import logging
from glue_job import GlueJob
from etl_jobs.data_etl_job import DataETLJob
from etl_jobs.log_etl_job import LogETLJob
from etl_jobs.email_etl_job import EmailETLJob
from observers.job_observer import JobObserver

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    job = GlueJob(max_workers=3)
    job.attach(JobObserver(DataETLJob()))
    job.attach(JobObserver(LogETLJob()))
    job.attach(JobObserver(EmailETLJob()))
    job.execute()
