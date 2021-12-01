from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime


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


class Car(Vehicle):

    def __init__(self, createdDate):
        super().__init__(createdDate)

    @property
    def modeOfTransport(self):
        return 'land'

    def move(self):
        print(f"moving...")


myCar = Car(datetime.now())
myCar.move()
myCar.areWeThereYet()
myCar.howDoYouMove()


interface CountFishInterface:
    "Fish counting interface"

    def oneFish():
        "Increments the fish count by one"

    def twoFish():
        "Increments the fish count by two"

    def getFishCount():
        "Returns the fish count"
