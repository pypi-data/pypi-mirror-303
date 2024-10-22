import math


class ShowAccess:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__[self.name]
        print(f"Get {self.name} = {value}")
        return value

    def __set__(self, instance, value):
        print(f"Set {self.name} = {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        value = instance.__dict__.pop(self.name, None)
        if value is not None:
            print(f"Delete {self.name} = {value}")


class Circle:
    radius = ShowAccess()
    
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2



if __name__ == "__main__":
    c = Circle(int(input('Введите радиус')))
    print(c.area)
    del c.radius