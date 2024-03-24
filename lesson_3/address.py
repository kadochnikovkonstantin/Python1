class Address:
    
        def __init__(self, index, city, street, house, apartment):
            self.index = index
            self.city = city
            self.street = street
            self.house = house
            self.apartment = apartment
    
        def sayIndex(self):
            print(self.index)

        def sayCity(self):
            print(self.city)

        def sayStreet(self):
            print(self.street)

        def sayHouse(self):
            print(self.house)

        def sayApartment(self):
            print(self.apartment)
