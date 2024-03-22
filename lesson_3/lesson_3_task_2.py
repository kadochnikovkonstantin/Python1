from smartphone import Smartphone
catalog = []

for _ in range(1):
    brand = input("Введите марку смартфона: ")
    model = input("Введите модель смартфона: ")
    number = input("Введите номер телефона: ")

    phone = Smartphone(model, number, brand)
    catalog.append(phone)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}.")