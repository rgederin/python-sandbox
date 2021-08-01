# python-sandbox
Sandbox repo for playing with python

# Table of content

- [Core data types in Python](#core-data-types-in-python)
    * [Numbers](#numbers)
    * [Boolean](#boolean)
    * [Strings](#stringss)
    * [Lists](#lists)

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


