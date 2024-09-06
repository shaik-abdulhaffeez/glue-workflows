import concurrent.futures
import threading
import logging

class GlueJob:
    def __init__(self, max_workers=2):
        self.observers = []
        self.max_workers = max_workers

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, job_status):
        def notify_observer(observer):
            thread_name = threading.current_thread().name
            observer.update(job_status, thread_name)

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(notify_observer, observer) for observer in self.observers]
            concurrent.futures.wait(futures)

    def execute(self):
        # Execute job logic
        logging.info("Executing Glue job...")
        # Simulate job completion
        self.notify('Job completed')
