from operations import Operations

class task_03:
    """Клас калькулятора для завдання task_03"""
    def __init__(self):
        self.operations = Operations()

    def calculate(self, a, b, operator):
        if operator == '+':
            return self.operations.add(a, b)
        elif operator == '-':
            return self.operations.subtract(a, b)
        elif operator == '*':
            return self.operations.multiply(a, b)
        elif operator == '/':
            return self.operations.divide(a, b)
        else:
            raise ValueError("Невідомий оператор!")

    def run(self):
        while True:
            try:
                a = float(input("Введіть перше число: "))
                b = float(input("Введіть друге число: "))
                operator = input("Оберіть операцію (+, -, *, /) або 'q' для виходу: ").strip()

                if operator.lower() == 'q':
                    print("Калькулятор завершив роботу.")
                    break

                result = self.calculate(a, b, operator)
                print(f"Результат: {result}\n")

            except ValueError as e:
                print(f"Помилка: {e}\n")
            except Exception as e:
                print(f"Сталася помилка: {e}\n")

