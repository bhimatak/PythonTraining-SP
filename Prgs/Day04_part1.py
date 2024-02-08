# class Emp:
#     pass
#
# e1 = Emp()
#
# print(type(e1))

def f1():
    print("hello1")

def f2():
    print("hello2")

def main():
    print("Main Method")
    f1()
    f2()

if __name__ == "__main__":
    print("Hello Welocome to Day04")
    main()

    print("Exiting from main day04")
    print(dir())
else:
    print("using in other module",__name__)