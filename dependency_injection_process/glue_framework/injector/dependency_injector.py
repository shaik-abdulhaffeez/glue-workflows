class DependencyInjector:
    def __init__(self):
        self.dependencies = {}

    def register(self, name, implementation):
        self.dependencies[name] = implementation

    def get(self, name):
        return self.dependencies.get(name)
