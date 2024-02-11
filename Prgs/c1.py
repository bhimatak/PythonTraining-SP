class A:
    def __init__(self, a,b):
        self.__a =a
        self.__b =b

    def printDetAB(self):
        print(f'A: {self.__a}\nB: {self.__b}')


class B(A):
    def __init__(self, x,y,a,b):
        super().__init__(a,b)
        self.__x =x
        self.__y =y

    def printDetXY(self):
        print(f'X: {self.__x}\nY: {self.__y}')
        #self.printDetAB()


ob1 = B(10,20,30,40)
ob1.printDetXY()
#ob1.printDetAB()