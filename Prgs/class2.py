class Person:
    NoOfPersons = 0
    def __init__(self, age=0, name="", phno=0):
        self.__age = age
        self.__name = name
        self.__phone = phno

    def __str__(self):
        str1 = (f'Name: {self.__name}\n'
                f'Age: {self.__age}\n'
                f'PhNo: {self.__phone}\n')
        return str1
    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPhNo(self, phno):
        self.__phone = phno

    def getPhNo(self):
        return self.__phone

    def printDetails(s):
        print("====Persons Details are====")
        print(f"Name: {s.__name}")
        print(f"Age: {s.__age}")
        print(f"Phno: {s.__phone}")




p1 = Person(10)
p1.printDetails()
print("===================")
p1.setAge(45)
p1.setName("Bhima")
p1.setPhNo(9980156833)
p1.printDetails()

print(p1.getPhNo())
p2 = Person()
p2.printDetails()



