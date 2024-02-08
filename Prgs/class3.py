class Person:
    NAME = "XYZ"
    def __init__(self, name="XYZ", phno=0):
        self._name = name
        self._phno = phno

    def printDetails(self):
        print(f"Name: {self._name}\nPhno: {self._phno}")

    def getName(self):
        return self._name

    def getPhno(self):
        return self._phno


class Emp(Person):

    def __init__(self, id,sal,name1,phno1):
        super().__init__(name1,phno1)
        self.__id = id
        self.__sal = sal

    def printDetEmp(self):
        print(self.NAME)
        # print(self.getPhno())
        print(f"ID: {self.__id}\nSalary: {self.__sal}")


e1 = Emp(101, 10000,"bhima", 9998888)

# e1.printDetails()
e1.printDetEmp()
e1.printDetails()