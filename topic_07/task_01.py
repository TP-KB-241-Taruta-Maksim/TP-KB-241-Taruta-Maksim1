class Person:
    def __init__(self, name, age):
        # Викликається при створенні об'єкта
        self.name = name
        self.age = age

    def __str__(self):
        # Рядок для користувача (print)
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        # Рядок для розробника
        return f"Person('{self.name}', {self.age})"

    def __len__(self):
        # Повертає довжину імені
        return len(self.name)

    def __eq__(self, other):
        # Порівняння двох людей
        return self.name == other.name and self.age == other.age

    def __add__(self, other):
        # Сумує вік двох людей
        return Person(self.name + "&" + other.name, self.age + other.age)


# === ТЕСТУВАННЯ ===

p1 = Person("Max", 18)
p2 = Person("Max", 18)
p3 = Person("Anna", 20)

print("Вивід через __str__:", p1)
print("Вивід через __repr__:", repr(p1))
print("Довжина імені (__len__):", len(p1))
print("Порівняння (__eq__):", p1 == p2)
print("Порівняння різних:", p1 == p3)

# __add__
p4 = p1 + p3
print("Результат додавання (__add__):", p4)
