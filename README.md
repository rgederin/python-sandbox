# python-sandbox
Sandbox repo for playing with python

# Table of content

# Core data types in Python

There are 6 data types in Python and they are:

1. Numbers (Numeric)
2. Strings
3. Lists
4. Dictionaries
5. Tuples
6. Sets

![data](https://github.com/rgederin/python-sandbox/blob/master/img/types.jpeg)


There is one more data type called Range — but that is mainly used when we are iterating through values such as in for loops.


## Numbers

In Python, numeric data type represent the data which has numeric value. Numeric value can be integer, floating number or even complex numbers. These values are defined as int, float and complex class in Python. 

* **Integers** – This value is represented by int class. It contains positive or negative whole numbers (without fraction or decimal). In Python there is no limit to how long an integer value can be.
* **Float** – This value is represented by float class. It is a real number with floating point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation. 
* **Complex Numbers** – Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j. For example – 2+3j 

```
# Python program to
# demonstrate numeric value
 
a = 5
print("Type of a: ", type(a))
 
b = 5.0
print("\nType of b: ", type(b))
 
c = 2 + 4j
print("\nType of c: ", type(c))
```

Output:

```
Type of a:  <class 'int'>

Type of b:  <class 'float'>

Type of c:  <class 'complex'>
```

## Boolean

Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false). But non-Boolean objects can be evaluated in Boolean context as well and determined to be true or false. It is denoted by the class bool.

Note – True and False with capital ‘T’ and ‘F’ are valid booleans otherwise python will throw an error.

```
x = 1
y = 2
num = x < y
type(num)
# will output <class 'bool'>
```

## Lists

A list is an array that is **mutable** and **ordered**, with **duplicates allowed**. This means that it has indexes, just like Strings. You can declare different data types inside a list. 

### Creating List

Lists in Python can be created by just placing the sequence inside the square brackets[]. 

```
# Python program to demonstrate 
# Creation of List 
   
# Creating a List
List = []
print("Initial blank List: ")
print(List)
   
# Creating a List with 
# the use of a String
List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)
   
# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0]) 
print(List[2])
   
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)
```

Output:

```
Initial blank List: 
[]

List with the use of String: 
['GeeksForGeeks']

List containing multiple values: 
Geeks
Geeks

Multi-Dimensional List: 
[['Geeks', 'For'], ['Geeks']]
```

### Adding Elements to a List

**Using append() method**

Elements can be added to the List by using built-in append() function. Only one element at a time can be added to the list by using append() method, for addition of multiple elements with the append() method, loops are used. Tuples can also be added to the List with the use of append method because tuples are immutable. Unlike Sets, Lists can also be added to the existing list with the use of append() method.

```
# Creating a List
List = []
print("Initial blank List: ")
print(List) # []
  
# Addition of Elements 
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List) # [1, 2, 4]
  
# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List) # [1, 2, 4, 1, 2, 3]
  
# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List) # [1, 2, 4, 1, 2, 3, (5, 6)]
  
# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List) # [1, 2, 4, 1, 2, 3, (5, 6), ['For', 'Geeks']]
```

**Using insert() method**

append() method only works for addition of elements at the end of the List, for addition of element at the desired position, insert() method is used. Unlike append() which takes only one argument, insert() method requires two arguments(position, value).

```
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List) # [1, 2, 3, 4]
  
# Addition of Element at 
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List) # ['Geeks', 1, 2, 3, 12, 4]
```

**Using extend() method**

Other than append() and insert() methods, there’s one more method for Addition of elements, extend(), this method is used to add multiple elements at the same time at the end of the list.

Note – append() and extend() methods can only add elements at the end.

```
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List) # [1, 2, 3, 4]
  
# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List) # [1, 2, 3, 4, 8, 'Geeks', 'Always']
```