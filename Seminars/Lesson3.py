def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)
n = int(input()) # 5
sumNumbers(n) # 15


def sum_str(*args):
    res = ""
    for i in args:
        res += i
    return res
print(sum_str('a', 's', 'd', 'w')) # asdw

from modul import max1
print(max1(5,10))

from modul import *# все функции
print(max1(5,10))

import modul as m1
print(m1.max1(5,11))


В Python можно перемножать строку на число.
def new_string(symbol, count):
    return symbol * count
print(new_string('!', 5)) # !!!!!

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [38, 27, 43, 3, 9, 82, 10]
merge_sort(list1)
print(list1)