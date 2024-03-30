from address import Address
from mailing import Mailing

from_address = Address('614000', 'Perm', 'Lenina', 1, 8)
to_address = Address('617073', 'Krasnokamsk', 'Kommunisticheskaya', 12, 44)
user_mailing = Mailing(to_address, from_address, 100, '6677899')

print(f'Отправление {user_mailing.track} из {user_mailing.from_address} в {user_mailing.to_address}. Стоимость {user_mailing.cost} рублей.')