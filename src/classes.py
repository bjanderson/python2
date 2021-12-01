from models.address import Address
from models.person import Person
from models.student import Student

if __name__ == "__main__":
    address1 = Address("123 Main St.", "Fredricksburg", "VA", 22400)
    address2 = Address("234 Main St.", "Fredricksburg", "VA", 22400)

    bob = Person(20, address1)
    alice = Person(22, address2)

    bob.tellAge()
    bob.tellAddress()
    alice.tellAge()
    alice.tellAddress()

    chuck = Student(15, address1, 123)
    dave = Student(16, address2, 4567)

    chuck.tellId("hello")
    chuck.tellAge()
    chuck.tellAddress()
