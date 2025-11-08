from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address       # Address
        self.from_address = from_address   # Address
        self.cost = cost                   # число
        self.track = track                 # строка