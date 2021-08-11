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
    * [List](#list)
    * [Dictionaries](#Dictionaries)


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

**List code snippets:** https://github.com/rgederin/python-sandbox/blob/master/python_code/src/collections/dictionary_core.py

![data](https://github.com/rgederin/python-sandbox/blob/master/img/pl.jpeg)

![data](https://github.com/rgederin/python-sandbox/blob/master/img/pl.png)


## Dictionaries

In Python, dictionaries (or dicts for short) are a central data structure. Dicts store an arbitrary number of objects, each identified by a unique dictionary key. Dictionaries are also often called maps, hashmaps, lookup tables, or associative arrays. They allow for the efficient lookup, insertion, and deletion of any object associated with a given key.

Dictionaries are:

* Mutable.
* Dynamic. They can grow and shrink as needed.
* Can be nested.  A dictionary can contain another dictionary. A dictionary can also contain a list.
* Dictionary elements are accessed via keys.

Python features a robust dictionary implementation that’s built directly into the core language: the **dict** data type.

* **More about dict data type:** https://realpython.com/python-dicts/#
* **Code examples:** https://github.com/rgederin/python-sandbox/blob/master/python_code/src/dictionary_core.py

Python’s dictionaries are indexed by keys that can be of any hashable type. A hashable object has a hash value that never changes during its lifetime (see __hash__), and it can be compared to other objects (see __eq__). Hashable objects that compare as equal must have the same hash value.

Immutable types like strings and numbers are hashable and work well as dictionary keys. You can also use tuple objects as dictionary keys as long as they contain only hashable types themselves.

Besides plain **dict** objects, Python’s standard library also includes a number of specialized dictionary implementations. These specialized dictionaries are all based on the built-in dictionary class (and share its performance characteristics) but also include some additional convenience features:

* **collections.OrderedDict**: Remember the Insertion Order of Keys (https://realpython.com/python-ordereddict/)
* **collections.defaultdict**: Return Default Values for Missing Keys (https://docs.python.org/3/library/collections.html#collections.defaultdict)
* **collections.ChainMap**: Search Multiple Dictionaries as a Single Mapping (https://docs.python.org/3/library/collections.html#collections.ChainMap)
* **types.MappingProxyType**: A Wrapper for Making Read-Only Dictionaries (https://docs.python.org/3/library/types.html#types.MappingProxyType)