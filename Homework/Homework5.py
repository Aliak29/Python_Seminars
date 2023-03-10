# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power(a, b):
    if b == 1:
        return a
    if b > 1:
        return (a * power(a, b - 1))

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
print(power(a, b))

# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum_recursion(a, b):
    if a == 0:
        return b;
    return sum_recursion(a-1, b+1)

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
print(sum_recursion(a, b))