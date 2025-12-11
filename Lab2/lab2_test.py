from lab2 import add_student, delete_student, update_student


def test_add_student():
    data = []
    add_student(data, {"name": "Bob", "phone": "", "email": "", "address": ""})
    add_student(data, {"name": "Anna", "phone": "", "email": "", "address": ""})
    assert data[0]["name"] == "Anna"
    assert data[1]["name"] == "Bob"


def test_delete_student():
    data = [{"name": "Bob"}]
    assert delete_student(data, "Bob") is True
    assert delete_student(data, "Emma") is False


def test_update_student():
    data = [{"name": "Bob", "phone": "1", "email": "a", "address": "x"}]
    updated = {"name": "Bob", "phone": "999", "email": "a", "address": "x"}
    assert update_student(data, "Bob", updated) is True
    assert data[0]["phone"] == "999"
