
from models.person import Person


class Student(Person):
    def __init__(self, age, address, studentId):
        super().__init__(age, address)
        self.studentId = studentId

    def tellId(self, word):
        print(f"My id is {self.studentId}, {word}")
