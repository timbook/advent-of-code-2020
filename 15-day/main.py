data = [20, 9, 11, 0, 1, 2]

class DataList:
    def __init__(self, data):
        self.cache = {}

        for i, n in enumerate(data[:-1]):
            self.cache[n] = i + 1

        self.turn = i + 2
        self.next_add = data[-1]

    def __repr__(self):
        return '\n'.join([f"{key}:{self.cache[key]}" for key in sorted(self.cache)])

    def __len__(self):
        return len(self.cache)

    def add(self):
        if self.turn == 2020:
            self.add_2020 = self.next_add

        if self.turn == 30_000_000:
            self.add_3m = self.next_add

        if self.next_add in self.cache:
            new = self.turn - self.cache[self.next_add]
        else:
            new = 0

        self.cache[self.next_add] = self.turn
        self.next_add = new
        self.turn += 1

dl = DataList(data)
while dl.turn <= 2020:
    dl.add()

n_last = dl.add_2020
print(f"The 2020th number is: {n_last}")

while dl.turn <= 30_000_000:
    dl.add()

n_last = dl.add_3m
print(f"The 2020th number is: {n_last}")
