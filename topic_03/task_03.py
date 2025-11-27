# ✅ Функція для знаходження позиції вставки
def find_insert_position(sorted_list, value):
    for i in range(len(sorted_list)):
        if value <= sorted_list[i]:
            return i
    return len(sorted_list)

# ✅ Функція, яка вставляє елемент у правильне місце
def insert_sorted(sorted_list, value):
    pos = find_insert_position(sorted_list, value)
    sorted_list.insert(pos, value)
    return sorted_list

# Тест роботи функції insert_sorted
print(insert_sorted([1, 2, 4, 5], 3))


print("=== Тестування функцій словників у Python ===")

# Початковий словник
my_dict = {"name": "Ivan", "age": 20, "city": "Kyiv"}
print("Початковий словник:", my_dict)

# 1. update() – оновлення або додавання ключів
my_dict.update({"age": 21, "country": "Ukraine"})
print("Після update({'age': 21, 'country': 'Ukraine'}):", my_dict)

# 2. del – видалення елемента за ключем
del my_dict["city"]
print("Після del my_dict['city']:", my_dict)

# 3. keys() – отримання всіх ключів
print("Ключі (keys()):", list(my_dict.keys()))

# 4. values() – отримання всіх значень
print("Значення (values()):", list(my_dict.values()))

# 5. items() – отримання пар (ключ, значення)
print("Пари ключ-значення (items()):", list(my_dict.items()))

# 6. clear() – очищення словника
my_dict.clear()
print("Після clear():", my_dict)

print("=== Кінець тестування ===")
