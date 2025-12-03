import requests

# URL API НБУ
NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

def get_exchange_rates():
    """
    Отримання актуальних курсів валют з API НБУ.
    Повертає словник валют -> курс у гривнях.
    """
    response = requests.get(NBU_API_URL)
    data = response.json()

    rates = {}

    for item in data:
        if item["cc"] in ["USD", "EUR", "PLN"]:
            rates[item["cc"]] = item["rate"]

    return rates


def convert_currency(amount, currency, rates):
    """
    Конвертація валюти у гривню.
    """
    if currency not in rates:
        return None
    return amount * rates[currency]


def main():
    print("=== Конвертер валют НБУ ===")
    print("Доступні валюти: USD, EUR, PLN")

    # Отримуємо курси
    rates = get_exchange_rates()

    # Введення користувача
    currency = input("Введіть валюту (USD/EUR/PLN): ").upper()
    amount = float(input("Введіть суму: "))

    result = convert_currency(amount, currency, rates)

    if result is None:
        print("Помилка: така валюта не підтримується!")
    else:
        print(f"{amount} {currency} = {result:.2f} UAH за курсом НБУ")



if __name__ == "__main__":
    main()
