# Abstraction example

from abc import ABC, abstractmethod

class Browser(ABC):

    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass


class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass

class TC1(Browser):

    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("Gearbox is ready")

    def runTC(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()

tc1 = TC1()
tc1.runTC()