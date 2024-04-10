# Перше завдання

def total_salary(path):
    try:
        total_salary = 0
        num_developers = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                developer, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1
        if num_developers != 0:
            average_salary = total_salary / num_developers
        else:
            average_salary = 0
        return total_salary, average_salary
    except FileNotFoundError:
        print("Файл не знайдено!")
        return None, None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None, None


total, average = total_salary('goit-algo-hw/goit-algo-hw-04/total_salary.txt')
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {
          total} \nСередня заробітна плата: {average}")


# Друге завдання

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {'id': cat_id, 'name': name, 'age': age}
                cats_info.append(cat_info)
    except FileNotFoundError:
        print('Файл не знайдено!')
    except Exception as e:
        print(f'Виникла помилка!: {e}')
    return cats_info


path_to_cats_file = 'goit-algo-hw/goit-algo-hw-04/cats.txt'

cats_info = get_cats_info(path_to_cats_file)
print(cats_info)


# Третє завдання (не обов'язкове)

import sys
from pathlib import Path
from colorama import Fore, Style

def list_files(directory):
    for path in directory.iterdir():
        if path.is_file():
            print(Fore.BLUE + f"File: {path.name}")
        elif path.is_dir():
            print(Fore.GREEN + f"Directory: {path.name}")
            list_files(path)

def main():
    if len(sys.argv) != 2:
        print("Usage: python.py <directory_path>")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.is_dir():
        print("Error: Given path is not a directory.")
        return

    list_files(directory_path)

if __name__ == "__main__":
    main()


# Четверте завдання


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."


def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            name, phone = args
            print(add_contact(contacts, name, phone))
        elif command == "change" and len(args) == 2:
            name, new_phone = args
            print(change_contact(contacts, name, new_phone))
        elif command == "phone" and len(args) == 1:
            name = args[0]
            print(show_phone(contacts, name))
        elif command == "all" and not args:
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
