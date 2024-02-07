def myfun(n):
    if n <3:
        return True
    else:
        return False

a = filter(myfun, [1,2,3,4])
print(list(a))
print('{:09.3f}'.format(33.3))