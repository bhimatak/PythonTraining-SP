class Person:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age

    def printPerson(self):
        print(f"Name: {self.__name}\n"
              f"Age: {self.__age}")

    def setName(self, name=None):
        self.__name = name

    def setAge(self, age=0):
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age


class Address:
    def __init__(self, address=None, state=None, pCode=0):
        self.__address = address
        self.__state = state
        self.__pinCode = pCode

    def printAddress(self):
        print(f"Address: {self.__address}\n"
              f"State: {self.__state}\n"
              f"PinCode: {self.__pinCode}")


class Employee(Person, Address):
    def __init__(self, id=0, sal=0, name=None, age=0, address=None, state=None, pCode=0):
        Person.__init__(self, name, age)
        Address.__init__(self, address, state, pCode)
        self.__id = id
        self.__sal = sal

    def printEmp(self):
        print(f"ID: {self.__id}\n"
              f"Salary: {self.__sal}")


e2 = Employee(102, 20000, "bhima", 45, "Gulbarga", "Karnataka", 585102)
print("=======================")
e2.printPerson()
e2.printAddress()
e2.printEmp()
