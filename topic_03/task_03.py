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
print("Ключі (keys()):", my_dict.keys())

# 4. values() – отримання всіх значень
print("Значення (values()):", my_dict.values())

# 5. items() – отримання пар (ключ, значення)
print("Пари ключ-значення (items()):", my_dict.items())

# 6. clear() – очищення словника
my_dict.clear()
print("Після clear():", my_dict)

print("=== Кінець тестування ===")
