#class Address:
    #def __init__(self, index, city, street, house, apartment):
        #self.index = index
        #self.city = city
        #self.street = street
        #self.house = house
        #self.apartment = apartment

    #@property
    #def full_address(self):
        #return f"{self.street}, {self.house}, {self.apartment}, {self.city}, {self.index}"

#class Mailing:
    #def __init__(
        #self,
        #to_address,
        #from_address,
    #):
        #self.to_address = to_address
        #self.from_address = from_address

    #@property
    #def to(self):
        #return self.to_address.full_address

    #@property
    #def from_(self):
        #return self.from_address


class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.aptamet = apartment
    
    @property
    def get_full_address(self): 
        return "{}, {}, {}, {}, {}".format(self.street, self.house, self.aptamet, self.city, self.index)


class Mailing(object):

    to_address = Address("123456", "Moscow", "Lenina", "12", "3")
    from_address= Address("234567", "St.Petersburg", "Pushkin", "5", "2")

    track = "ABC123ABC"
    cost = 100

def print_address(track, from_address, to_address, cost):
    print("Отправление ", track, from_address, "в", to_address, ". Стоимость - ", cost, ".")
print_address(Mailing.track, Mailing.from_address, Mailing.to_address, Mailing.cost)