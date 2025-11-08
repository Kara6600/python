from smartphone import Smartphone

# создаем список смартфонов
catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79991234567"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79881234567"),
    Smartphone("Huawei", "P30 Pro", "+79771234567"),
    Smartphone("Google", "Pixel 6", "+79661234567")
]

# цикл по списку и вывод информации
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")