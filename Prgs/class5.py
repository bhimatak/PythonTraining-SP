class Foo(object):
    def __init__(self):
        print("foo init")
class Bar(object):
    def __init__(self):
        print("bar init")
class FooBar(Foo, Bar):
    def __init__(self):
        print("foobar init")
        super(FooBar, self).__init__()

test = FooBar()
print(isinstance(test,FooBar))
print(isinstance(test,Bar))
print(isinstance(test, Foo))

