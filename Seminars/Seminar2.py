По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120 

Способ 1
result = 1
n = int(input('Введите число = '))
for i in range(1, n + 1):
    result *= i
print(result)

Способ 2
n = int(input('Введите число = '))
result = 1
while n > 1:
    result = result * n
    n = n-1
print(result)


Способ 3
n = int(input('Введите число = '))
result = 1
while n > 1:
    result *= n
    n -= 1
    if n == 10:
        break
else:
    print('END!')
print(result)

Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6

a = int(input('Введите число Фибоначчи: '))
number = a
if (a == 0):
    print(0)
else:
    fibPrev, fibNext = 0, 1
    n = 1
    while(fibNext <= a):
        if(fibNext == a):
        print(f'{number} является {n}-м по счету числом Фибоначчи.')
        break
        fibPrev, fibNext = fibNext, fibPrev + fibNext
        n += 1
    else:
        print(f'{number} не является числом Фибоначчи, введите другое число.')

Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50

Один цикл for 
n = int(input('Введите общее количество рассматриваемых дней = '))      
count = 0
period = 0
for i in range(n):
    user_temp = int(input('Средняя температура за день = '))
    if user_temp > 0:
        count += 1
        if count > period:
            period = count
    else:
        count = 0
print(f'Дней оттепели было: {period} шт.')


n = int(input('Введите общее количество рассматриваемых дней = '))
temp = [] # список
# range(5) -> 0, 1, 2, 3, 4
# range(5, 11) ->  5, 6, 7, 8, 9, 10
# range (1, 11, 2) -> 1, 3, 5, 7, 9
for i in range(n):
    user_temp = int(input('Средняя температура за день = '))
    temp.append(user_temp) #adds an item to the end of a list               
print(temp)

count = 0
period = 0
for i in range(n):
    if temp[i] > 0:
        count += 1
        if count > period:
            period = count
    else:
        count = 0
print(f'Дней оттепели было: {period} шт.')

2 Способ
import random
n = int(input('Введите общее количество рассматриваемых дней = '))
temp = [] 
for i in range(n):
    temp.append(random.randint(-10,10))              
print(temp)
count = 0
period = 0
for i in range(n):
    if temp[i] > 0:
        count += 1
        if count > period:
            period = count
    else:
        count = 0
print(f'Дней оттепели было: {period} шт.')

Срезы
a = [14, 3, 75, 56, 86]
print(a[:])
print(a[2:])
print(a[:3])
print(a[1:4:2])