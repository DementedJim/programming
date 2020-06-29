def wordcounter(s):
  c = 1
  words = s.split(' ')
  for i in words:
     if(i not in '!,.1234567890-+;[]{}'):
       yield print("размер {0}-го слова {1}: {2}".format(c, i, len(i)))
       c+=1

a = input("Введите текст: \t\n")
iterator = wordcounter(a)
try:
    while True:
        item = next(iterator)
except StopIteration:
    pass
finally:
    del iterator