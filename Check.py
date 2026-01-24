class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_value(self):
        return f'Вывод:{self.count}'


class WeightedCounter(Counter):
    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def increment(self):
        self.count += self.weight

    def decrement(self):
        self.count -= self.weight


counter = Counter()
counter.increment()
print(counter.get_value())

weighed_counter = WeightedCounter(weight=2)
weighed_counter.increment()
print(weighed_counter.get_value())