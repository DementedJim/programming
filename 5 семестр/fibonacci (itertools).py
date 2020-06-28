import itertools


def fibonacci(n):
    list = []
    for i in itertools.count(0):
        if i == 0:
            list += [0]
        if i == 1:
            list += [1]
        if i > 1:
            list += [list[-1] + list[-2]]
        if i == n - 1:
            break
    return list


print('Введите количество чисел в списке Фибоначчи')
n = int(input())
print(fibonacci(n))