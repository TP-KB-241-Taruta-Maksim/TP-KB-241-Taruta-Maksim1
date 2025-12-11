import csv

# глобальний список студентів
students = []


def load_from_csv(filename):
    """Завантаження студентів з CSV."""
    data = []
    try:
        with open(filename, "r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("CSV файл не знайдено, створюється новий.")
    return sorted(data, key=lambda s: s["name"])


def save_to_csv(filename, data):
    """Збереження студентів у CSV."""
    with open(filename, "w", newline='', encoding="utf-8") as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for s in data:
            writer.writerow(s)


def add_student(data, new_item):
    """Додає студента у відсортовану позицію."""
    pos = 0
    for s in data:
        if new_item["name"] > s["name"]:
            pos += 1
        else:
            break
    data.insert(pos, new_item)
    return data


def delete_student(data, name):
    """Видаляє студента. Повертає True/False."""
    for s in data:
        if s["name"] == name:
            data.remove(s)
            return True
    return False


def update_student(data, name, updated):
    """Оновлює студента. Повертає True/False."""
    for s in data:
        if s["name"] == name:
            data.remove(s)
            add_student(data, updated)
            return True
    return False


def print_all(data):
    """Вивід списку студентів."""
    print("\n--- Список студентів ---")
    for s in data:
        print(f"{s['name']} | {s['phone']} | {s['email']} | {s['address']}")
    print("------------------------\n")
