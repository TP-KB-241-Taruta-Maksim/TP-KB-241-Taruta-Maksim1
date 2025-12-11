import pytest
from student import Student
from student_list import StudentList

def test_add_student():
    lst = StudentList()
    st = Student("Bob", "123", "b@b.com", "Kyiv")
    lst.add_student(st)
    assert len(lst.get_all()) == 1

def test_remove_student():
    lst = StudentList()
    lst.add_student(Student("Bob", "1", "a", "b"))
    assert lst.remove_student("Bob") is True
    assert lst.remove_student("Bob") is False

def test_update_student():
    lst = StudentList()
    lst.add_student(Student("Bob", "1", "a", "b"))
    lst.update_student("Bob", phone="999")
    assert lst.get_all()[0].phone == "999"
