import logging
import functions
print("В functions є:", dir(functions))

from functions import plus, minus, multi, dilenya
from operations import operations

# ==== Налаштування логування ====
logging.basicConfig(
    filename="calculator.log",       # файл для збереження логів
    level=logging.INFO,              # рівень логування
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("=== Калькулятор з логуванням ===")

while True:
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        op = input("Введіть операцію (+ - * /): ")

        if op not in operations:
            print("Невідома операція!")
            logging.warning(f"Введена невідома операція: {op}")
            continue

        # виконання операції
        if op == '+':
            result = plus(a, b)
        elif op == '-':
            result = minus(a, b)
        elif op == '*':
            result = multi(a, b)
        elif op == '/':
            result = dilenya(a, b)

        print("Результат:", result)

        # ====== ЛОГУВАННЯ ======
        logging.info(f"Ввід: a={a}, b={b}, операція={op}, результат={result}")

    except ZeroDivisionError as e:
        print("Помилка:", e)
        logging.error(f"Помилка ділення: {e}")

    except ValueError:
        print("Помилка: введено не число!")
        logging.error("Помилка: користувач ввів не число")

    except Exception as e:
        print("Невідома помилка:", e)
        logging.critical(f"Невідома помилка: {e}")

    # можливість виходу
    stop = input("Продовжити? (y/n): ")
    if stop.lower() == 'n':
        break
