# Abstraction example

from abc import ABC, abstractmethod

class PyATB(ABC):

    @abstractmethod
    def payFees(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Wasim(PyATB):

    def payFees(self):
        print("Paid")

was = Wasim()
was.enrolled()