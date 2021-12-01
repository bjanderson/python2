
class Person:
    def __init__(self, age, address):
        self.age = age
        self.address = address

    def tellAge(self):
        print(f"I am {self.age} years old.")

    def tellAddress(self):
        print(self.address.toString())
