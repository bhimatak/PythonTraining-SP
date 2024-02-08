'''
define a class of rectangle
width and height

r1 = h10,w20
r2 = h30,w40

rest = r1+r2 = h40,w60


'''

class Rectangle:

    def __init__(self,h=0,w=0):
        self.__h = h
        self.__w = w

    def printDetails(self):
        print(f"Height: {self.__h}\nWidth: {self.__w}")

    def setH(self):
        self.__h = int(input("Enter Height: "))
    def setW(self):
        self.__w = int(input("Enter Width: "))

    def getH(self):
        return self.__h
    def getW(self):
        return self.__w


r1 = Rectangle()
print("Enter the details of rect1")
r1.setH()
r1.setW()
print("\nDetails of Rec1")
r1.printDetails()
r2 = Rectangle()
r2.setH()
r2.setW()
print("\nDetails of Rec2")
r2.printDetails()

print(type(r1), type(r2))
res = Rectangle(10,20)
resultRec = Rectangle(r1.getH()+r2.getH(),r1.getW()+r2.getW())

resultRec.printDetails()
print(type(resultRec))

