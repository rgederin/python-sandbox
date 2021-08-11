##### Creating dictationary #####

# define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces
phone_book = {
    "Ruslan": "452629",
    "Dima": "43224",
    "Anna": "5325345634"
}

print(phone_book)
print(type(phone_book))

# construct a dictionary with the built-in dict() function.  The argument to dict() should be a sequence of key-value
# pairs. A list of tuples works well for this:
phone_book = dict([
    ("Ruslan", "452629"),
    ("Dima", "43224"),
    ("Anna", "5325345634")
])

print(phone_book)
print(type(phone_book))

# If the key values are simple strings, they can be specified as keyword arguments
phone_book = dict(
    Ruslan="452629",
    Dima="43224",
    Anna="5325345634"
)

print(phone_book)
print(type(phone_book))

##### Accessing Dictionary Values #####

# A value is retrieved from a dictionary by specifying its corresponding key in square brackets ([]):
# If you refer to a key that is not in the dictionary, Python raises an exception
print(phone_book['Ruslan'])

# Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:
phone_book["Aryna"] = "1111"
print(phone_book)

# If you want to update an entry, you can just assign a new value to an existing key
phone_book["Aryna"] = "2222"
print(phone_book)

# To delete an entry, use the del statement, specifying the key to delete:
del phone_book["Aryna"]
print(phone_book)

##### Building a Dictionary Incrementally #####

# You can start by creating an empty dictionary, which is specified by empty curly braces. Then you can add new keys and values one at a time:
person = {}
print(type(person))

person['fname'] = 'Ruslan'
person['lname'] = 'Gederin'
person['age'] = 30
person['wife'] = 'Anna'
person['children'] = []
person['pets'] = {'cat1': 'Baileys', 'cat2': 'Asty'}

print(person['fname'])
print(person['pets'])

# Retrieving the values in the sublist or subdictionary requires an additional index or key:
print(person['pets']['cat1'])

##### Operators and Built-in Functions #####

# the in and not in operators return True or False according to whether the specified operand occurs as a key in the
# dictionary

print("Ruslan" in phone_book)
print("Aryna" in phone_book)

# You can use the in operator together with short-circuit evaluation to avoid raising an error when trying to access
# a key that is not in the dictionary:

print("Aryna" in phone_book and phone_book["Aryna"])

# The len() function returns the number of key-value pairs in a dictionary:
print(len(phone_book))

##### Built-in Dictionary Methods #####

# d.clear() empties dictionary d of all key-value pairs:
person.clear()
print(person)

# d.get(<key>[, <default>])
print(person.get("fname"))
print(person.get("fname", "default"))

# d.items() - Returns a list of key-value pairs in a dictionary.
print(phone_book.items())

# d.keys() - Returns a list of keys in a dictionary
print(phone_book.keys())

# d.values() - Returns a list of values in a dictionary.
print(phone_book.values())

# d.pop(<key>[, <default>]) - Removes a key from a dictionary, if it is present, and returns its value.
print(phone_book.pop("Dima", "not found"))
print(phone_book)
print(phone_book.pop("Dima", "not found"))

# d.popitem() - emoves the last key-value pair added from d and returns it as a tuple.
print(phone_book.popitem())

# d.update(<obj>) - Merges a dictionary with another dictionary or with an iterable of key-value pairs.

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2)
print(d1)

d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update([('b', 200), ('d', 400)])

print(d1)