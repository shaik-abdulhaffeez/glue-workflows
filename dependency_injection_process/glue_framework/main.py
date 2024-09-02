from injector.dependency_injector import DependencyInjector
from manager.glue_job_manager import GlueJobManager
from metadata.metadata_system import MetadataSystem
from jobs.job_a import JobA
from jobs.job_b import JobB

# Initialize Dependency Injector
injector = DependencyInjector()
injector.register("JobA", JobA())
injector.register("JobB", JobB())

# Initialize Glue Job Manager
manager = GlueJobManager(injector)

# Initialize Metadata System
metadata = MetadataSystem()

# Run Jobs
manager.run_job("JobA")
metadata.update_health_state("JobA", "Success")

manager.run_job("JobB")
metadata.update_health_state("JobB", "Success")

# Print Health States
print(metadata.get_health_state("JobA"))
print(metadata.get_health_state("JobB"))
