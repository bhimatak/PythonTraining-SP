class Person:
    def __init__(self,name=None,age=0):
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

    def __init__(self,address=None,state=None,pCode=0):
        self.__address = address
        self.__State = state
        self.__pinCode = pCode


    def getAddress(self):
        return self.__address

    def setAddress(self, value=None):
        self.__address = value


    def State(self):
        return self.__State


    def State(self, value=None):
        self.__State = value


    def pinCode(self):
        return self.__pinCode

    def pinCode(self, value=0):
        self.__pinCode = value


    def printAddress(self):
        print(f"Address: {self.__address}\n"
              f"State: {self.__State}\n"
              f"PinCode: {self.__pinCode}")


class Employee(Person, Address):

    def __init__(self, id=0,sal=0,name=None,age=0,address=None,state=None,pCode=0):
        # super(Employee,self).__init__(address=None,state=None,pCode=0)
        Person.__init__(self,name,age)
        Address.__init__(self,address,state,pCode)
        self.__id = id
        self.__sal = sal


    def id(self):
        return self.__id

    def id(self, value=0):
        self.__id = value

    def sal(self):
        return self.__sal

    def sal(self, value=0):
        self.__sal = value

    def printEmp(self):
        print(f"ID: {self.__id}\n"
              f"Salary: {self.__sal}")


e1 = Employee(sal=10000,id=101)
print(Employee.__mro__) # method resolution object
'''
(<class '__main__.Employee'>, <class '__main__.Person'>, <class '__main__.Address'>, <class 'object'>)

'''
e1.printEmp()

e2 = Employee(102,20000,"bhima",45,"Gulbarga",
              "Karnataka",585102)
print("=======================")
e2.printPerson()
e2.printAddress()
e2.printEmp()


