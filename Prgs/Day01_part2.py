'''
Q1 .Print series 0,3,8,15,24,35,48,63,80,99
n = 10
'''
'''
i = 1
n = 10
while i<=n:
    if i == n:
        print((i*i)-1)
    else:
        print((i*i)-1, end=",")
    i+=1
# print("\b")
'''
'''
test = input("Enter the val: ")
print(type(test), test, id(test))
test = int(test)
print(type(test), test,id(test))
test2 = int(input("Enter the val: "))
print(type(test2), test2,id(test2))

i = 1
j = 1

while i<=5:
    print(f"i={i}", end=" ")
    j=1
    while j<=3:
        print("j=",j, end=" ")
        j+=1
    print()
    i+=1
'''
'''
Q2 .
n = 5
*
* *
* * *
* * * *
* * * * *
'''
'''
for(i=0;i<5;i++)
    for(j=0;j<=i;j++)
        printf("* ");
    printf("\n");
'''
# n = int(input("n: "))
# i = 1
# j = 1
'''
while i<=n:
    j = 1
    while j<=i:
        print("* ", end="")
        j += 1
    print()
    i+=1

print("hello"*5)
'''
'''
while i<=n:
    print("* "*i, end="")
    i+=1
    print()
'''
'''
for i in (11,201.1,301,"bhima",41):
    print(i,type(i))
MAX = 15
START = 10
i = 0
j = 0
for i in range(START,MAX,2):
    print(i, end=" ")
    for j in range(1,5):
        print(j)
    print()
print(j)


n = 5
for i in range(1,(n*n)+1):
    if i%n == 0:
        print(i)
    else:
        print(i, end="*")

sum = 0

n = 12345

while n:
    r = n%10

    sum=sum*10+r
    # print(sum)
    n = n//10
    # print("n: ",n)
print(sum)

'''
'''
flag = False
for i in range(1,11):
    for j in range(101,103):
        if i >= 6 or j == 102:
            if i>=6:
                flag = True
            break
        print("J: ",j)
    if flag:
        break
    print("I: ",i)

'''
'''
for i in range(1,11):
    if i >= 6:
        print("Continue Executed")
        i -= 5
        continue
        print("Skipped")
    print(i)
'''


str1 = "Bhima"

print(str1[len(str1)-1])
start = 0
end = len(str1)-1
print(str1[:-1:1])



