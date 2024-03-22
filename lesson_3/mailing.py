from address import Address
class Mailing(object):

    to_address = Address("123456", "Moscow", "Lenina", "12", "3")
    from_address= Address("234567", "St.Petersburg", "Pushkin", "5", "2")

    track = "ABC123ABC"
    cost = 100