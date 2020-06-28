def fact(n):
  n = int(n)
  if n >= 1:
    return n * fact(n - 1)
  elif n == 0:
    return 1
    
print('vvedite chislo')
print(fact(int(input())))

def fact_test():
  assert fact(5) == 120, "факториал от {}".format(5)
  assert fact(-1) == None, "Факториал от {} ".format(-1)
  assert fact(0) == 1, "факториал от {}".format(0)
  assert fact(5.1) == 120, "факториал от {}".format(5.1)

fact_test()