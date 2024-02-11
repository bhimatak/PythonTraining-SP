
'''
fp = open("test1.txt","a")

print(fp.tell())
'''


'''content = fp.readline()
print(content, type(content))
print(fp.tell())
content = fp.readline()
print(content, type(content))
print(fp.tell())
fp.seek(0)
content = fp.readline()
print(content)
'''
'''
fp.write("Appended")





fp.close()

'''

fileName2 = input("Enter the 1 file name: ")
'''
fileName2 = input("Enter the 2 file name: ")
with open(fileName1, "r") as fp:
    str1 = fp.read()
    # print(str1)
'''
with open(fileName2, "w+") as fp:
    str1 = fp.read()
    print(str1)
    str1 += "Second String appended hello"
    fp.write(str1)


