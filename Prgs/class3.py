class Person:
    NAME = "XYZ"
    def __init__(self, name="XYZ", phno=0):
        self.__name = name
        self.__phno = phno

    def printDetails(self):
        print(f"Name: {self.__name}\nPhno: {self.__phno}")

    def getName(self):
        return self.__name

    def getPhno(self):
        return self.__phno


class Emp(Person):

    def __init__(self, id,sal,name1,phno1):
        super().__init__(name1,phno1)
        self.__id = id
        self.__sal = sal

    def printDetEmp(self):
        # print(self.NAME)
        # print(self.getPhno())
        print(f"ID: {self.__id}\nSalary: {self.__sal}")


e1 = Emp(101, 10000,"bhima", 9998888)

# e1.printDetails()
e1.printDetEmp()
e1.printDetails()
