x = {'foo', 'bar', 'baz', 'foo', 'qux', 'bar'}

print(type(x))
print(x)

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])

print(type(x))
print(x)

x = set(('foo', 'bar', 'baz', 'foo', 'qux'))

print(type(x))
print(x)

_str = "quux"

print(list(_str))
print(set(_str))

# A set can be empty. However, recall that Python interprets empty curly braces ({}) as an empty dictionary,
# so the only way to define an empty set is with the set() function

x = set()
print(type(x))
print(x)

x = {}
print(type(x))
print(x)

# You might think the most intuitive sets would contain similar objects—for example, even numbers or surnames:

s1 = {2, 4, 6, 8, 10}
s2 = {'Smith', 'McArthur', 'Wilson', 'Johansson'}

# Python does not require this, though. The elements in a set can be objects of different types:
x = {42, 'foo', 3.14159, None}
print(x)

# Don’t forget that set elements must be immutable. For example, a tuple may be included in a set:
x = {42, 'foo', (1, 2, 3), 3.14159}
print(x)

# The len() function returns the number of elements in a set, and the in and not in operators can be used to test for
# membership:

x = {'foo', 'bar', 'baz'}

print(len(x))
print('bar' in x)
print('qux' in x)

## Operating on a Set

# Given two sets, x1 and x2, the union of x1 and x2 is a set consisting of all elements in either set.

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1 | x2)

# Set union can also be obtained with the .union() method. The method is invoked on one of the sets, and the other is
# passed as an argument:

print(x1.union(x2))

# The way they are used in the examples above, the operator and method behave identically. But there is a subtle
# difference between them. When you use the | operator, both operands must be sets. The .union() method, on the other
# hand, will take any iterable as an argument, convert it to a set, and then perform the union.

y = x1.union(('baz', 'qux', 'quux'))

print(y)

# Below is a list of the set operations available in Python. Some are performed by operator, some by method,
# and some by both. The principle outlined above generally applies: where a set is expected, methods will typically
# accept any iterable as an argument, but operators require actual sets as operands.

# x1.intersection(x2[, x3 ...])

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1.intersection(x2))
print(x1 & x2)

# x1.difference(x2[, x3 ...])

print(x1.difference(x2))
print(x1 - x2)

# Modifying a Set

# Although the elements contained in a set must be of immutable type, sets themselves can be modified. Like the
# operations above, there are a mix of operators and methods that can be used to change the contents of a set.

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 |= x2

print(x1)

x1.update(['corge', 'garply'])

print(x1)

x = {'foo', 'bar', 'baz'}
x.add('qux')

print(x)