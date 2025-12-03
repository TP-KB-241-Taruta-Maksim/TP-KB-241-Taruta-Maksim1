from functions import plus, minus, multi, divide

def get_numbers():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    return a, b

def execute_operation(choice):
    if choice == "1":
        a, b = get_numbers()
        return plus(a, b)
    elif choice == "2":
        a, b = get_numbers()
        return minus(a, b)
    elif choice == "3":
        a, b = get_numbers()
        return multi(a, b)
    elif choice == "4":
        a, b = get_numbers()
        return divide(a, b)
    else:
        return "Невірний вибір!"



