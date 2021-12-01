
class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def toString(self):
        return f"{self.street}\n{self.city}, {self.state} {self.zipcode}"
