# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

split = 2
list = []

while split < 9:
    for i in range(2, 99):
        if i % split == 0:
            list.append(i)

    print(f'Кртано {split} - {len(list)} чисел')
    list = []
    split += 1

