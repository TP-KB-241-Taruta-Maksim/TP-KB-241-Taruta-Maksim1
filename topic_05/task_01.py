import random

options = ["stone", "scissor", "paper"]

user = input("Введіть stone, scissor або paper: ").lower()

# Перевірка на коректність введення
if user not in options:
    print("Помилка: неправильний вибір!")
else:
    comp = random.choice(options)
    print("Комп'ютер обрав:", comp)

    if user == comp:
        print("Нічия!")
    elif (user == "stone" and comp == "scissor") or \
         (user == "scissor" and comp == "paper") or \
         (user == "paper" and comp == "stone"):
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")
