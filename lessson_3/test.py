class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def print_address(self):
        print(f"Индекс: {self.index}, Город: {self.city}, Улица: {self.street}, Дом: {self.house}, Квартира: {self.apartment}")

from Address import Address

class Mailing:
    def __init__(
        self,
        to_address,
        from_address,
        track,
        cost
    ):
        self.to_address = Address(to_address)
        self.from_address = Address(from_address)
        self.track = track
        self.cost = float(cost)
