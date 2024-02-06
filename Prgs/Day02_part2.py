l = []
print(l,type(l))
l.append(10)
l.append(11)
l.append(12)

for i in range(len(l)):
    print(l[i],end=" ")
print()
l.insert(0,101)
print(l)
l.pop(0)
print(l)
print(l[::-1])
l[0] = 555
print(l)
l = ['bhima', 101,102.2]
print(l)

l =[1,2,3]*3
print(l)
l1 = [1,2,3]
l2 = [4,5,6]
l1 +=l2

print(l1, max(l1), min(l1))
str1 = "abcde"
l3 = list(range(1,101,2))
print(l3, type(l3))

l4 = [1,2,3,1,4,2,5,3]
print(l4.count(1))
print(l4.index(2))
l4.remove(3)
print(l4)
l4.reverse()
print(l4)
l4.sort(reverse=True)
print(l4)

'''
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)
'''

