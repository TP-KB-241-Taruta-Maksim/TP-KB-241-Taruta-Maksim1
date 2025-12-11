from sys import argv
from lab2 import *

def main():
    if len(argv) < 2:
        print("Помилка: потрібно вказати CSV файл.")
        return

    csv_file = argv[1]

    global students
    students = load_from_csv(csv_file)

    while True:
        print("D - Додати")
        print("U - Оновити")
        print("R - Видалити")
        print("P - Показати")
        print("X - Вихід")

        cmd = input("Ваш вибір: ").lower()

        if cmd == "d":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            address = input("Адреса: ")
            add_student(students, {"name": name, "phone": phone, "email": email, "address": address})

        elif cmd == "u":
            name = input("Кого оновити: ")
            new_name = input("Нове ім'я: ") or name
            new_phone = input("Новий телефон: ")
            new_email = input("Новий email: ")
            new_addr = input("Нова адреса: ")

            updated = {
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_addr
            }

            update_student(students, name, updated)

        elif cmd == "r":
            name = input("Кого видалити: ")
            delete_student(students, name)

        elif cmd == "p":
            print_all(students)

        elif cmd == "x":
            save_to_csv(csv_file, students)
            print("Збережено. Вихід.")
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()
