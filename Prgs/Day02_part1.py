str1 = "012345"
      #-6-5-4-3-2-1
print(str1[7:60])
'''
neg step
1. start is greater than stop index
'''


print(str1[-6:-1])
'''
str2 = r"this is\\nPython Class"
str3 = R"C:\\Windows\\Users\\neha"
print(str2)
print(str3)
print("%02.2f"%(2.34568))

str5 = "BHIMA"
str5 = str5.center(1,"*")
print(str5)

str6 = "This,is,Python Class Python Python"
list1 = str6.split(',')

print(list1)
for l1 in list1:
    print(l1, type(l1))

# a,b,c = map(int,input().split())
# print(a,b,c, type(a))

str7 = "This is a python Programming Class v0.1".replace("Python", "Java",2)
print(str6+"\n"+str7)

str8 = str6.casefold().replace("python", "java")
print(type(str8), str8)


str9 = "This is Python Class".replace("Python", "Java").replace("Class", "Tution")
print(str9)

str10 = "This is Python Class is is is"
str11 = str10.index("is")
print(str11, type(str11))

str12 = "This is Python Class"
list1 =['Bhima', 'Shankar', 'Bangalore']
l1 = str12.split()
print(l1[2])
l1[2] = "Java"
print(l1[2])
print(" ".join(l1))
print(str12.endswith("ss"))
print(str12.startswith("this"))


'''
'''

for i in range(10):
    print(i)
else:
    print("For: Executed after loop")

i = 1

while i<10:
    print(i)

    if i==5:
        break
    i+=1
else:
    #acc +=1
    print(f"count: {i}")
'''