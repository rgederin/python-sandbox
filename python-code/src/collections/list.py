# Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets ([])
_list = ['foo', 'bar', 'baz', 'qux']

print(_list)

# Lists Are Ordered
a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']

print(a is b)

# Lists Can Contain Arbitrary Objects
a = [2, 4, 6, 8]
print(a)

a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(type(a))
print(a)

# List Elements Can Be Accessed by Index
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[0])
print(a[2])
print(a[5])

print(a[-1])
print(a[-2])
print(a[-5])

# Slicing also works. If a is a list, the expression a[m:n] returns the portion of a from index m to,
# but not including, index n
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[2:5])

# Both positive and negative indices can be specified:

print(a[-5:-2])
print(a[1:4])
print(a[-5:-2] == a[1:4])

# Several Python operators and built-in functions can also be used with lists in ways that are analogous to strings:

# The in and not in operators:

print(a)
print('qux' in a)
print('thud' not in a)

# The concatenation (+) and replication (*) operators

a = a + ['grault', 'garply']
print(a)

a = a * 2
print(a)

# The len(), min(), and max() functions:

print(len(a))
print(min(a))
print(max(a))

# Lists Can Be Nested

x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

print(x)

print('ddd' in x)
print('ddd' in x[1])
print('ddd' in x[1][1])

# Modifying a Single List Value

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)

a[2] = 10
a[-1] = 20

print(a)

# A list item can be deleted with the del command:
del a[3]

print(a)

# Modifying Multiple List Values
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]

print(a)

# Prepending or Appending Items to a List
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a += ['grault', 'garply']
print(a)

a = [10, 20] + a
print(a)

# Methods That Modify a List

# a.append(<obj>) - Appends an object to a list.
a = ['a', 'b']
a.append(123)

print(a)

a.append([1, 2, 3])
print(a)

# a.extend(<iterable>) - Extends a list with the objects from an iterable.
a = ['a', 'b']
a.extend([1, 2, 3])
print(a)

# a.insert(<index>, <obj>) - Inserts an object into a list.
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.insert(3, 3.14159)
print(a)

# a.remove(<obj>) - removes object <obj> from list a. If <obj> isn’t in a, an exception is raised:

a.remove('corge')
print(a)

# a.pop(index=-1) Removes an element from a list. a.pop() simply removes the last item in the list
print(a.pop())
print(a)
