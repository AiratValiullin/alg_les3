# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import sample

lst = sample(range(20), 10)
max_num = 0
min_num = 20
sum_ = 0
print(lst)
for i in lst:

    if max_num < i: # находим максимальное число
        max_num = i
    if min_num > i: # находим минимальное число
        min_num = i

# Присваиваем значения индексов переменным
max_i = lst.index(max_num)
min_i = lst.index(min_num)

# Делаем срез списка если минимальный элемент слева и считаем сумму значений
if min_i < max_i:
    print(lst[min_i+1:max_i])
    for j in lst[min_i+1:max_i]:
        sum_ = sum_ + j

# Делаем срез списка если минимальный элемент справа и считаем сумму значений
else:
    print(lst[max_i+1:min_i])
    for j in lst[max_i+1:min_i]:
        sum_ = sum_ + j


print(f' сумма элементов {sum_}')
