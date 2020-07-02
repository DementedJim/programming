def kvadr(max):
    a = 1
    b = 1
    while a < max:
        yield b
        if a == 1:
            a += 1
        b = a ** 2
        a += 1
    return []


def listgen(m):
  l = []
  for n in kvadr(m):
      if int(n / 10) == 0:
          l.append(n)
      elif int(n / 100) == 0:
          l.append(int(n / 10))
          l.append(int(n % 10))
  return l
        

print('Введите максимальное значение квадрата')
max = int(input())
print('Введите номер цифры')
a = int(input()) - 1
print(listgen(max)[a])


if __name__=='__main__':
  assert listgen(5) == [1, 4, 9], ("Функция, считающая количество цифр в числе работает некорректно")


 
