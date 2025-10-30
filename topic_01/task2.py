text = "   прИвіт, я маКс!   "

print("Оригінальний рядок:", repr(text))

#Прибирає зайві пробіли
print("strip():", repr(text.strip()))

# Первая біг буква
print("capitalize():", text.strip().capitalize())

# БІг Букви Кожного Слова
print("title():", text.strip().title())

# БІГ БУКВИ
print("upper():", text.strip().upper())

# міні букви
print("lower():", text.strip().lower())
