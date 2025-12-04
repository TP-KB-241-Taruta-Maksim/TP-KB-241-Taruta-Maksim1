import locale

locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} років)"


# Створюємо список студентів
students = [
    Student("Максим", 18),
    Student("Іван", 20),
    Student("Андрій", 19),
    Student("Олена", 17)
]

# Вибір способу сортування
sort_key = input("Введіть 'name' для сортування за іменем або 'age' для сортування за віком: ").strip().lower()

if sort_key == "name":
    sorted_students = sorted(students, key=lambda s: locale.strxfrm(s.name))
elif sort_key == "age":
    sorted_students = sorted(students, key=lambda s: s.age)
else:
    print("Невірний вибір, сортування за замовчуванням за іменем")
    sorted_students = sorted(students, key=lambda s: locale.strxfrm(s.name))

# Виведення результату
for student in sorted_students:
    print(student)

