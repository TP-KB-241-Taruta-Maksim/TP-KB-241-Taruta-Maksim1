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

print("Калькулятор. Введіть 'exit' або 'stop' щоб завершити програму.")

while True:
    op = input("Операція (+, -, *, /): ")
    
    # Перевірка на вихід
    if op.lower() in ["exit", "stop", "вихід"]:
        print("Програма завершена.")
        break

    # Перевірка на допустимість операції
    if op not in ["+", "-", "*", "/"]:
        print("Невідома операція, спробуйте ще раз.")
        continue

    # Введення чисел
    try:
        a = float(input("Перше число: "))
        b = float(input("Друге число: "))
    except ValueError:
        print("Помилка: введіть коректне число.")
        continue

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

