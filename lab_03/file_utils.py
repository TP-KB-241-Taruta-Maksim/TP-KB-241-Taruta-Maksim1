import csv
from student import Student

class FileUtils:

    @staticmethod
    def load_students(filename):
        students = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 4:
                        students.append(Student(row[0], row[1], row[2], row[3]))
        except FileNotFoundError:
            pass
        return students

    @staticmethod
    def save_students(filename, students):
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            for s in students:
                writer.writerow([s.name, s.phone, s.email, s.address])
