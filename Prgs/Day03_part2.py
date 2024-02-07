'''
def f1(a,b=0):
    print(a,b)
    return [i for i in range(a)]

ret = f1(10)
print(ret, type(ret))

def f2(*args):
    print(type(args))
    for i in range(len(args)):
        print(args[i], type(args[i]))


f2(10,20,30)
'''
'''
def f3(**kwargs):
    print(type(kwargs))
    for key,val in kwargs.items():
        print(key,val)

d1 = {'a':1,'b':2}
f3()

x = lambda val: val**3

print(x(2))
print(x(3))
print(x(4))

'''
'''def f1(x):
    return x**3
'''
'''
x = lambda n: n**2
y = lambda x(num): 
print(x(x(2)))


'''

def f1(x):
    if x%2 == 0:
        return x**2
    else:
        return x**3

l1 = [1,2,3,4,5]
l4 = [5,6,7,8,9]
s1 = {1,2,3}
s2 = {4,5,6}

l3 = []
for i in l1:
    l3.append(f1(i))
print(l3)

l5 = tuple(map(f1,l1))
print(l5, type(l5))
def f2(str1):
    str1 +="101"
    return str1

str2 = "ABCD"
l6 = list(map(f2,str2))
str4 ="".join(l6)
print(str4)


'''
a=10
b=20

l3 = list(map(f1, l1))
print(l3)
'''
'''
def f3(x,y):
    return x+y

a = {10,20,30,101,102}
b = {40,50,60,70,35}

l6 = list(map(f3,a,b))
print(l6)
'''
'''
def f1(x):
    if x<18:
        return False
    else:
        return True

list1 = list(filter(f1, [5,8,18,20,3,22]))
print(list1, type(list1))

# for i in list1:
#     print(i)
x = iter(list1)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
'''
'''
def f1():
    for i in range(11):
        if i%2 == 0:
            yield i

l1 = f1()
print(l1, type(l1))
for i in l1:
    print(i)
l2 = f1()
print(l2, type(l2))

for x in f1():
    print(x)
'''



def func1():
    print("Hello1")

def func2():
    print("hello2")
f = func1

# print(f, type(f))
# f()

f = func2
# print(f, type(f))
# f()

print("=================================")
def retFunc(f):
    print("in the retFunc")
    def func1():
        print("hello")
    func1()
    print("out of retFunc")
    return f

'''
str1 ="bhima"
print(id(str1))
str1 = str1+"Shankar"
print(id(str1))
'''
# func1 = retFunc(func1)
#
# func1()
# retFunc(func2)

@retFunc
def func3():
    print("hello 3")

func3()



