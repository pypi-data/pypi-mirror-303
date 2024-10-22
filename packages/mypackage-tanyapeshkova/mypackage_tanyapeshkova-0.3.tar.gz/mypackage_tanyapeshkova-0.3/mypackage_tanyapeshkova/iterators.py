class Iterator:
    def __init__(self, limit):
        self.current = 10
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        current_value = self.current
        self.current += 1
        return current_value

def main(limit):
    iterator = Iterator(limit)
    for number in iterator:
        print(number)


if __name__ == "__main__":
    limit = int(input('Введите предел:'))
    main(limit)