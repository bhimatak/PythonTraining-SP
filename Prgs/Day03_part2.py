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

def f3(x,y):
    return x+y

a = {10,20,30,101,102}
b = {40,50,60,70,35}

l6 = list(map(f3,a,b))
print(l6)
