from address import Address
from mailing import Mailing

to_address = Address(655150, "Abakan", "Lenina", 15, 105)
from_address = Address(655180, "Tomsk", "Frunze", 18, 2)

send = Mailing(to_address, from_address, 500.0, 123456)

print(
    f"Отправление {send.track} из {send.from_address.index}, {send.from_address.city}, "
    f"{send.from_address.street}, {send.from_address.house_number} - {send.from_address.apartment_number} "
    f"в {send.to_address.index}, {send.to_address.city}, {send.to_address.street}, {send.to_address.house_number} - "
    f"{send.to_address.apartment_number}. Стоимость {send.cost} рублей."
)
