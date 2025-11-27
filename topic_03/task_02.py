print("=== Тестування функцій списків у Python ===")

# Початковий список
my_list = [3, 1, 4]
print("Початковий список:", my_list)

# 1. append() – додає елемент в кінець
my_list.append(5)
print("Після append(5):", my_list)

# 2. extend() – додає кілька елементів
my_list.extend([9, 2])
print("Після extend([9, 2]):", my_list)

# 3. insert(index, value) – вставка на позицію
my_list.insert(1, 100)
print("Після insert(1, 100):", my_list)

# 4. remove(value) – видалення за значенням (тільки перше співпадіння)
my_list.remove(4)
print("Після remove(4):", my_list)

# 5. copy() – створення копії списку
copy_list = my_list.copy()
print("Копія списку:", copy_list)

# 6. sort() – сортування списку
my_list.sort()
print("Після sort():", my_list)

# 7. reverse() – перевертання списку
my_list.reverse()
print("Після reverse():", my_list)

# 8. clear() – очищення списку
my_list.clear()
print("Після clear():", my_list)

print("=== Кінець тестування ===")
