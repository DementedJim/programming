import random


n = random.randint(0,99)
t = False
while t != True:
  s = input("Введите число: ")
  if int(s) == n:
     print("И вы правильно угадали число {}!".format(s))
     t = True
  else: 
    print("Увы, это было число {}!".format(n))