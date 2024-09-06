class ETLJob:
    def extract(self):
        raise NotImplementedError

    def transform(self, data):
        raise NotImplementedError

    def load(self, data):
        raise NotImplementedError
