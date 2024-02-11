class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

    def disp(self):
        print("Hello")


my_iter = MyIterator([10, 20, 30, 40, 50])

my_iter.disp()
print(type(my_iter))

x = iter(my_iter)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
