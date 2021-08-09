# python-sandbox
Sandbox repo for playing with python

# Table of content

- [Python version management](#Python-Version-Management)
    * [Pyenv](#pyenv)
    * [Virtual environments and pyenv](#Virtual-environments-and-pyenv)
- [Python package management](#Python-package-management)
    * [Pip](#pip)
    * [Pipenv](#Pipenv)
    * [Poetry](#poetry)
    * [Conda](#conda)
    * [Highlevel comparison](#Highlevel-comparison)
- [Core data types in Python](#core-data-types-in-python)
    * [Numbers](#numbers)
    * [Boolean](#boolean)
    * [Strings](#strings)
    * [Lists](#lists)
    * [Tuple](#tuple)
    * [Set](#set)
    * [Dictionary](#dictionary)
- [Mutable vs Immutable Objects in Python](#mutable-vs-immutable-objects-in-python)
    * [ID and TYPE](#id-and-type)
    * [Mutable and Immutable Objects](#Mutable-and-Immutable-Objects)
    * [Strings](#strings)
    * [How objects are passed to functions](#How-objects-are-passed-to-functions)


# Python version management

macOS and most Unix operating systems come with a version of Python installed by default. This is often called the system Python. The system Python works just fine, but it’s usually out of date. As of this writing, macOS High Sierra still ships with Python 2.7.10 as the system Python.

It’s important that you leave the system Python as the default, because many parts of the system rely on the default Python being a specific version. This is one of many great reasons to customize your Python environment!

## Pyenv

Pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

**More about pyenv:** https://realpython.com/intro-to-pyenv/#why-use-pyenv

## Virtual environments and pyenv

Virtual environments are a big part of managing Python installations and applications. 

Virtual environments and pyenv are a match made in heaven. pyenv has a wonderful plugin called pyenv-virtualenv that makes working with multiple Python version and multiple virtual environments a breeze. If you’re wondering what the difference is between pyenv, pyenv-virtualenv, and tools like virtualenv or venv, then don’t worry. You’re not alone.

Here’s what you need to know:

* **pyenv** manages multiple versions of Python itself.
* **virtualenv/venv** manages virtual environments for a specific Python version.
* **pyenv-virtualenv** manages virtual environments for across varying versions of Python.

# Python package management

For many of the projects you work on, you’ll probably need some number of third-party packages. Those packages may have their own dependencies in turn. In the early days of Python, using packages involved manually downloading files and pointing Python at them. Today, we’re fortunate to have a variety of package management tools available to us.

Most package managers work in tandem with virtual environments, isolating the packages you install in one Python environment from another. Using the two together is where you really start to see the power of the tools available to you.

## Pip

Pip is a package manager for Python. That means it’s a tool that allows you to install and manage additional libraries and dependencies that are not distributed as part of the standard library.

Package management is so important that pip has been included with the Python installer since versions 3.4 for Python 3 and 2.7.9 for Python 2, and it’s used by many Python projects.

The concept of a package manager might be familiar to you if you are coming from other languages. JavaScript uses npm for package management, Ruby uses gem, and .NET use NuGet. In Python, pip has become the standard package manager.

**More about pip:** https://realpython.com/what-is-pip/#getting-started-with-pip

## Pipenv

Pipenv — the officially recommended Python packaging tool from Python.org, free (as in freedom).

Pipenv is a project that aims to bring the best of all packaging worlds to the Python world. It harnesses Pipfile, pip, and virtualenv into one single toolchain. It features very pretty terminal colors. Windows is a first–class citizen, in our world.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. The lock command generates a lockfile (Pipfile.lock).

**More about pipenv:** https://docs.pipenv.org/en/latest/

## Poetry

Poetry addresses additional facets of package management, including creating and publishing your own packages. Poetry comes with all the tools you might need to manage your projects in a deterministic way.

**More about poetry:** https://python-poetry.org/docs/

## Conda

With conda, you can use pip to install packages as usual, but you can also use conda install to install packages from different channels, which are collections of packages provided by Anaconda or other providers.

Anaconda is a full distribution of the software in the PyData ecosystem, including Python itself along with binaries for several third-party open-source projects. Besides Anaconda, there’s also Miniconda, which is a minimal Python distribution including basically Conda and its dependencies so that you can install only the packages you need, from scratch

Conda is a package, dependency, and environment management system that could be installed without the Anaconda or Miniconda distribution. It runs on Windows, macOS, and Linux and was created for Python programs, but it can package and distribute software for any language. The main purpose is to solve external dependencies issues in an easy way, by downloading pre-compiled versions of software

**More about conda:** https://docs.conda.io/en/latest/

## Highlevel comparison

https://ahmed-nafies.medium.com/pip-pipenv-poetry-or-conda-7d2398adbac9



























# Core data types in Python

There are 6 data types in Python and they are:

1. Numbers (Numeric)
2. Strings
3. Lists
4. Dictionaries
5. Tuples
6. Sets

![data](https://github.com/rgederin/python-sandbox/blob/master/img/types.jpeg)

![data](https://github.com/rgederin/python-sandbox/blob/master/img/dt.png)

![data](https://github.com/rgederin/python-sandbox/blob/master/img/dt2.jpeg)


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

## Strings

In Python, Strings are arrays of bytes representing Unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

### Creating a String

Strings in Python can be created using single quotes or double quotes or even triple quotes.

```
# Creating a String 
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)  # Welcome to the Geeks World
  
# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1) # I'm a Geek
  
# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
  
# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks
            For
            Life'''
print("\nCreating a multiline String: ")
print(String1) # Geeks
            For
            Life
```

### Accessing characters in Python

In Python, individual characters of a String can be accessed by using the method of Indexing. Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character and so on.

While accessing an index out of the range will cause an IndexError. Only Integers are allowed to be passed as an index, float or other types will cause a TypeError.

![data](https://github.com/rgederin/python-sandbox/blob/master/img/strings.jpeg)

```
String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1) # GeeksForGeeks
  
# Printing First character
print("\nFirst character of String is: ")
print(String1[0]) # G
  
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1]) # s
```

### String Slicing

To access a range of characters in the String, method of slicing is used. Slicing in a String is done by using a Slicing operator (colon).

```
# Creating a String
String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) # GeeksForGeeks
  
# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12]) # ksForGeek
  
# Printing characters between 
# 3rd and 2nd last character
print("\nSlicing characters between " +
    "3rd and 2nd last character: ")
print(String1[3:-2]) # ksForGee
```

### Deleting/Updating from a String

In Python, Updation or deletion of characters from a String is not allowed. This will cause an error because item assignment or item deletion from a String is not supported. Although deletion of entire String is possible with the use of a built-in del keyword. This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned. Only new strings can be reassigned to the same name.

Updation of a character:

```
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
  
# Updating a character 
# of the String
String1[2] = 'p'
print("\nUpdating character at 2nd Index: ")
print(String1)
```

Error:

```
Traceback (most recent call last):
File “/home/360bb1830c83a918fc78aa8979195653.py”, line 10, in
String1[2] = ‘p’
TypeError: ‘str’ object does not support item assignment
```

Updating Entire String:

```
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1) # Hello, I'm a Geek
  
# Updating a String
String1 = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String1) # Welcome to the Geek World
```

Deletion of a character:

```
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
  
# Deleting a character 
# of the String
del String1[2] 
print("\nDeleting character at 2nd Index: ")
print(String1)
```

Error:

```
Traceback (most recent call last):
File “/home/499e96a61e19944e7e45b7a6e1276742.py”, line 10, in
del String1[2]
TypeError: ‘str’ object doesn’t support item deletion
```

Deleting Entire String:

Deletion of entire string is possible with the use of del keyword. Further, if we try to print the string, this will produce an error because String is deleted and is unavailable to be printed.

```
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
  
# Deleting a String
# with the use of del
del String1 
print("\nDeleting entire String: ")
print(String1)
```

Error:

```
Traceback (most recent call last):
File “/home/e4b8f2170f140da99d2fe57d9d8c6a94.py”, line 12, in
print(String1)
NameError: name ‘String1’ is not define
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

### Accessing elements from the List

In order to access the list items refer to the index number.Use the index operator [ ] to access an item in a list.The index must be an integer.Nested list are accessed using nested indexing.

```
# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
  
# accessing a element from the 
# list using index number
print("Accessing a element from the list")
print(List[0])  # Geeks
print(List[2])  # Geeks
  
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'] , ['Geeks']]
  
# accessing an element from the 
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1]) # For
print(List[1][0]) # Geeks
```

**Negative indexing**

In Python, negative sequence indexes represent positions from the end of the array. Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3]. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.

```
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
  
# accessing a element using
# negative indexing
print("Accessing element using negative indexing")
  
# print the last element of list
print(List[-1]) # Geeks
  
# print the third last element of list 
print(List[-3]) # For
```

### Removing Elements from the List

**Using remove() method**

Elements can be removed from the List by using built-in remove() function but an Error arises if element doesn’t exist in the set. Remove() method only removes one element at a time, to remove range of elements, iterator is used. The remove() method removes the specified item.

Note – Remove method in List will only remove the first occurrence of the searched element.

```
# Creating a List
List = [1, 2, 3, 4, 5, 6, 
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

  
# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List) # [1, 2, 3, 4, 7, 8, 9, 10, 11, 12]
  
# Removing elements from List
# using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List) # [7, 8, 9, 10, 11, 12]
```

**Using pop() method**

Pop() function can also be used to remove and return an element from the set, but by default it removes only the last element of the set, to remove element from a specific position of the List, index of the element is passed as an argument to the pop() method.

```
List = [1,2,3,4,5]
  
# Removing element from the 
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List) # [1, 2, 3, 4]
  
# Removing element at a 
# specific location from the 
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List) # [1, 2, 4]
```

### Slicing of a List

In Python List, there are multiple ways to print the whole List with all the elements, but to print a specific range of elements from the list, we use Slice operation. Slice operation is performed on Lists with the use of a colon(:). To print elements from beginning to a range use [: Index], to print elements from end-use [:-Index], to print elements from specific Index till the end use [Index:], to print elements within a range, use [Start Index:End Index] and to print the whole List with the use of slicing operation, use [:]. Further, to print the whole List in reverse order, use [::-1].

Note – To print elements of List from rear end, use Negative Indexes.

![data](https://github.com/rgederin/python-sandbox/blob/master/img/slicing.jpeg)

```
# Creating a List
List = ['G','E','E','K','S','F',
        'O','R','G','E','E','K','S']
print("Initial List: ")
print(List)      # ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
  
# Print elements of a range
# using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)     # ['K', 'S', 'F', 'O', 'R']
  
# Print elements from a 
# pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List) # ['F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
  
# Printing elements from
# beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List) # ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
```

**Negative index List slicing**

```
# Creating a List
List = ['G','E','E','K','S','F',
        'O','R','G','E','E','K','S']
print("Initial List: ")
print(List) # ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
  
# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List) # ['G', 'E', 'E', 'K', 'S', 'F', 'O']
  
# Print elements of a range
# using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List) # ['R', 'G', 'E', 'E', 'K']
  
# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List) # ['S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G']
```

### List Comprehension

List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.

A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.

```
newList = [ expression(element) for element in oldList if condition ]
```

```
# below list contains square of all 
# odd numbers from range 1 to 10 
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print (odd_square) # [1, 9, 25, 49, 81]
```

For better understanding the above code is similar to –

```
odd_square = [] 
  
for x in range(1, 11): 
    if x % 2 == 1: 
        odd_square.append(x**2) 
  
print (odd_square) # [1, 9, 25, 49, 81]
```

### List performnce 

![data](https://github.com/rgederin/python-sandbox/blob/master/img/list-perf.png)

## Tuple

Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers. 

Values of a tuple are syntactically separated by ‘commas’. Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses. This helps in understanding the Python tuples more easily.

### Creating a Tuple

In Python, tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses for grouping the data sequence.
 

Note: Creation of Python tuple without the use of parentheses is known as Tuple Packing. 

```
#Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print (Tuple1) # ()
 
#Creating a Tuple
#with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1) # ('Geeks', 'For')
 
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1)) # (1, 2, 4, 5, 6)
 
#Creating a Tuple
#with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1) # ('G', 'e', 'e', 'k', 's')
```

### Creating a Tuple with Mixed Datatypes.

Tuples can contain any number of elements and of any datatype (like strings, integers, list, etc.). Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.

```
#Creating a Tuple
#with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1) # (5, 'Welcome', 7, 'Geeks')
 
#Creating a Tuple
#with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3) # ((0, 1, 2, 3), ('python', 'geek'))
 
#Creating a Tuple
#with repetition
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1) # ('Geeks', 'Geeks', 'Geeks')
 
#Creating a Tuple
#with the use of loop
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1) # ('Geeks',)
                    (('Geeks',),)
                    ((('Geeks',),),)
                    (((('Geeks',),),),)
                    ((((('Geeks',),),),),)
```

### Accessing of Tuples

Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed via unpacking or indexing (or even by attribute in the case of named tuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
 

Note: In unpacking of tuple number of variables on the left-hand side should be equal to a number of values in given tuple a.

```
#Accessing Tuple
#with Indexing
Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[1]) # e
 
 
#Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")
 
#This line unpack
#values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a) # Geeks
print(b) # For
print(c) # Geeks
```

### Concatenation of Tuples

Concatenation of tuple is the process of joining two or more Tuples. Concatenation is done by the use of ‘+’ operator. Concatenation of tuples is done always from the end of the original tuple. Other arithmetic operations do not apply on Tuples. 

Note- Only the same datatypes can be combined with concatenation, an error arises if a list and a tuple are combined. 

```
# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')
 
Tuple3 = Tuple1 + Tuple2
 
# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)
 
# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)
 
# Printing Final Tuple
print("\nTuples after Concatenation: ")
print(Tuple3)
```

![data](https://github.com/rgederin/python-sandbox/blob/master/img/t1.jpeg)

### Slicing of Tuple

Slicing of a Tuple is done to fetch a specific range or slice of sub-elements from a Tuple. Slicing can also be done to lists and arrays. Indexing in a list results to fetching a single element whereas Slicing allows to fetch a set of elements. 
Note- Negative Increment values can also be used to reverse the sequence of Tuple

```
# Slicing of a Tuple
 
# Slicing of a Tuple
# with Numbers
Tuple1 = tuple('GEEKSFORGEEKS')
 
# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:]) # ('E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S')
 
# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ") # ('S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G')
print(Tuple1[::-1])
 
# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9]) # ('S', 'F', 'O', 'R', 'G')
```

![data](https://github.com/rgederin/python-sandbox/blob/master/img/t2.jpeg)

### Deleting a Tuple

Tuples are immutable and hence they do not allow deletion of a part of it. The entire tuple gets deleted by the use of del() method. 
 
Note- Printing of Tuple after deletion results in an Error.

## Set

In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.

The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.

### Creating a Set
Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by ‘comma’.

Note – A set cannot have mutable elements like a list, set or dictionary, as its elements. 

```
# Python program to demonstrate
# Creation of Set in Python
 
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
 
# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)
 
# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)
 
# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)
```

A set contains only unique elements but at the time of set creation, multiple duplicate values can also be passed. Order of elements in a set is undefined and is unchangeable. Type of elements in a set need not be the same, various mixed up data type values can also be passed to the set. 

```
# Creating a Set with
# a List of Numbers
# (Having duplicate values)
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)
 
# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)
```

### Adding Elements to a Set

Using add() method

Elements can be added to the Set by using built-in add() function. Only one element at a time can be added to the set by using add() method, loops are used to add multiple elements at a time with the use of add() method.

Note – Lists cannot be added to a set as elements because Lists are not hashable whereas Tuples can be added because tuples are immutable and hence Hashable. 

```
# Python program to demonstrate
# Addition of elements in a Set
 
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
 
# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6,7))
print("\nSet after Addition of Three elements: ")
print(set1)
 
# Adding elements to the Set
# using Iterator
for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)
```

Using update() method

For addition of two or more elements Update() method is used. The update() method accepts lists, strings, tuples as well as other sets as its arguments. In all of these cases, duplicate elements are avoided.

```

# Python program to demonstrate
# Addition of elements in a Set
 
# Addition of elements to the Set
# using Update function
set1 = set([ 4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)
```

### Accessing a Set

Set items cannot be accessed by referring to an index, since sets are unordered the items has no index. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

```
# Python program to demonstrate
# Accessing of elements in a set
   
# Creating a set
set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)
   
# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
    print(i, end =" ")
   
# Checking the element
# using in keyword
print("Geeks" in set1)
```

## Dictionary

Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’.
 

### Creating Dictionary

In Python, a Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’. Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable. Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing it to curly braces{}.
Note – Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.

```
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
   
# Creating a Dictionary 
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
   
# Creating a Dictionary 
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
   
# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
   
# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)
```

### Accessing elements of Dictionary

In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets. There is also a method called get() that will also help in accessing the element from a dictionary.

```
# Python program to demonstrate  
# accessing a element from a Dictionary 
   
# Creating a Dictionary 
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
   
# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])
 
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))
```


# Mutable vs Immutable Objects in Python

Everything in Python is an object. And what every newcomer to Python should quickly learn is that all objects in Python can be either mutable or immutable.

Lets dive deeper into the details of it… Since everything in Python is an Object, every variable holds an object instance. When an object is initiated, it is assigned a unique object id. Its type is defined at runtime and once set can never change, however its state can be changed if it is mutable. Simple put, a mutable object can be changed after it is created, and an immutable object can’t.

Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable. Objects of built-in types like (list, set, dict) are mutable. Custom classes are generally mutable. To simulate immutability in a class, one should override attribute setting and deletion to raise exceptions.

![data](https://github.com/rgederin/python-sandbox/blob/master/img/im.png)

Now comes the question, how do we find out if our variable is a mutable or immutable object. For this we should understand what ‘ID’ and ‘TYPE’ functions are for.

## ID and TYPE

The built-in function id() returns the identity of an object as an integer. This integer usually corresponds to the object’s location in memory, although this is specific to the Python implementation and the platform being used. The is operator compares the identity of two objects.

The built-in function type() returns the type of an object. Lets look at a simple example:

```
''' Example 1 '''
>>> x = "Holberton"
>>> y = "Holberton"
>>> id(x)
140135852055856
>>> id(y)
140135852055856
>>> print(x is y) '''comparing the types'''
True
''' Example 2 '''
>>> a = 50
>>> type(a)
<class: ‘int’>
>>> b = "Holberton"
>>> type(b)
<class: 'string'>
```

We have now seen how to compare two simple string variables to find out the types and id’s .So using these two functions, we can check to see how different types of objects are associated with variables and how objects can be changed.

## Mutable and Immutable Objects
So as we discussed earlier, a mutable object can change its state or contents and immutable objects cannot.

Mutable objects:

`list, dict, set, byte array`

Immutable objects:

`int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes`

A practical example to find out the mutability of object types

```
x = 10
x = y
```

We are creating an object of type int. identifiers x and y points to the same object.

```
id(x) == id(y)
id(y) == id(10)
```

if we do a simple operation.

```
x = x + 1
```

Now

```
id(x) != id(y)
id(x) != id(10)
```

The object in which x was tagged is changed. object 10 was never modified. Immutable objects doesn’t allow modification after creation.

In the case of mutable objects

```
m = list([1, 2, 3])
n = m
```

We are creating an object of type list. identifiers m and m tagged to the same list object, which is a collection of 3 immutable int objects.

```
id(m) == id(n)
```

Now poping an item from list object does change the object,

```
m.pop()
object id will not be changed
id(m) == id(n)
```

m and n will be pointing to the same list object after the modification. The list object will now contain [1, 2].

So what have we seen so far from the above examples?

* Python handles mutable and immutable objects differently.
* Immutable are quicker to access than mutable objects.
* Mutable objects are great to use when you need to change the size of the object, example list, dict etc.. Immutables are used when you need to ensure that the object you made will always stay the same.
* Immutable objects are fundamentally expensive to “change”, because doing so involves creating a copy. Changing mutable objects is cheap.

## Exceptions in immutability

Not all of the immutable objects are actually immutable. Confused? Let me explain.
As discussed earlier, Python containers liked tuples are immutable. That means value of a tuple can't be changed after it is created. But the "value" of a tuple is infact a sequence of names with unchangeable bindings to objects. The key thing to note is that the bindings are unchangeable, not the objects they are bound to.

Let us consider a tuple t = (‘holberton’, [1, 2, 3])

The above tuple t contains elements of different data types, the first one is an immutable string and the second one is a mutable list.The tuple itself isn’t mutable . i.e. it doesn’t have any methods for changing its contents. Likewise, the string is immutable because strings don’t have any mutating methods. But the list object does have mutating methods, so it can be changed. This is a subtle point, but nonetheless important: the “value” of an immutable object can’t change, but it’s constituent objects can.

## How objects are passed to functions

Its important for us to know difference between mutable and immutable types and how they are treated when passed onto functions. Memory efficiency is highly affected when the proper objects are used.

For example if a mutable object is called by reference in a function, it can change the original variable itself. Hence to avoid this, the original variable needs to be copied to another variable. Immutable objects can be called by reference because its value cannot be changed anyways.

```
def updateList(list1):
    list1 += [10]
n = [5, 6]

print(id(n))                  # 140312184155336
updateList(n)

print(n)                      # [5, 6, 10]
print(id(n))                  # 140312184155336
```

As we can see from the above example, we have called the list via call by reference, so the changes are made to the original list itself.

Lets take a look at another example:

```
def updateNumber(n):
    print(id(n))
    n += 10
b = 5
print(id(b))                   # 10055680
updateNumber(b)                # 10055680
print(b)                       # 5
```

In the above example the same object is passed to the function, but the variables value doesn’t change even though the object is identical. This is called pass by value. So what is exactly happening here? When the value is called by the function, only the value of the variable is passed, not the object itself. So the variable referencing the object is not changed, but the object itself is being changed but within the function scope only. Hence the change is not reflected.

https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/