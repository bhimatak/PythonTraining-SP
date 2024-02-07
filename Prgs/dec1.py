def outter_fun(func):
    print("Dec 1")
    def inner_func(str1):
        print("inner function")

        print(str1)
        ret = func(str1)
        print("inside inner_function: ",ret)
        ret = list(ret)
        return ret
    print("Exiting from outer function")
    # func()
    return inner_func

@outter_fun
def f1(str1):
    # print("f1")
    str1 = "0001"+str1
    return str1

@outter_fun
def f2(str1):
    # print("f1")
    str1 = "0002"+str1
    return str1
print("===================================")
f1("Amit")
f2("Sneha")
'''

in1 = outter_fun(f1)
print(in1)
retval = in1("Bhima")
print(retval)


r1 = f1("Bhima")
print(r1)
'''