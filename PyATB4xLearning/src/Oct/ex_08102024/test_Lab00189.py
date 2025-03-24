# Reading from a .csv file
# a. import pandan - in-built library function
# b. import csv - file
import pandas as pd
import csv



class Test_CRED():

    #using csv
    def test_update_1(self):
        with open('PyATB4xLearning/src/Oct/ex_08102024/userdata.csv') as csvfile:
            reader =  csv.reader(csvfile)
            for row in reader:
                print(row[0], row[1])

    #using pandas
    def test_update_2(self):
        df = pd.read_csv('PyATB4xLearning/src/Oct/ex_08102024/userdata.csv')
        print(df)

