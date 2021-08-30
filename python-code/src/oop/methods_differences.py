from __future__ import annotations

import math
from typing import List


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'


obj = MyClass()
print(obj.method())  # ('instance method called', <__main__.MyClass object at 0x102addf10>)

# This confirmed that method (the instance method) has access to the object instance (printed as <MyClass instance>)
# via the self argument.

# When the method is called, Python replaces the self argument with the instance object, obj.

print(MyClass.method(obj))  # another way to call instance method

print(obj.class_method())  # ('class method called', <class '__main__.MyClass'>)

# Calling classmethod() showed us it doesn’t have access to the <MyClass instance> object, but only to the <class
# MyClass> object, representing the class itself (everything in Python is an object, even classes themselves).

print(obj.static_method())  # static method called

# Behind the scenes Python simply enforces the access restrictions by not passing in the self or the cls argument
# when a static method gets called using the dot syntax.
#
# This confirms that static methods can neither access the object instance state nor the class state. They work like
# regular functions but belong to the class’s (and every instance’s) namespace.

# Calling different methods on a class level
print(MyClass.class_method())
print(MyClass.static_method())


# print(MyClass.method()) - TypeError: method() missing 1 required positional argument: 'self'


class Pizza:
    def __init__(self, ingredients: List, radius: int):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

    @classmethod
    def margherita(cls, radius) -> Pizza:
        return cls(['mozzarella', 'tomatoes'], radius)

    @classmethod
    def prosciutto(cls, radius) -> Pizza:
        return cls(['mozzarella', 'tomatoes', 'ham'], radius)


margherita_small = Pizza.margherita(4)
prosciutto_big = Pizza.prosciutto(10)

print(margherita_small)
print(prosciutto_big)