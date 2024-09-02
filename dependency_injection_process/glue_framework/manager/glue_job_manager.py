class GlueJobManager:
    def __init__(self, injector):
        self.injector = injector

    def run_job(self, job_name):
        job = self.injector.get(job_name)
        if job:
            job.execute()
        else:
            print(f"Job {job_name} not found")
