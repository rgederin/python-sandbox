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
