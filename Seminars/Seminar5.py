# n = int(input('Введите длину списка: '))
# a = [int(x) for x in input( 'Введите числа через пробел: ' ).split()]
# max_a = (max([a[i] for i in range(n)]))
# min_a = (min([a[i] for i in range(n)]))
# for i in range(len(a)):
#     if a[i] == max_a:
#         a[i] = min_a
# print(a)

# def change_mark(old_mark):
#     maximum = max(old_mark)
#     minimum = min(old_mark)
#     new_mark =[]
#     for item in old_mark:
        if item == maximum:
            item = minimum
        new_mark.append(item)
    return new_mark

n = int(input('Введите длину списка: '))
a = [int(x) for x in input( 'Введите числа через пробел: ' ).split()]
print(change_mark(a))

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n - 1) + fib(n - 2)
    
n = int(input('Введите число = ')) 
print(fib(n))


def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
    
n = int(input('Введите число = ')) 
print(fib(n))


def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        return True
n = int(input('Введите число = '))
print(is_prime(n))



n = int(input('Введите длину списка: '))
a = [int(x) for x in input( 'Введите числа через пробел: ' ).split()]
print(a[::-1])
срезы

def reverse_num(n: int):
    if n == 0:
        return ''
    num = input('->')
    return reverse_num(n-1) + '' + num

print(reverse_num(4))