# Початковий список студентів
students = [
    {"name": "Ivan", "grade": 78},
    {"name": "Olena", "grade": 92},
    {"name": "Maks", "grade": 67},
    {"name": "Sofiia", "grade": 85}
]

print("=== Сортування списку словників ===")
print("1 - Сортувати за ім'ям")
print("2 - Сортувати за оцінкою (від меншої до більшої)")
print("3 - Сортувати за оцінкою (від більшої до меншої)")

choice = input("Ваш вибір (1/2/3): ")

if choice == "1":
    result = sorted(students, key=lambda x: x["name"])
elif choice == "2":
    result = sorted(students, key=lambda x: x["grade"])
elif choice == "3":
    result = sorted(students, key=lambda x: x["grade"], reverse=True)
else:
    print("Невірний вибір!")
    result = students

print("\n=== Результат сортування ===")
for item in result:
    print(f"{item['name']} — {item['grade']}")
