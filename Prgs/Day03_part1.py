'''
======================SETS============================
s1 = {'abcd','abc1',1200, 3.7,'abcd'}
print(s1)

thisset = {"apple", "banana", "cherry", True, 1, 2,False, 0}

print(thisset)

l1 =['abcd1', 1,'abcd1',3,4,5,1]

print(l1)
s2 = set(l1)
print(s2)
l1 = list(s2)
print(l1)

s2.add(6)
s2.add(7.7)
s2.add(5)
print(s2)

s1.update(s2)
print("S1: ",s1)
print(s2)

s1 = {1,2,3,4,5}
s2 = {1,3,6,7,8,5}

#print(s1.intersection(s2))
print(s1.union(s2))
s1.update("45")
print(s1)

# a,b,c = map(int,input().split())

s1.remove('5')
print(s1)
s1.discard('4')
print(s1)

s1 = {1,2,3,4}
s2 = {4,5,6,8}
s2 = s1
print(s2, id(s1), id(s2))

print({1, 2, 3, 4}.symmetric_difference({2, 3, 4,5,8,9}))
print({1,2,5}.issuperset({1,2,3,5}))
==================================================
'''


l = []
for i in range(1,101):
    if i%2 == 0:
        l.append(i)

print(l)


l1 = [val**2 for val in range(1,15) if val%2 != 0] + [val**2 for val in range(1,15) if val%2 == 0]
print(l1)
#[1,3,5,2,4,6]

l1 =[1,2,3,4,5]
# l2 = [True, False,True, False,True]
# 'i' in "bhima"
l2 = [0 if i%2 == 0 else 1 for i in l1]
'''for i in l1:
    if i%2 == 0:
        l2.append(False)
    else:
        l2.append(True)
'''
print(l2)