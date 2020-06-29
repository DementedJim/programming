from datetime import datetime
from functools import partial


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        res = func(*args, **kwargs)
        t = datetime.now()
        with open('log.txt', 'a') as f:
            a, b, c = args
            str = f"{func.__name__}, {a} {b} {c} = {res}, {t}"
            f.write(str)
            f.write("\r\n")
        return res
    return inner


@trace
def calc(op1, action, op2):
    return eval(f"{op1} {action} {op2}")


def main():
    a1 = partial(calc, 1, '+')
    a1(100)


if __name__ == "__main__":
    main()
