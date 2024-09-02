from .glue_job_interface import GlueJobInterface

class JobA(GlueJobInterface):
    def execute(self):
        print("Executing Job A")
