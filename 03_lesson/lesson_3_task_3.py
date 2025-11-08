from address import Address
from mailing import Mailing

# создаем адрес отправителя
from_addr = Address(
    index="123456",
    city="Москва",
    street="Тверская",
    house="10",
    apartment="15"
)

# создаем адрес получателя
to_addr = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский",
    house="20",
    apartment="25"
)

# создаем объект Mailing
mail = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="AB123456789RU"
)

# выводим информацию
print(
    f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)