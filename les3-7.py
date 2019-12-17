# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint

lst = [randint(0, 20) for i in range(6)]
min1 = 100
min2 = 100
print(lst)
for i in lst:
    if min1 > i:
        min1 = i

lst2 = lst[:lst.index(min1)]+lst[lst.index(min1)+1:]

for i in lst2:
    if min2 > i:
        min2 = i

print(f' Первое минимальное число {min1}')
print(f' Второе минимальное число {min2}')
