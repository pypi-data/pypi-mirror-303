import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{end_time - start_time:.3f} seconds")
        return result
    return wrapper

@timeit
def slow_sum(a, b, *, delay):
    time.sleep(delay)
    return a + b



if __name__ == "__main__":
    slow_sum(2, 2, delay=1)  