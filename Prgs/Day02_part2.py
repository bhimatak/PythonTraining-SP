'''
===================================================

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
===================================================
'''
'''
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)
'''

t1 = (1,2,3)

print(t1,id(t1))

for i in range(len(t1)):
    print(t1[i])

t2 = ()
print(type(t2))

l = list(t1)
l[1] = 101
t1 = tuple(l)
print(t1, id(t1))

t3 = (4,5,6)*3
print(t1+t3)
t4 =tuple(range(5))
print(t4, type(t4))

d1 = {"die":"end of life"}

print(type(d1),d1)
print(d1['die'])

d2 = {'name':['alias','fname']}
print(d2['name'][1])

d1['die'] = 'new life'
d1['name'] = "alias"

print(d1,len(d1))

for (key,value) in d1.items():
    print(key,type(value))

d3 = {'key1':[1,2,3,4,5],'key2':(101,102,103),'key3':['10',20,33.3]}
l1 =[]
for t1 in d3:
    l1.append(t1)
print(l1)
for i in range(len(l1)):
    if l1[i] == 'key2':
        d3['key2'] = "Bhima"
print(d3)

d4 = {}
d4['key1']="bhima"
print(d4)
d4['key2']="abcd1"
print(d4)
d4['key1']='abcd2'
print(d4)
d5 = {'key1':{'1':201,'2':301,'3':401}}

print(d5['key1'], type(d5['key1']))
print(d5['key1']['1'])
print(type(d5['key1']))
print(type(type(dict)))

if type(d5['key1']) == type(type(dict)):
    print("Yes")
else:
    print("No")