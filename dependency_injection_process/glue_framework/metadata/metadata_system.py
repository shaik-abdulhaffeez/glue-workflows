class MetadataSystem:
    def __init__(self):
        self.health_states = {}

    def update_health_state(self, job_name, state):
        self.health_states[job_name] = state

    def get_health_state(self, job_name):
        return self.health_states.get(job_name, "Unknown")
