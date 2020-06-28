'''
Иванов Дмитрий Владимирович, ИВТ3
Задание 3
Варинт 5, 6
'''

import math

def volume(l, h):
    D = 2 * math.sqrt (l*l - h*h)
    S = 1/2 * D*D
    V = 1/3 * S * h
    return V

print ("Вариант 5: {}".format(volume(10,6)))

def diagonal(S):
  a = math.sqrt(S / 6)
  d = round(a * math.sqrt(3))
  return d

print ("Вариант 6: {}".format(diagonal(18)))

assert volume(10,8) == 192, "Рассчеты неверны"
assert volume(11,6) == 340, "Рассчеты неверны"
assert volume(5,3) == 32, "Рассчеты неверны"
assert diagonal(18) == 3, "Рассчеты неверны"
assert diagonal(25) == 4, "Рассчеты неверны"
assert diagonal(81) == 6, "Рассчеты неверны"