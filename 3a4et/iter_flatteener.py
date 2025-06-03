class FlattenIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.reset()

    def reset(self):
        self.stack = list(reversed(self.nested_list))

    def __iter__(self):
        self.reset()
        return self

    def __next__(self):
        while self.stack:
            current = self.stack.pop()
            if isinstance(current, list):
                self.stack.extend(reversed(current))
            else:
                return current
        raise StopIteration
