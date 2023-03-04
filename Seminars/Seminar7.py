У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.

transformation = lambda x: x
values = [2, 3, 5, 7, 'asfsd'] 
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')

values = [1, 23, 42, 54]
transformed_values = list(map(lambda x: x, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')

test1 = tuple(filter(lambda x: (x>3) and (x<40), values))
print(test1)

test_2 = []
for item in values:
    if ((item > 3) and (item < 40)):
        test_2.append(item)
print(test_2)        
test_2=[item for item in values if ((item>3) and (item<40))]
print(test_2)



Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
orbits_elliptic = [item for item in orbits if item [0] != item [1]]
max_elliptic_length = max(list(map(lambda x: math.pi*x[0]*x[1], orbits_elliptic)))
longest_orbit = [item for item in orbits_elliptic if math.pi*item[0]*item[1] == max_elliptic_length]

print('{:.4f}'.format(max_elliptic_length))
print(*longest_orbit)

def find_farthest_orbit(orbits):
    return max(orbits, key=lambda x:(x[0] != x[1])*x[0]*x[1])

orbits = [(1, 3), (2.5, 10), (7, 2), (6,6)]
print(find_farthest_orbit(orbits))
print(orbits.index(find_farthest_orbit(orbits)))

def find_farthest_orbit(orbits):
    #return max(orbits, key=lambda x:(x[0] != x[1])*x[0]*x[1])
    s_orbits = list(map(lambda x: x[0]*x[1] if x[0] != x[1] else 0, orbits))
    max_s_i = s_orbits.index(max(s_orbits))
    return orbits[max_s_i]
orbits = [(1, 3), (2.5, 10), (7, 2), (6,6), (40, 40)]
print(*find_farthest_orbit(orbits))


def find_farthest_orbit(orbits):
    dict_s = {x[0]*x[1]: x for x in orbits if x[0] != x[1]}
    return dict_s[max(dict_s)]
orbits = [(1, 3), (2.5, 10), (7, 2), (6,6), (40, 40)]
print(*find_farthest_orbit(orbits)) 



Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

def same_by(characteristic, objects):
    if not objects:
        return True
    return len(set(map(characteristic, objects))) == 1

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


list_1 = [1, 2]
list_2 = [3, 4, 1]
print([(x,y) for x in list_1 for y in list_2 if x != y])