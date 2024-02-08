class Person:
    def __init__(self, name="XYZ", phno=0):
        self.__name = name
        self.__phno = phno

    def printDetails(self):
        print(f"Name: {self.__name}\nPhno: {self.__phno}")

class Emp(Person):

    def __init__(self, id,sal):
        self.__id = id
        self.__sal = sal

    def printDetEmp(self):
        print(f"ID: {self.__id}\nSalary: {self.__sal}")

e1 = Emp(101,10000)

e1.printDetails()
e1.printDetEmp()