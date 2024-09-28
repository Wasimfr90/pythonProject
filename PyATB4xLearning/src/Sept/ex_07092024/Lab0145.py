

class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from excel")

class MYSQLDBConnection:

    @staticmethod
    def readMYSQLFile():
        print("Reading from MY SQL")


# No need to Inherit from super/parent class, if the method is @staticmethod
# Directly we can call.


class TC1:
    def runTC1(self):
        ExcelReader().readExcelFile()
        MYSQLDBConnection().readMYSQLFile()


tc1 = TC1()
tc1.runTC1()