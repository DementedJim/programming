def converter():
  number = int(input('Введите число \n'))
  t = input('Введите название системы счисления: \n')

  if (number == 0):
      print("\n Ноль")
  elif (number == 1):
      print("\n Один")
  elif (number == 2):
      print("\n Два")
  elif (number == 3):
      print("\n Три")
  elif (number == 4):
      print("\n Четыре")
  elif (number == 5):
      print("\n Пять")
  elif (number == 6):
      print("\n Шесть")
  elif (number == 7):
      print("\n Семь")
  elif (number == 8):
      print("\n Восемь")
  elif (number == 9):
      print("\n Девять")
  else:
      print("\n Такой цифры нет")

  if t == 'bin':
      print(bin(number))
  elif t == 'oct':
      print(oct(number))
  elif t == 'hex':
      print(hex(number))

converter()
