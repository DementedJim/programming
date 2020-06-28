'''
Иванов Дмитрий, ИВТ3

Самостоятельная работа 2
Вариант 3
1. Штрих Шеффера (NAND).
6. ((C∨B)→B)∧(A ∧ B)→B
17. ¬(A∨B)→¬(B∨C)
'''

def AandB(a,b):
  return (a and b)


def AorB(a,b):
  return (a or b)


def AimplB(a,b):
  return int(not a or b)


def AnandB(a,b):
  return int(not (AandB(a,b)))

def taskSix(a, b, c):
  return AimplB(AandB (AimplB(AorB(c,b), b), AandB (a,b)), b)

def taskSvntn (a, b, c):
  return AimplB (not AorB(a,b), not AorB(b,c))

def nandTable():
  print('_' * 25)
  print('| a | b | a nand b |')
  print('_' * 25)
  for a in range(2):
    for b in range (2):
      print('| ' + str(a) + ' | ' + str(b) + ' | ' + str(AnandB(a,b)))
  print('_' * 25) 

def taskTable():
  print('_' * 52)
  print('| a | b | c |  ((C∨B)→B)∧(A ∧ B)→B  | ¬(A∨B)→¬(B∨C)|')
  print('_' * 52)
  for a in range(2):
    for b in range(2):
      for c in range (2):
        print('| ' + str(a) + ' | ' + str(b) + ' | ' + str(c) + ' | ' + str(taskSix(a, b, c)) + '| '+ str(taskSvntn(a, b, c)))
  print('_' * 52)


nandTable()
taskTable()
