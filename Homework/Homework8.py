# Задача
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import os
            
def create_phonebook_file():
    with open('phonebook.txt', mode='w', encoding='utf-8') as file:
        file.write('last_name,first_name,patronymic,phone_number\n')
            
def read_text_file():
        with open('phonebook.txt', mode='r', encoding='utf-8') as file:
            phonebook = []
            return phonebook

def write_text_file():
        with open('phonebook.txt', mode='w', encoding='utf-8') as file:
            phonebook = []
            return phonebook

def add_contact(phonebook):
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        phonebook_headers = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
        new_contact = {}
        for field in phonebook_headers:
            new_contact[field] = input(f"Введите {field.lower()}: ")
        phonebook.append(new_contact)
        print("Контакт успешно добавлен.")
            
def search_contact(phonebook):
    phonebook_headers = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    search_field = input("Введите данные для поиска: ")
    found_contacts = []
    for contact in phonebook:
        for field in phonebook_headers:
            if search_field.lower() in contact[field].lower():
                found_contacts.append(contact)
                break 
    if found_contacts:
        print("Результаты поиска:")
        for contact in found_contacts:
            print(", ".join(contact[field] for field in phonebook_headers))
    else:
        print("Контакты не найдены.")

def display_contacts(phonebook):
    print('Телефонная книга:')
    for contact in phonebook:
        print(contact)

def edit_contact(phonebook):
    phonebook_headers = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    search_field = input("Введите данные для поиска контакта, который нужно изменить: ")
    found_contacts = []
    for i, contact in enumerate(phonebook):
        for field in phonebook_headers:
            if search_field.lower() in contact[field].lower():
                found_contacts.append((i, contact))
                break  
    if found_contacts:
        print("Найдены следующие контакты:")
        for i, contact in found_contacts:
            print(f"{i}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Номер телефона']}")
        contact_index = int(input("Введите номер контакта для редактирования: "))
        contact = phonebook[found_contacts[contact_index][0]]
        for field in phonebook_headers:
            new_value = input(f"Введите новое значение для поля {field.lower()} [{contact[field]}]: ")
            if new_value:
                contact[field] = new_value
        print("Контакт успешно изменен.")
    else:
        print("Контакты не найдены.")

def delete_contact(phonebook):
    phonebook_headers = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    search_field = input("Введите данные для поиска контакта, который нужно удалить: ")
    found_contacts = []
    for i, contact in enumerate(phonebook):
        for field in phonebook_headers:
            if search_field.lower() in contact[field].lower():
                found_contacts.append((i, contact))
                break  
    if found_contacts:
        print("Найдены следующие контакты:")
        for i, contact in found_contacts:
            print(f"{i}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Номер телефона']}")
        contact_index = int(input("Выберите номер контакта, который хотите удалить: "))
        if contact_index >= 0 and contact_index < len(found_contacts):
            contact = phonebook[found_contacts[contact_index][0]]
            phonebook.remove(contact)
            print('Контакт успешно удален')
        else:
            print('Неверный выбор')
    else:
        print('Контакты не найдены.')
        
def user_action():
    if os.path.isfile('phonebook.txt'):
        phonebook = read_text_file()
    else:
        create_phonebook_file()
        phonebook = []    
    while True:
        print('Выберите действие:')
        print('1. Добавить контакт')
        print('2. Поиск контакта')
        print('3. Отобразить все контакты')
        print('4. Редактировать контакт')
        print('5. Удалить контакт')
        print('0. Выход')
        choice = input('Введите номер действия: ')
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            display_contacts(phonebook)
        elif choice == '4':
            edit_contact(phonebook)
        elif choice == '5':
            delete_contact(phonebook)
        elif choice == '0':
            print('До свидания!')
            break
        else:
            print('Неверный выбор')

user_action()