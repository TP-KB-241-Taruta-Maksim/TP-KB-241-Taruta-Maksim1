from student_list import StudentList
from file_utils import FileUtils
from student import Student

FILENAME = "students.csv"

def main():

    student_list = StudentList()

    # загрузка из файла
    for st in FileUtils.load_students(FILENAME):
        student_list.add_student(st)

    while True:
        print("\n--- Телефонний довідник студентів ---")
        print("1. Показати всіх")
        print("2. Додати студента")
        print("3. Видалити студента")
        print("4. Оновити студента")
        print("5. Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            for s in student_list.get_all():
                print(s)

        elif choice == "2":
            name = input("Ім’я: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            address = input("Адреса: ")
            student_list.add_student(Student(name, phone, email, address))

        elif choice == "3":
            name = input("Кого видалити (ім’я): ")
            if not student_list.remove_student(name):
                print("Студента не знайдено")

        elif choice == "4":
            name = input("Кого оновити (ім’я): ")
            phone = input("Новий телефон (Enter — пропустити): ") or None
            email = input("Новий email (Enter — пропустити): ") or None
            address = input("Нова адреса (Enter — пропустити): ") or None

            if not student_list.update_student(name, phone, email, address):
                print("Студента не знайдено")

        elif choice == "5":
            FileUtils.save_students(FILENAME, student_list.get_all())
            print("Збережено. Вихід...")
            break

        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()
