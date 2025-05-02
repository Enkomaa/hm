class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = nested_list[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            top = self.stack.pop()
            if isinstance(top, list):
                self.stack.extend(top[::-1])
            else:
                return top
        raise StopIteration
