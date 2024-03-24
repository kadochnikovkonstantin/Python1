from address import Address
from mailing import Mailing

to_address = Address('123456', 'Moscow', 'Lenina', 12, 3)
from_address = Address('234567', 'St.Petersburg', 'Pushkin', 5, 2)
my_mailing = Mailing(to_address, from_address, 100, 'ABC123ABC')

print(f'Отправление {my_mailing.track} из {my_mailing.from_address.index} {my_mailing.from_address.city} {my_mailing.from_address.street} {my_mailing.from_address.house} {my_mailing.from_address.apartment} в {my_mailing.to_address.index} {my_mailing.to_address.city} {my_mailing.to_address.street} {my_mailing.to_address.house} {my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} рублей.')