from address import Address


class Mailing:
    """Класс почтового направления"""

    to_address: Address
    from_address: Address
    cost: float
    track: str

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
