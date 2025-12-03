from operations import execute_operation

print("=== Калькулятор ===")
print("1 — Додавання")
print("2 — Віднімання")
print("3 — Множення")
print("4 — Ділення")

choice = input("Виберіть операцію: ")
result = execute_operation(choice)
print("Результат:", result)

