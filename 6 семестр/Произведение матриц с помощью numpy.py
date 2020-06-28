import numpy as np
from datetime import datetime
import time

def multi(matrix1, matrix2):
  '''
  Произведение двух квадратных матриц произвольной размерности
  '''
  start = datetime.now()
  matrix3 = np.dot(matrix1,matrix2)
  print("Время выполнения функции: ", datetime.now() - start)
  return matrix3

if __name__ == "__main__":
    N = int(input("Введите размерность квадратных матриц с произвольными значениями: "))
    A = np.random.randint(10, size=(N,N))
    print(A, "\n")
    B = np.random.randint(10, size=(N,N))
    print(B, "\n")
    print(multi(A,B))
