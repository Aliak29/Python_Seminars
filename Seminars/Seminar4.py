# 1. Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# 'Hello, World!'
# H: 3,
# e: 1,
# l: 3

l = set(str)
print(l)
for item in l:
    count = str.count(item)
    print(item, count)

str= input("Введите слово: ")
unique = dict(zip(list(str),[list(str).count(i) for i in list(str)]))
print("Dictionary : ",unique)


# 2. Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = input('Введите текст: ').split()
print(len(set(text)))

# 3. Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)

n = 1
b = []
while n!= 0:
    n = int(input('n: '))
    b.append(n)
print(f'Максимальное число:{max(b)}')


x = int(input("Введите число: "))
maxx = x
while x != 0:
    if x > maxx:
        maxx = x
    x = int(input("Введите число: "))
print(f'Максимальное из введённых число: {maxx}')

int(input("Введите число: "))
max_x = 0
while (x:=int(input("Введите число: "))) != 0:
    if x > max_x:
    max_x = x
print(f'Максимальное из введённых число: {max_x}')


#Переворачивает список по возрастанию
a = [1, 0, 10, 11, 4]
k = 1
while k:
    k = 0
    for i in range(len(a)-1):
        if a[i] > a[i + 1]:
            b = a[i]
            a[i] = a[i + 1]
            a[i + 1] = b
            k = i
            lim = k - 1
print(a)