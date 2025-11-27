def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def dilenya(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль"

# НОВА ФУНКЦІЯ ЗАПИТУ ДАНИХ
def get_numbers():
    """Запитує два числа у користувача та обробляє помилки."""
    while True:
        try:
            a = float(input("Перше число: "))
            b = float(input("Друге число: "))
            return a, b
        except ValueError:
            print("Помилка: введіть коректні числа!\nСпробуйте ще раз.\n")


print("Калькулятор. Введіть 'exit' або 'stop' щоб завершити програму.")

while True:
    op = input("Операція (+, -, *, /): ")

    if op.lower() in ["exit", "stop", "вихід"]:
        print("Програма завершена.")
        break

    if op not in ["+", "-", "*", "/"]:
        print("Невідома операція, спробуйте ще раз.")
        continue

    # --- ОТРИМАННЯ ЧИСЕЛ ЧЕРЕЗ ФУНКЦІЮ ---
    a, b = get_numbers()

    match op:
        case "+":
            print("Результат:", plus(a, b))
        case "-":
            print("Результат:", minus(a, b))
        case "*":
            print("Результат:", multi(a, b))
        case "/":
            print("Результат:", dilenya(a, b))
