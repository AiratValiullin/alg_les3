# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
a = 0
b = 0
matrix = [[random.randint(0, 50) for i in range(5)] for _ in range(5)]
for t in matrix:
    print(t)
for line in matrix:
    for k in line:
        if a < k:
            a = k
    if b < a:
        b = a
print(b)
