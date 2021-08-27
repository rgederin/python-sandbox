# python-sandbox
Sandbox repo for playing with python

# Table of content

- [Python version management](#Python-Version-Management)
    * [Pyenv](#pyenv)
    * [Virtual environments and pyenv](#Virtual-environments-and-pyenv)
- [Python virtual environments](#Python-Virtual-Environments)
- [Python package management](#Python-package-management)
    * [Pip](#pip)
    * [Pipenv](#Pipenv)
    * [Poetry](#poetry)
    * [Conda](#conda)
    * [Highlevel comparison](#Highlevel-comparison)
- [Python data structures](#Python-data-structures)
    * [Array data structures](#Array-data-structures)
    * [Arrays](#arrays) 
    * [Arrays summary](#arrays-summary)
    * [List](#list)
    * [Linked Lists](#linked-lists)
    * [Tuple](#tuple)
    * [Dictionaries](#Dictionaries)
    * [Sets](#sets)
    * [Stacks (LIFO)](#Stacks-(LIFO))
    * [Queues (FIFO)](#Queues-(FIFO))
    * [Priority Queues](#Priority-Queues)
- [Python Modules and Packages](#Python-Modules-and-Packages)
    * [Modules](#Modules)
    * [Packages](#Packages)
- [OOP in Python](#OOP-in-Python)
    * [Basics](#basics
    )
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


# Python virtual environments

At its core, the main purpose of Python virtual environments is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has.

The great thing about this is that there are no limits to the number of environments you can have since they’re just directories containing a few scripts. Plus, they’re easily created using the virtualenv or pyenv command line tools.

**More about virtual environments:** https://realpython.com/python-virtual-environments-a-primer/


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


# Python data structures

Data structures are the fundamental constructs around which you build your programs. Each data structure provides a particular way of organizing data so it can be accessed efficiently, depending on your use case. Python ships with an extensive set of data structures in its standard library.

## Array data structures

An array is a fundamental data structure available in most programming languages, and it has a wide range of uses across different algorithms.

Python includes several array-like data structures in its standard library that each have slightly different characteristics:

* list: Mutable Dynamic Arrays
* tuple: Immutable Containers
* array.array: Basic Typed Arrays
* str: Immutable Arrays of Unicode Characters
* bytes: Immutable Arrays of Single Bytes
* bytearray: Mutable Arrays of Single Bytes


## List

Lists are a part of the core Python language. Despite their name, Python’s lists are implemented as dynamic arrays behind the scenes. 

This means a list allows elements to be added or removed, and the list will automatically adjust the backing store that holds these elements by allocating or releasing memory.

Python lists can hold arbitrary elements—everything is an object in Python, including functions. Therefore, you can mix and match different kinds of data types and store them all in a single list.

The important characteristics of Python lists are as follows:

* Lists are ordered.
* Lists can contain any arbitrary objects.
* List elements can be accessed by index.
* Lists can be nested to arbitrary depth.
* Lists are mutable.
* Lists are dynamic.

* **List code snippets:** https://github.com/rgederin/python-sandbox/blob/master/python-code/src/collections/list.py

![data](https://github.com/rgederin/python-sandbox/blob/master/img/pl.jpeg)

![data](https://github.com/rgederin/python-sandbox/blob/master/img/pl.png)


## Linked Lists

Linked lists are an ordered collection of objects. So what makes them different from normal lists? Linked lists differ from lists in the way that they store elements in memory. While lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements.

https://realpython.com/linked-lists-python/#understanding-linked-lists


## Tuple

Just like lists, tuples are part of the Python core language. Unlike lists, however, Python’s tuple objects are immutable. This means elements can’t be added or removed dynamically—all elements in a tuple must be defined at creation time.

Everything you’ve learned about lists—they are ordered, they can contain arbitrary objects, they can be indexed and sliced, they can be nested—is true of tuples as well. But they can’t be modified.

**Tuple has the following characteristics**

* Ordered: Tuples are part of sequence data types, which means they hold the order of the data insertion. It maintains the index value for each item.
* Unchangeable: Tuples are unchangeable, which means that we cannot add or delete items to the tuple after creation.
* Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) and can be accessed through indexing and slicing.
* Contains Duplicates: Tuples can contain duplicates, which means they can have items with the same value.

**Why use a tuple instead of a list?**

* Program execution is faster when manipulating a tuple than it is for the equivalent list. (This is probably not going to be noticeable when the list or tuple is small.)

* Sometimes you don’t want data to be modified. If the values in the collection are meant to remain constant for the life of the program, using a tuple instead of a list guards against accidental modification.

* There is another Python data type that you will encounter shortly called a dictionary, which requires as one of its components a value that is of an immutable type. A tuple can be used for this purpose, whereas a list can’t be.

![data](https://github.com/rgederin/python-sandbox/blob/master/img/tuple.jpeg)

* **Tuple code snippets:** https://github.com/rgederin/python-sandbox/blob/master/python-code/src/collections/tuple.py

## Arrays

### array.array: Basic Typed Arrays

Python’s array module provides space-efficient storage of basic C-style data types like bytes, 32-bit integers, floating-point numbers, and so on.

Arrays created with the array.array class are mutable and behave similarly to lists except for one important difference: they’re typed arrays constrained to a single data type.

Because of this constraint, array.array objects with many elements are more space efficient than lists and tuples. The elements stored in them are tightly packed, and this can be useful if you need to store many elements of the same type.

Also, arrays support many of the same methods as regular lists, and you might be able to use them as a drop-in replacement without requiring other changes to your application code.

```
>>> import array
>>> arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
>>> arr[1]
1.5
```

### str: Immutable Arrays of Unicode Characters

Python 3.x uses str objects to store textual data as immutable sequences of Unicode characters. Practically speaking, that means a str is an immutable array of characters. Oddly enough, it’s also a recursive data structure—each character in a string is itself a str object of length 1.

String objects are space efficient because they’re tightly packed and they specialize in a single data type. If you’re storing Unicode text, then you should use a string.

Because strings are immutable in Python, modifying a string requires creating a modified copy. 

### bytes: Immutable Arrays of Single Bytes

bytes objects are immutable sequences of single bytes, or integers in the range 0 ≤ x ≤ 255. Conceptually, bytes objects are similar to str objects, and you can also think of them as immutable arrays of bytes.

Like strings, bytes have their own literal syntax for creating objects and are space efficient. bytes objects are immutable, but unlike strings, there’s a dedicated mutable byte array data type called bytearray that they can be unpacked into.

### bytearray: Mutable Arrays of Single Bytes

The bytearray type is a mutable sequence of integers in the range 0 ≤ x ≤ 255. The bytearray object is closely related to the bytes object, with the main difference being that a bytearray can be modified freely—you can overwrite elements, remove existing elements, or add new ones. The bytearray object will grow and shrink accordingly.

A bytearray can be converted back into immutable bytes objects, but this involves copying the stored data in full—a slow operation taking O(n) time.

## Arrays summary: 

There are a number of built-in data structures you can choose from when it comes to implementing arrays in Python. In this section, you’ve focused on core language features and data structures included in the standard library.

If you’re willing to go beyond the Python standard library, then third-party packages like NumPy and pandas offer a wide range of fast array implementations for scientific computing and data science.

* If you want to restrict yourself to the array data structures included with Python, then here are a few guidelines:
* If you need to store arbitrary objects, potentially with mixed data types, then use a list or a tuple, depending on whether or not you want an immutable data structure.
* If you have numeric (integer or floating-point) data and tight packing and performance is important, then try out array.array.
* If you have textual data represented as Unicode characters, then use Python’s built-in str. If you need a mutable string-like data structure, then use a list of characters.
* If you want to store a contiguous block of bytes, then use the immutable bytes type or a bytearray if you need a mutable data structure.

In most cases, I like to start out with a simple list. I’ll only specialize later on if performance or storage space becomes an issue. Most of the time, using a general-purpose array data structure like list gives you the fastest development speed and the most programming convenience.

I’ve found that this is usually much more important in the beginning than trying to squeeze out every last drop of performance right from the start.

## Dictionaries

In Python, dictionaries (or dicts for short) are a central data structure. Dicts store an arbitrary number of objects, each identified by a unique dictionary key. Dictionaries are also often called maps, hashmaps, lookup tables, or associative arrays. They allow for the efficient lookup, insertion, and deletion of any object associated with a given key.

Dictionaries are:

* Mutable.
* Dynamic. They can grow and shrink as needed.
* Can be nested.  A dictionary can contain another dictionary. A dictionary can also contain a list.
* Dictionary elements are accessed via keys.

Python features a robust dictionary implementation that’s built directly into the core language: the **dict** data type.

* **More about dict data type:** https://realpython.com/python-dicts/#
* **Dictionaries code snippets:** https://github.com/rgederin/python-sandbox/blob/master/python-code/src/collections/list.py

Python’s dictionaries are indexed by keys that can be of any hashable type. A hashable object has a hash value that never changes during its lifetime (see __hash__), and it can be compared to other objects (see __eq__). Hashable objects that compare as equal must have the same hash value.

Immutable types like strings and numbers are hashable and work well as dictionary keys. You can also use tuple objects as dictionary keys as long as they contain only hashable types themselves.

![data](https://github.com/rgederin/python-sandbox/blob/master/img/dp.jpeg)

Besides plain **dict** objects, Python’s standard library also includes a number of specialized dictionary implementations. These specialized dictionaries are all based on the built-in dictionary class (and share its performance characteristics) but also include some additional convenience features:

* **collections.OrderedDict**: Remember the Insertion Order of Keys (https://realpython.com/python-ordereddict/)
* **collections.defaultdict**: Return Default Values for Missing Keys (https://docs.python.org/3/library/collections.html#collections.defaultdict)
* **collections.ChainMap**: Search Multiple Dictionaries as a Single Mapping (https://docs.python.org/3/library/collections.html#collections.ChainMap)
* **types.MappingProxyType**: A Wrapper for Making Read-Only Dictionaries (https://docs.python.org/3/library/types.html#types.MappingProxyType)

## Sets

A set is an unordered collection of objects that doesn’t allow duplicate elements. Typically, sets are used to quickly test a value for membership in the set, to insert or delete new values from a set, and to compute the union or intersection of two sets.

In a proper set implementation, membership tests are expected to run in fast O(1) time. Union, intersection, difference, and subset operations should take O(n) time on average. The set implementations included in Python’s standard library follow these performance characteristics.


### set: Your Go-To Set

The set type is the built-in set implementation in Python. It’s mutable and allows for the dynamic insertion and deletion of elements.

Python’s sets are backed by the dict data type and share the same performance characteristics. Any hashable object can be stored in a set.

Python’s built-in set type has the following characteristics:

* Sets are unordered.
* Set elements are unique. Duplicate elements are not allowed.
* A set itself may be modified, but the elements contained in the set must be of an immutable type.

![data](https://github.com/rgederin/python-sandbox/blob/master/img/sets.jpeg)

**More about set data type:** https://realpython.com/python-sets/

### frozenset: Immutable Sets

The frozenset class implements an immutable version of set that can’t be changed after it’s been constructed.

**More about frozenset data type:** https://realpython.com/python-sets/#frozen-sets 

### collections.Counter: Multisets

The collections.Counter class in the Python standard library implements a multiset, or bag, type that allows elements in the set to have more than one occurrence.

This is useful if you need to keep track of not only if an element is part of a set, but also how many times it’s included in the set.

**More about collections.Counter data type:** https://docs.python.org/3/library/collections.html#collections.Counter

### Sets and Multisets in Python: Summary

Sets are another useful and commonly used data structure included with Python and its standard library. Here are a few guidelines for deciding which one to use:

* If you need a mutable set, then use the built-in set type.
* If you need hashable objects that can be used as dictionary or set keys, then use a frozenset.
* If you need a multiset, or bag, data structure, then use collections.Counter.

## Stacks (LIFO)

A stack is a collection of objects that supports fast Last-In/First-Out (LIFO) semantics for inserts and deletes. Unlike lists or arrays, stacks typically don’t allow for random access to the objects they contain. The insert and delete operations are also often called push and pop.

Python ships with several stack implementations that each have slightly different characteristics. Let’s take a look at them and compare their characteristics.

**More about stack data types:** https://realpython.com/how-to-implement-python-stack/ 

### list: Simple, Built-In Stacks
Python’s built-in list type makes a decent stack data structure as it supports push and pop operations in amortized O(1) time.

https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks

Python’s lists are implemented as dynamic arrays internally, which means they occasionally need to resize the storage space for elements stored in them when elements are added or removed. The list over-allocates its backing storage so that not every push or pop requires resizing. As a result, you get an amortized O(1) time complexity for these operations.

The downside is that this makes their performance less consistent than the stable O(1) inserts and deletes provided by a linked list–based implementation (as you’ll see below with collections.deque). On the other hand, lists do provide fast O(1) time random access to elements on the stack, and this can be an added benefit.

There’s an important performance caveat that you should be aware of when using lists as stacks: To get the amortized O(1) performance for inserts and deletes, new items must be added to the end of the list with the append() method and removed again from the end using pop(). For optimum performance, stacks based on Python lists should grow towards higher indexes and shrink towards lower ones.

Adding and removing from the front is much slower and takes O(n) time, as the existing elements must be shifted around to make room for the new element. This is a performance antipattern that you should avoid as much as possible

```
>>> s = []
>>> s.append("eat")
>>> s.append("sleep")
>>> s.append("code")

>>> s
['eat', 'sleep', 'code']

>>> s.pop()
'code'
>>> s.pop()
'sleep'
>>> s.pop()
'eat'

>>> s.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
```

### collections.deque: Fast and Robust Stacks

The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time (non-amortized). Because deques support adding and removing elements from either end equally well, they can serve both as queues and as stacks.

Python’s deque objects are implemented as doubly-linked lists, which gives them excellent and consistent performance for inserting and deleting elements but poor O(n) performance for randomly accessing elements in the middle of a stack.

Overall, collections.deque is a great choice if you’re looking for a stack data structure in Python’s standard library that has the performance characteristics of a linked-list implementation.

```
from collections import deque
>>> s = deque()
>>> s.append("eat")
>>> s.append("sleep")
>>> s.append("code")

>>> s
deque(['eat', 'sleep', 'code'])

>>> s.pop()
'code'
>>> s.pop()
'sleep'
>>> s.pop()
'eat'

>>> s.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from an empty deque
```

### queue.LifoQueue: Locking Semantics for Parallel Computing

The LifoQueue stack implementation in the Python standard library is synchronized and provides locking semantics to support multiple concurrent producers and consumers.

Besides LifoQueue, the queue module contains several other classes that implement multi-producer, multi-consumer queues that are useful for parallel computing.

Depending on your use case, the locking semantics might be helpful, or they might just incur unneeded overhead. In this case, you’d be better off using a list or a deque as a general-purpose stack.

### Stack Implementations in Python: Summary

As you’ve seen, Python ships with several implementations for a stack data structure. All of them have slightly different characteristics as well as performance and usage trade-offs.

If you’re not looking for parallel processing support (or if you don’t want to handle locking and unlocking manually), then your choice comes down to the built-in list type or collections.deque. The difference lies in the data structure used behind the scenes and overall ease of use.

list is backed by a dynamic array, which makes it great for fast random access but requires occasional resizing when elements are added or removed.

The list over-allocates its backing storage so that not every push or pop requires resizing, and you get an amortized O(1) time complexity for these operations. But you do need to be careful to only insert and remove items using append() and pop(). Otherwise, performance slows down to O(n).

collections.deque is backed by a doubly-linked list, which optimizes appends and deletes at both ends and provides consistent O(1) performance for these operations. Not only is its performance more stable, the deque class is also easier to use because you don’t have to worry about adding or removing items from the wrong end.

In summary, collections.deque is an excellent choice for implementing a stack (LIFO queue) in Python.


## Queues (FIFO)

A queue is a collection of objects that supports fast FIFO semantics for inserts and deletes. The insert and delete operations are sometimes called enqueue and dequeue. Unlike lists or arrays, queues typically don’t allow for random access to the objects they contain.

With a queue, you remove the item least recently added (FIFO) but with a stack, you remove the item most recently added (LIFO).

Performance-wise, a proper queue implementation is expected to take O(1) time for insert and delete operations. These are the two main operations performed on a queue, and in a correct implementation, they should be fast.

Python ships with several queue implementations that each have slightly different characteristics. Let’s review them.

### list: Terribly Sloooow Queues

It’s possible to use a regular list as a queue, but this is not ideal from a performance perspective. Lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all the other elements by one, requiring O(n) time.

https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues

### collections.deque: Fast and Robust Queues

The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time (non-amortized). Because deques support adding and removing elements from either end equally well, they can serve both as queues and as stacks.

Python’s deque objects are implemented as doubly-linked lists. This gives them excellent and consistent performance for inserting and deleting elements, but poor O(n) performance for randomly accessing elements in the middle of the stack.

As a result, collections.deque is a great default choice if you’re looking for a queue data structure in Python’s standard library.

```
>>> from collections import deque
>>> q = deque()
>>> q.append("eat")
>>> q.append("sleep")
>>> q.append("code")

>>> q
deque(['eat', 'sleep', 'code'])

>>> q.popleft()
'eat'
>>> q.popleft()
'sleep'
>>> q.popleft()
'code'

>>> q.popleft()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from an empty deque
```

### queue.Queue: Locking Semantics for Parallel Computing

The queue.Queue implementation in the Python standard library is synchronized and provides locking semantics to support multiple concurrent producers and consumers.

The queue module contains several other classes implementing multi-producer, multi-consumer queues that are useful for parallel computing.

Depending on your use case, the locking semantics might be helpful or just incur unneeded overhead. In this case, you’d be better off using collections.deque as a general-purpose queue.

### multiprocessing.Queue: Shared Job Queues

multiprocessing.Queue is a shared job queue implementation that allows queued items to be processed in parallel by multiple concurrent workers. Process-based parallelization is popular in CPython due to the global interpreter lock (GIL) that prevents some forms of parallel execution on a single interpreter process.

As a specialized queue implementation meant for sharing data between processes, multiprocessing.Queue makes it easy to distribute work across multiple processes in order to work around the GIL limitations. This type of queue can store and transfer any pickleable object across process boundaries.

### Queues in Python: Summary

Python includes several queue implementations as part of the core language and its standard library.

list objects can be used as queues, but this is generally not recommended due to slow performance.

If you’re not looking for parallel processing support, then the implementation offered by collections.deque is an excellent default choice for implementing a FIFO queue data structure in Python. It provides the performance characteristics you’d expect from a good queue implementation and can also be used as a stack (LIFO queue).

## Priority Queues

A priority queue is a container data structure that manages a set of records with totally-ordered keys to provide quick access to the record with the smallest or largest key in the set.

You can think of a priority queue as a modified queue. Instead of retrieving the next element by insertion time, it retrieves the highest-priority element. The priority of individual elements is decided by the order applied to their keys.

Priority queues are commonly used for dealing with scheduling problems. For example, you might use them to give precedence to tasks with higher urgency.

### list: Manually Sorted Queues

You can use a sorted list to quickly identify and delete the smallest or largest element. The downside is that inserting new elements into a list is a slow O(n) operation.

While the insertion point can be found in O(log n) time using bisect.insort in the standard library, this is always dominated by the slow insertion step.

Maintaining the order by appending to the list and re-sorting also takes at least O(n log n) time. Another downside is that you must manually take care of re-sorting the list when new elements are inserted. It’s easy to introduce bugs by missing this step, and the burden is always on you, the developer.

This means sorted lists are only suitable as priority queues when there will be few insertions.

### heapq: List-Based Binary Heaps

heapq is a binary heap implementation usually backed by a plain list, and it supports insertion and extraction of the smallest element in O(log n) time.

This module is a good choice for implementing priority queues in Python. Since heapq technically provides only a min-heap implementation, extra steps must be taken to ensure sort stability and other features typically expected from a practical priority queue

### queue.PriorityQueue: Beautiful Priority Queues

queue.PriorityQueue uses heapq internally and shares the same time and space complexities. The difference is that PriorityQueue is synchronized and provides locking semantics to support multiple concurrent producers and consumers.

Depending on your use case, this might be helpful, or it might just slow your program down slightly. In any case, you might prefer the class-based interface provided by PriorityQueue over the function-based interface provided by heapq:

```
>>> from queue import PriorityQueue
>>> q = PriorityQueue()
>>> q.put((2, "code"))
>>> q.put((1, "eat"))
>>> q.put((3, "sleep"))

>>> while not q.empty():
...     next_item = q.get()
...     print(next_item)
...
(1, 'eat')
(2, 'code')
(3, 'sleep')
```

### Priority Queues in Python: Summary

Python includes several priority queue implementations ready for you to use.

queue.PriorityQueue stands out from the pack with a nice object-oriented interface and a name that clearly states its intent. It should be your preferred choice.

If you’d like to avoid the locking overhead of queue.PriorityQueue, then using the heapq module directly is also a good option.


# Python Modules and Packages

This article explores Python modules and Python packages, two mechanisms that facilitate modular programming.

Modular programming refers to the process of breaking a large, unwieldy programming task into separate, smaller, more manageable subtasks or modules. Individual modules can then be cobbled together like building blocks to create a larger application.

There are several advantages to modularizing code in a large application:

* **Simplicity:** Rather than focusing on the entire problem at hand, a module typically focuses on one relatively small portion of the problem. If you’re working on a single module, you’ll have a smaller problem domain to wrap your head around. This makes development easier and less error-prone.

* **Maintainability:** Modules are typically designed so that they enforce logical boundaries between different problem domains. If modules are written in a way that minimizes interdependency, there is decreased likelihood that modifications to a single module will have an impact on other parts of the program. (You may even be able to make changes to a module without having any knowledge of the application outside that module.) This makes it more viable for a team of many programmers to work collaboratively on a large application.

**Reusability:** Functionality defined in a single module can be easily reused (through an appropriately defined interface) by other parts of the application. This eliminates the need to duplicate code.

**Scoping:** Modules typically define a separate namespace, which helps avoid collisions between identifiers in different areas of a program. (One of the tenets in the Zen of Python is Namespaces are one honking great idea—let’s do more of those!)

Functions, modules and packages are all constructs in Python that promote code modularization.

## Modules

There are actually three different ways to define a module in Python:

* A module can be written in Python itself.
* A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
* A built-in module is intrinsically contained in the interpreter, like the itertools module.

A module’s contents are accessed the same way in all three cases: with the import statement.

math module:

```
def plus(a, b):
    print("sum two elements")
    return a + b


PI = 3.14

fib_numbers = (0, 1, 1, 2, 3, 5, 8, 13)
```

And simple usage:

```
import math
# import <module_name>[, <module_name> ...]

print(math)
print(math.PI)

res = math.plus(5, 6)
print(res)

print(math.fib_numbers)
```

**More about modules:** https://realpython.com/python-modules-packages/#python-modules-overview

## Packages

Suppose you have developed a very large application that includes many modules. As the number of modules grows, it becomes difficult to keep track of them all if they are dumped into one location. This is particularly so if they have similar names or functionality. You might wish for a means of grouping and organizing them.

Packages allow for a hierarchical structuring of the module namespace using dot notation. In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names.

Creating a package is quite straightforward, since it makes use of the operating system’s inherent hierarchical file structure. 

![data](https://github.com/rgederin/python-sandbox/blob/master/img/pkg.png)

**More about packages:** https://realpython.com/python-modules-packages/#python-packages


# OOP in Python

Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.

For instance, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.

Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees, students and teachers, and so on. OOP models real-world entities as software objects that have some data associated with them and can perform certain functions.

## Basics

Classes are used to create user-defined data structures. Classes define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.

A class is a blueprint for how something should be defined. It doesn’t actually contain any data. The Dog class specifies that a name and an age are necessary for defining a dog, but it doesn’t contain the name or age of any specific dog.

While the class is the blueprint, an instance is an object that is built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, like Miles, who’s four years old.

### Classes and objects

All class definitions start with the class keyword, which is followed by the name of the class and a colon. Any code that is indented below the class definition is considered part of the class’s body.

```
class Dog:
    # Class attribute
    voice = "bark bark"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # toString
    def __str__(self):
        return f"{self.name} is {self.age} years old dog"

    # instance method
    def speak(self):
        print(f"{self.name} says {self.voice}")


pluto = Dog("Pluto", 2)

print(pluto.age)
print(pluto.name)
print(pluto.voice)

# objects are mutable
pluto.age = 3
print(pluto.age)

pluto.speak()

print(pluto)
```

**More about classes:** https://realpython.com/python3-object-oriented-programming/#define-a-class-in-python


### Basic inheritance

Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that child classes are derived from are called parent classes.

```
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))

print(type(buddy))
print(isinstance(buddy, Dog))

print(miles.speak())
print(miles.speak("grrrrr"))
```

**More about basic inheritance:** https://realpython.com/python3-object-oriented-programming/#inherit-from-other-classes-in-python 
