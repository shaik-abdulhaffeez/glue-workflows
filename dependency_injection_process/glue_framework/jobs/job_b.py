from .glue_job_interface import GlueJobInterface

class JobB(GlueJobInterface):
    def execute(self):
        print("Executing Job B")
