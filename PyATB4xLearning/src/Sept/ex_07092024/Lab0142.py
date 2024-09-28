# Abstraction example

from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class GearBox(ABC):

    @abstractmethod
    def setGear(self):
        pass

class Car(Engine):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stop")

    def setGear(self):
        print("Gearbox is ready")

    def drive(self):
        self.start()
        self.setGear()
        self.stop()

car = Car()
car.drive()