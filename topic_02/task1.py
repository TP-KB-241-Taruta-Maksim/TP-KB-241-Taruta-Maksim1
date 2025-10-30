import math

# Функція для обчислення дискримінанту
def discriminant(a, b, c):
    return b**2 - 4*a*c

# Функція для знаходження коренів
def quadratic_roots(a, b, c):
    D = discriminant(a, b, c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("Два різних корені:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif D == 0:
        x = -b / (2*a)
        print("Один корінь:")
        print("x =", x)
    else:
        print("Дійсних коренів немає")

# Приклад використання
a = 1
b = 5
c = 6

quadratic_roots(a, b, c)