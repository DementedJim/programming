from datetime import datetime


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


calc(1, '+', 100)

