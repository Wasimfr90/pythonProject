# Abstraction


from abc import ABC, abstractmethod

class Father(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass


class Pramod(Father):
    pass

    # def loan(self):
    #     print("paid the loan")

pramod = Pramod("1L")
pramod.loan()
