from Address import Address
from Mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Невский", "20", "25")

mailing = Mailing(to_address, from_address, 500, "TRACK123456")

print(f"Отправление {mailing.track} из {mailing.from_adress.index}, {mailing.from_adress.city}, {mailing.from_adress.street}, {mailing.from_adress.home} - {mailing.from_adress.apartment} в {mailing.to_adress.index}, {mailing.to_adress.city}, {mailing.to_adress.street}, {mailing.to_adress.home} - {mailing.to_adress.apartment}. Стоимость {mailing.cost} рублей.")