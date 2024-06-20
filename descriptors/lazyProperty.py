import time


class lazyProperty:
    def __init__(self, func) -> None:
        self.name = func.__name__
        self.func = func
        print(f"func name {self.name}  {self.func}")

    def __get__(self, obj, owner=None):
        print(f"in {obj} {owner}")
        obj.__dict__[self.name] = self.func(obj)
        return obj.__dict__[self.name]


class Car:
    @lazyProperty
    def transform_car(self):
        time.sleep(3)
        print("Transfomed the car after 3 seconds")


car = Car()
car.transform_car


class Alpha:
    def __init__(self, p):
        print(f"Alpha initialized with p = {p}")


class Beta:
    def __init__(self, q):
        print(f"Beta initialized with q = {q}")


class Gamma(Alpha, Beta):
    def __init__(self, p, q=None):
        super(Gamma, self).__init__(p=1000)
        super(Alpha, self).__init__(q=q)
        super(Beta, self).__init__()
        print("Gamma initialized")


gamma_instance = Gamma(p=10, q=20)


# descriptors.py
class Verbose_attribute:
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42

    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        return f"here is the value: {value}"
        # raise AttributeError("Cannot change the value")


class Foo:
    attribute1 = Verbose_attribute()


my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
my_foo_object.atr = 120
my_foo_object.attribute1 = 12220
