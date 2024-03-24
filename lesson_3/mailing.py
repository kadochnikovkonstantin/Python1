class Mailing:

        def __init__(self, to_address, from_address, cost, track):
            self.to_address = to_address
            self.from_address = from_address
            self.cost = cost
            self.track = track
        
        def sayTrack(self):
            print(self.track)

        def sayTo_address(self):
            print(self.to_address)

        def sayFrom_address(self):
            print(self.from_address)

        def sayCost(self):
            print(self.cost)