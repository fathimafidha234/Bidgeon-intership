from datetime import datetime
from collections import Counter


def log_call(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a") as file:
            file.write(
                f"{timestamp} | {func.__name__} | args={args} | kwargs={kwargs}\n"
            )

        return func(*args, **kwargs)

    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def greet(name):
    print(f"Hello, {name}")


@log_call
def square(num):
    return num * num
add(10, 20)
add(5, 15)

greet("Aslam")
greet("John")

square(4)
square(7)
square(10)


def read_logs():
    counter = Counter()

    with open("log.txt", "r") as file:
        for line in file:
            parts = line.split("|")
            function_name = parts[1].strip()
            counter[function_name] += 1

    print("\nFunction Call Counts")
    print("-" * 25)
    for func, count in counter.items():
        print(f"{func}: {count}")
read_logs()