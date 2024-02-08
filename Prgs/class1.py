class Emp:
    NoofEmps = 0
    #constructor of the class
    def __init__(myself, id=0, name=""):
        myself._empid = id
        myself._name = name
        Emp.NoofEmps +=1

    def getDetails(self):
        self._name = input("Enter the New Emp Name: ")
        self._empid = int(input("Enter ID"))

    def printDetails(myself):
        print(myself._name)
        print(myself._empid)
        print(Emp.NoofEmps)


'''
e1 = Emp()
# print(type(e1))
print("================")
print(e1.NoofEmps)
e1.printDetails()
e2 = Emp()
e2.printDetails()
print("================")

e2.name = "xyz"
e1.printDetails()
e2.printDetails()
print("================")
Emp.NoofEmps = 101
e1.printDetails()
e2.printDetails()

print("================")
e1.NoofEmps=102
e1.printDetails()
e2.printDetails()
'''
'''
e1 = Emp(101,"bhima")
print("Created e1",Emp.NoofEmps)
e2 = Emp(102,"shankar")
e1.printDetails()

e2.printDetails()
print("Created e2",Emp.NoofEmps)
Emp.NoofEmps = 3000
e1.printDetails()
print("After",Emp.NoofEmps)
e2.printDetails()
'''

e1 = Emp(101,"bhima")
e1.printDetails()
print("============================")
e1.getDetails()
e1.printDetails()

e2 = e1
e2.printDetails()

