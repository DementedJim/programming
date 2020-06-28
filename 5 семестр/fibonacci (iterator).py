class FibIter:

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
        self.a, self.b = 0, 1

    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration
        result = self.a + self.b
        self.a = result
        self.a, self.b = self.b, self.a
        self.counter += 1
        return result


print('Введите количество чисел в списке Фибоначчи')
num = int(input())
fibinit = FibIter(num)
list = []
for i in range(num):
        if i == 0:
            list += [0]
        elif i == 1:
            list += [1]
        else:
            list += [next(fibinit)]
print(list)