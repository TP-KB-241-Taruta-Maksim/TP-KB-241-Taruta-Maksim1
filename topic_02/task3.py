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

print("Калькулятор з match")
a = float(input("Перше число: "))
b = float(input("Друге число: "))
op = input("Операція (+, -, *, /): ")

match op:
    case "+":
        print("Результат:", plus(a, b))
    case "-":
        print("Результат:", minus(a, b))
    case "*":
        print("Результат:", multi(a, b))
    case "/":
        print("Результат:", dilenya(a, b))
    case _:
        print("Невідома операція")