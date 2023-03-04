# def print_operation_table(operation, num_rows=6, num_columns=7):
#     matrix = [[operation(j, i) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for row in matrix:
#         print(*row, '\n')

# print_operation_table(lambda x, y: x*y)

# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# 5. Добавить контакт

contacts_file = r'C:\Users\Aliya\Downloads\Python course\Seminars\contacts_file.txt'
def append_contact(contacts_file):
    contact = input('Введите контакт в формате Ф И О Телефон:')
    with open(contacts_file, 'a', encoding="utf-8") as f:
        f.write(f'\n{contact}')
        print ('Контакт добавлен')

def read_file(contacts_file):
    with open(contacts_file, 'r', encoding="utf-8") as f:
        print (f.read())

def search_contact(contacts_file):
    search_by = input("Введите информацию для поиска (фамилия, имя или отчество):")
    with open(contacts_file, 'r', encoding="utf-8") as f:
        for line in f:
            if search_by in line:
                print(line)

def user_action():
    print ('Добро пожаловать! \n1) Вывести весь справочник \n2) Добавить контакт \n3) Найти контакт')
    while (input1:= int(input('Выберите действие со справочником (0 = выход):'))) != 0:
        if input1 == 1:
            read_file(contacts_file)
        elif input1 == 2:
            append_contact(contacts_file)
        elif input1 == 3:
            search_contact(contacts_file)
        else:
            print("Некорректный ввод")

user_action()

# def output(dataPath):
#     with open(dataPath, 'r') as f:
#         for line in f:
#             print(line)

# def add(dataPath):
#     with open(dataPath, 'a') as f:
#         b = '\n'
#         a = 'Feya Wilson FTGH +375234545657\n'
#     f.write(a)

# def search(dataPath):
#     with open(dataPath, 'r') as f:
#         N = input('Введите Имя или Фамилию: ')
#         for line in f:
#             if N in line:
#                 print(line)

# dataPath = r'C:\Users\Aliya\Downloads\Python course\contacts_file.txt'
# output(dataPath)
# add(dataPath)
# search(dataPath)