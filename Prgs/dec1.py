def outter_fun():
    print("Dec 1")
    def inner_func():
        print("inner function")

        # print()
        return "hello world"
    print("Exiting from outer function")
    return inner_func

def f1():
    return "hello1"

in1 = outter_fun()
print(in1)
in1()

