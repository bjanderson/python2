from abc import ABC, abstractmethod, abstractproperty


class Vehicle(ABC):

    def __init__(self, createdDate):
        self.createdDate = createdDate

    @abstractproperty
    def modeOfTransport(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def areWeThereYet(self):
        print('A couple more minutes...')
        self.move()

    def howDoYouMove(self):
        print(f"I move by {self.modeOfTransport}")
