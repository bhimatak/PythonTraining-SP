a=10
b=10


try:
    if b==0:
        raise ValueError(f"b's Value is {b}")

    c = a/b
except ValueError as v:
    print(v, type(v))

except Exception as e:
    print(type(e))
    e = "got 0 in the division part "+str(e)
    print(e)
    print(type(e))
else:
    print(c)

