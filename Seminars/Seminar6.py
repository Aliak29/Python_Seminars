'''
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
'''
import random


def random_int_list(length, min, max):
    list = []
    for i in range(length):
        list.append(random.randint(min, max))
    return list

length_array_1 = int(input("Введите количество элементов в 1 массиве: "))
list_1 = random_int_list(length_array_1, 0, 20)
print(list_1)
length_array_2 = int(input("Введите количество элементов во 2 массиве: "))
list_2 = random_int_list(length_array_2, 0, 20)
print(list_2)
list_3 = []
for item in list_1:
    if item not in list_2:
        list_3.append(item)
print(f'Вывод: {len(list_3)}')
print(list_3)

'''
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
'''
import random
a = int(input('Введите длину списка = '))
lst = [] 
for i in range(a):
    lst.append(random.randint(1,5))              
print(lst)

count = 0
for i in range(1, a-1):
    if (lst[i] > lst[i-1]) and (lst[i] > lst[i+1]):
        count +=1
print(count) 


'''
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.

'''
import random
a = int(input('Введите длину списка = '))
lst = [] 
for i in range(a):
    lst.append(random.randint(1,5))              
print(lst)

count = 0
for i in range(a):
    num1 = lst[i]
    for j in range(i + 1, a):
        num2 = lst[j]
        if num1 == num2:
            count +=1
print(count) 

'''
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
'''

number_friend_check = int(input('Введите число для проверки:'))

def divisors_sum (input_number):
    sum = 0
    for i in range (1, input_number):
        if input_number % i == 0:
            sum += i
    return sum

def friendly_pairs (input_number):
    for i in range (2, input_number + 1):
        j = divisors_sum (i)
        if i <= (input_number) and j <= (input_number):
            print(i, j)

friendly_pairs(number_friend_check)


#2
n = int(input())
list_1 = list()

for i in range(n):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
    list_1.append(tuple([i, summa]))


for i in range(len(list_1)):
    for j in range(i, len(list_1)):
        if (i != j) and (list_1[i][0]) == (list_1[j][1]) and (list_1[i][1]) == (list_1[j][0]):
            print(*list_1[i])