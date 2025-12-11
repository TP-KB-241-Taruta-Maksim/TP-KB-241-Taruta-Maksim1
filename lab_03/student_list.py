from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, name: str):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                return True
        return False

    def update_student(self, name: str, phone=None, email=None, address=None):
        for s in self.students:
            if s.name == name:
                if phone: s.phone = phone
                if email: s.email = email
                if address: s.address = address
                return True
        return False

    def get_all(self):
        return self.students
