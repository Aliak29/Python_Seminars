# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка через функцию

list_1 = [7, 9, 11, 13, 15, 17]
print(list_1) 
print(*list_1) #без квадратных скобок
print(list_1[0])#по индексу
print(list_1[-1])

for i in list_1:
    print(i)
    
print(len(list_1)) #длина списка

list_1.append(8)#добавление элемента в конец списка
print(list_1)

#заполнение пустого списка поочередно от 0 до 4
list_1 = []
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)
    

list_1 = list() # создание пустого списка
for i in range(5): # цикл выполнится 5 раз
    n = int(input()) # пользователь вводит целое число
    list_1.append(n) # сохранение элемента в конец списка
    print(list_1) # [12, 7, -1, 21, 0]

list_1 = [12, 7, -1, 21, 0]
for i in range(len(list_1)):
    print(list_1[i]) # вывод каждого элемента списка
    
    
Основные действия со списками:
1. Удаление последнего элемента списка.
Метод pop удаляет последний элемент из списка:
list_1 = [12, 7, -1, 21, 0]
# a = list_1.pop()
# print(a)
print(list_1.pop()) # 0
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1) # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1) # [12, 7]

2. Удаление конкретного элемента из списка.
Надо указать значение индекса в качестве аргумента функции pop:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1) # [7, -1, 21, 0] 


3. Добавление элемента на нужную позицию.
 Функция insert — указание индекса (позиции) и значения.
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1) # [12, 7, 11, -1, 21, 0] 

Срез списка
● Отрицательное число в индексе — счёт с конца списка
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]


Кортежи
Кортеж — это неизменяемый список.
Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты каких-либо
данных от изменений (намеренных или случайных). Кортеж занимает меньше места в
памяти и работают быстрее, по сравнению со списками
t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,) # в конце обязательно запятая
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))

v = [1, 2, 3]
print(v)
print(type(v))
v = tuple(v)
print(v)
print(type(v))

# a, b = 1, 2 # множественное присваивание
# a = b = 1
a, b, c = v
print(a, b, c)



t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))# r:red g:green b:blue

t = (1, 2, 3, 4, 5,)
print(t[1])
for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])
    

Словари
Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
В списках в качестве ключа используется индекс элемента. В словаре для определения
элемента используется значение ключа (строка, число).

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
dictionary[895] = 6516516
print(dictionary)

for item in dictionary:
    # print(item)
    print('{}: {}'.format(item, dictionary[item]))   
key and value 
for (k,v) in dictionary.items():
    print(k,v)
print(dictionary.items())

d = {}
d = dict()

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d)
print(d['q'])


Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
Одно множество может содержать значения любых типов. Если у Вас есть два множества,
Вы можете совершать над ними любые стандартные операции, например, объединение,
пересечение и разность. Давайте разберем их.
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors)
colors.clear() # clear
print(colors) #set() пустое множество q = set()


Операции со множествами в Python:
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13} все действия по порядку
print(q)

Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут
работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})


List comprehensions are a handy option for creating lists based on existing lists.
When using them you can build by using strings and tuples as well. 

list_variable = [x for x in iterable]
number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)


Задача 1
Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
Решение:
1. Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
    
Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
print(list_1)

Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
print(list_1)
Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i*i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
print(list_1)
Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]