# Запрос первого числа
num1 = float(input("Введите первое число: "))

# Запрос операции
operation = input("Введите операцию (+, -, *, /): ")

# Запрос второго числа
num2 = float(input("Введите второе число: "))

# Выполнение операции
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0: # Проверка деления на ноль
        result = num1 / num2
    else:
        result = "Ошибка: Деление на ноль!"
else:
    result = "Неверная операция."

# Вывод результата
print("Результат:", result)