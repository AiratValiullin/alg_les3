# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

min_ = 100
max_ = 0
list1 = [random.randint(0, 10) for i in range(5)]
print(list1)

for j in list1:
    if j > max_:
        max_ = j
    elif j < min_:
        min_ = int(j)

min_index = list1.index(min_)
max_index = list1.index(max_)

list1[min_index], list1[max_index] = list1[max_index], list1[min_index]

print(list1)
