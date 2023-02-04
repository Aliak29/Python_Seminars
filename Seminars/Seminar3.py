# 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# [1, 2, 2, 3, 5, 6]
# -> 5
# 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# [1, 2, 2, 3, 5, 6]
# -> 5

list = [1, 2, 2, 3, 5, 6]
print(len(set(list)))

import random
def random_int_list (length, min, max):
    list = []
    for i in range (length):
        list.append(random.randint(min,max))
    return list

length_input = int(input("Введите длину списка: "))
min_input = int(input("Введите минимальное значение списка: "))
max_input = int(input("Введите максимальное значение списка: "))
list1 = random_int_list(length_input, min_input, max_input)
print(list1)
set1 = set(list1)
print(set1)
print(len(set1))


# 2. Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# [1, 2, 3, 4, 5]
# 3
# -> [3, 4, 5, 1, 2]

start_lst = [1, 2, 3, 4, 5]
k = int(input('k: '))
k = -(k%len(start_lst))
result_llst = []

for i in range(len(start_lst)):
    result_llst.append(start_lst[k])
    k += 1

print(result_llst)


if k<0
    def shift(lst, steps):
        if steps < 0:
            steps = abs(steps)
            for i in range(steps):
                lst.append(lst.pop(0))
        else:
            for i in range(steps):
                lst.insert(0, lst.pop())

#print(*set(list.values()))

# 3. Напишите программу для печати всех уникальных значений в словаре.
# {
#     1: 'V',
#     4: 'C',
#     'ew': 'C'
# }
# -> V, C

list = [{'1':'V'}, {'4': 'C'}, {'ew': 'C'}]
print('Изначальный список: ',list)
unique_value = set( value for dictionary in list for value in dictionary.values())
print('Уникальные значения: ',unique_value)



# 4. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)
# [6, 9, 3, 6, 87, 1, 3]
# -> 4

list = [6, 9, 3, 6, 87, 1, 3]
k = 0
for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        k += 1
print(k)


start = [6, 9, 3, 6, 87, 1, 3]
count = 0
temp = start[0]
for item in start[1:]:
    if item > temp:
        count += 1
    temp = item

print(count)
