from mailing import Mailing
def print_address(track, from_address, to_address, cost):
    print("Отправление ", track, from_address, "в", to_address, ". Стоимость - ", cost, ".")
print_address(Mailing.track, Mailing.from_address, Mailing.to_address, Mailing.cost)