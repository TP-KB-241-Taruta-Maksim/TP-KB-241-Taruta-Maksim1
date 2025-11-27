def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

# Функція ділення з обробкою винятку
def dilenya(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка: ділення на нуль!"

# Функція для запиту чисел
def get_numbers():
    """Запитує два числа та обробляє винятки введення."""
    while True:
        try:
            a = float(input("Перше число: "))
            b = float(input("Друге число: "))
            return a, b
        except ValueError:
            print("Помилка: введіть коректні числа!\n")


print("Калькулятор. Введіть 'exit' або 'stop' для завершення.")

while True:
    op = input("Операція (+, -, *, /): ")

    # Вихід із програми
    if op.lower() in ["exit", "stop", "вихід"]:
        print("Програма завершена.")
        break

    # Перевірка на коректну операцію
    if op not in ["+", "-", "*", "/"]:
        print("Невідома операція, спробуйте ще раз.")
        continue

    # Отримання чисел
    a, b = get_numbers()

    # Виконання операції
    match op:
        case "+":
            print("Результат:", plus(a, b))
        case "-":
            print("Результат:", minus(a, b))
        case "*":
            print("Результат:", multi(a, b))
        case "/":
            print("Результат:", dilenya(a, b))
