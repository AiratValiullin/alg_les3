# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный». Это два абсолютно разных значения.

from random import randint

lst = [randint(-10, 10) for i in range(10)]
max_ = -50
max_index = 0

for i in lst:
    if i < 0 and i > max_:
        max_ = i
        max_index = lst.index(i)

print(lst)
print(f' Максимальный отрицательный элемент - {max_} [{max_index}]')
