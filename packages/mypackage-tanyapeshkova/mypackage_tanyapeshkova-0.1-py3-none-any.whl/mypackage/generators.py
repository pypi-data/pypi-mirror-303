def simple_generator():
    for i in range(5):
        yield i * 2


if __name__ == "__main__":
 for value in simple_generator():
 print(value)