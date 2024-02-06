from math import *
str1 = "BhIma"
# print(str1.casefold())
print(str1.encode(encoding='utf-32'))
str2 = '01\t012\t0123\t01234'
print(str2.expandtabs(2))

d1 = {1:2,3:4}

str3 = "bhima"
s1 =10
s2 = 20
print("This is format {0},{1},{2},{3}".format(str1,s1,s2,d1))
print(d1[1])
l = list(str3)
l[2]='H'
str4 = "".join(l)
print(str4)
print(pow(2,3))
print(sqrt(4))
print(factorial(5))
print(pi)