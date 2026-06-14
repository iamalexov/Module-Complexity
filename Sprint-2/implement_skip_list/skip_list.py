class SkipList:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)
        self.items.sort()

    def __contains__(self, value):
        return value in self.items

    def to_list(self):
        return self.items.copy()