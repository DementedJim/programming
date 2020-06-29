import numpy as np


def vstr (b):
    b.sort()
    print(b)
    return

def insertion(data):
	for i in range(len(data)):
		j = i - 1
		key = data[i]
		while data[j] > key and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = key
	return data

def parity(m):
    a = []
    b = []
    for x in (m):
        if x % 2 == 0:
            a.append(x)
        else:
            b.append(x)
    print("Четные элементы: ", a)
    print("Нечетные элементы: ", b)


a = list(np.random.randint(0, 10, 10))
print(a)
print(insertion (a))
vstr(a)
parity(insertion(a))
