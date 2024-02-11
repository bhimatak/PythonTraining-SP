class Test:
    pass

t1 = Test()

setattr(t1,'x',10)

print(t1.x)

t2 = Test()
print(t2.x)
