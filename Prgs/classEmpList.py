class Person:
    def __init__(self,name=None,age=0):
        self.__name = name
        self.__age = age

    def setPDetails(self):
        # print("Enter Personal Details")
        self.__name = input("Name: ")
        self.__age = int(input("Age: "))
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

    def setAddDetails(self):
        # print("Enter Address")
        self.__address = input("Address: ")
        self.__State = input("State: ")
        self.__pinCode = int(input("PinCode: "))
    def getAddress(self):
        return self.__address

    def setAddress(self, value=None):
        self.__address = value


    def getState(self):
        return self.__State


    def setState(self, value=None):
        self.__State = value


    def getPinCode(self):
        return self.__pinCode

    def setPinCode(self, value=0):
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

    def setEmpDetails(self):
        self.setPDetails()
        self.setAddDetails()
        # print("Enter Employee Details")
        self.__id = int(input("ID: "))
        self.__sal = int(input("Salary: "))
    def getId(self):
        return self.__id

    def setId(self, value=0):
        self.__id = value

    def getSal(self):
        return self.__sal

    def setSal(self, value=0):
        self.__sal = value



    def printEmp(self):
        print(f"ID: {self.__id}\n"
              f"Salary: {self.__sal}")

    def printEmpDetails(self):
        print("========================")
        self.printPerson()
        self.printAddress()
        print(f"ID: {self.__id}\n"
              f"Salary: {self.__sal}")
        print("========================")


EmpList = [Employee() for i in range(3)]
def disEmpRecs():
    # global EmpList
    for i in range(3):
        print(f"Employee {i + 1} Details")
        EmpList[i].printEmpDetails()
def setEmpRecs():
    # global EmpList
    for i in range(3):
        print(f"Employee {i + 1} Details")
        EmpList[i].setEmpDetails()


def main():
    # global EmpList
    for i in range(3):
        EmpList.append(Employee())
    setEmpRecs()
    disEmpRecs()

if __name__ == "__main__":
    main()








'''
change emp2 details by search and update
'''

fName = input("Find Name: ")
flag = False
for i in range(3):
    # print(f"Employee {i + 1} Details")
    if EmpList[i].getName() == fName:
        print("found")

        EmpList[i].setPinCode(int(input("Enter New PinCode: ")))
        print("Pin Code Updated Successfully")
        flag = True
        break

if flag == False:
    print("Employee Not Found")

disEmpRecs()