# 4. Определить, какое число в массиве встречается чаще всего.

import random
list1 = [random.randint(0, 10) for i in range(20)]
print(list1)
k = 0

for j in list1:
    if list1.count(j) > list1.count(k):
        k = j

print(f' Число {k},  встречается чаще остальных')