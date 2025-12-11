# Відсортований список студентів (4 поля)
students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "address": "Kyiv"},
    {"name": "Emma", "phone": "0931112233", "email": "emma@gmail.com", "address": "Lviv"},
    {"name": "Jon",  "phone": "0735556677", "email": "jon@gmail.com",  "address": "Odesa"},
    {"name": "Zak",  "phone": "0990001122", "email": "zak@gmail.com",  "address": "Dnipro"}
]


def printAll():
    print("\n--- Список студентів ---")
    for s in students:
        print(f"Ім'я: {s['name']} | Телефон: {s['phone']} | Email: {s['email']} | Адреса: {s['address']}")
    print("------------------------\n")


def addStudent():
    print("\n--- Додавання нового студента ---")
    name = input("Введіть ім'я: ")
    phone = input("Введіть номер телефону: ")
    email = input("Введіть email: ")
    address = input("Введіть адресу: ")

    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    # визначення позиції вставки (сортування)
    pos = 0
    for s in students:
        if name > s["name"]:
            pos += 1
        else:
            break

    students.insert(pos, newItem)
    print("Студента додано!\n")


def deleteStudent():
    print("\n--- Видалення студента ---")
    name = input("Введіть ім'я студента, якого потрібно видалити: ")

    index = -1
    for s in students:
        if s["name"] == name:
            index = students.index(s)
            break

    if index == -1:
        print("Студента не знайдено!\n")
    else:
        del students[index]
        print("Студента видалено!\n")


def updateStudent():
    print("\n--- Оновлення інформації про студента ---")
    name = input("Введіть ім'я студента, дані якого потрібно оновити: ")

    found = None
    for s in students:
        if s["name"] == name:
            found = s
            break

    if found is None:
        print("Студента не знайдено!\n")
        return

    print("\nВведіть нові дані (Enter — залишити без змін):")

    new_name = input(f"Нове ім'я [{found['name']}]: ") or found['name']
    new_phone = input(f"Новий телефон [{found['phone']}]: ") or found['phone']
    new_email = input(f"Новий email [{found['email']}]: ") or found['email']
    new_address = input(f"Нова адреса [{found['address']}]: ") or found['address']

    # Видаляємо старий запис
    students.remove(found)

    # Створюємо оновлений запис
    updated = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "address": new_address
    }

    # Вставляємо в правильну позицію (щоб список залишався відсортованим)
    pos = 0
    for s in students:
        if new_name > s["name"]:
            pos += 1
        else:
            break

    students.insert(pos, updated)

    print("Дані оновлено!\n")


def main():
    while True:
        print("Оберіть дію:")
        print("  D - Додати студента")
        print("  U - Оновити дані студента")
        print("  R - Видалити студента")
        print("  P - Показати всіх студентів")
        print("  X - Вийти з програми")

        choice = input("Ваш вибір: ")

        match choice.lower():
            case "d":
                addStudent()
                printAll()
            case "u":
                updateStudent()
                printAll()
            case "r":
                deleteStudent()
                printAll()
            case "p":
                printAll()
            case "x":
                print("Вихід")
                break
            case _:
                print("Невірна команда!\n")


main()
