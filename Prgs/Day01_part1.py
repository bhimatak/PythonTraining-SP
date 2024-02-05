'''
str1 = "hello"
print(str1)
str2 = "this is pyhon's class"
print(str2, type(str2))
str3 = 'this is "Python" class'
print(str3)

str4 = "Hello " + "World"
print(str4)
'''
#str5 = '''
#Hello
'''

print(str5)
print(ord('\n'))
print(chr(65))

for i in range(len(str5)):
    print(ord(str5[i]))
'''
'''
a = int(10.15)
print(type(a),a)
b = float(101)
print(type(b), b)
c = str(102)
print(type(c),c)

for i in range(len(c)):
    print(ord(c[i]))

d = str(103.3)
print(type(d),d)

for i in range(len(d)):
    print(ord(d[i]))

a = 10//3
print(type(a), a)

c = a**3
print(type(c), c)


a = [1,2,3,4,5]

if 'w' not in "Hello World":
    print("True")
else:
    print("False")


str1 = "Hello"
for i in str1:
    print(i)

a = 5
print(bin(a))
c = a&1
print(c)


a=10
b=20
c=5
if (a<b) or (a<c):
    print("Hello")
else:
    print("World")
a = -1
b = not a
print(b)

print(help('keywords'))
help('global')
'''
'''
a="this is a Python"
b="Class"
c="Programming"
print(a,b,c, sep="*")

print(f'%s %s %s %d'%(a,b,c,10),end="====")
print()
d = f'{a} {b} {c} '+ str(10)
print(f'{a} {b} {c}')
print(d)
'''

a = 10
b = 20

if a>b:
    if True:
        pass
    pass
print("Hello")
print("Welcome")







