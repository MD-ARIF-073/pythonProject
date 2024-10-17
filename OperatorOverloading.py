

class MyNum():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return (self.value * 2) + (other.value * 2)


a = MyNum(2)
b = MyNum(3)

c = a + b

print(c)



class MyInt():
    def __init__(self, value):
        self.__value = value

    def __int__(self):
        return self.__value

    def __add__(self, other):
        return self.__value + int(other) * int(other)


a = MyInt(2)
b = MyInt(3)

c = a + b

print(c)


class MyInt():
    def __init__(self, value):
        self.__value = value

    def __int__(self):
        return self.__value


    def __iadd__(self, other):
        return self.__value + int(other) * int(other)


a = MyInt(2)

a += MyInt(3)

print(a)