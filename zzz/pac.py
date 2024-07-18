class Pac:
    def __init__(self, key):
        self.key = key
        self.values = []

    def push(self, element):
        self.values.append(element)

    def pac(self):
        return [self.key] + self.values
