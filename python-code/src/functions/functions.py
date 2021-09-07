def f():
    s = '-- Inside f()'
    print(s)


print('Before calling f()')
f()
print('After calling f()')


########### Argument Passing

# Positional Arguments The most straightforward way to pass arguments to a Python function is with positional
# arguments (also called required arguments). In the function definition, you specify a comma-separated list of
# parameters inside the parentheses

def f(quantity, item, price):
    print(f'{quantity} {item} cost ${price:.2f}')


f(6, 'bananas', 1.77)

# Positional args are order-dependent
f('bananas', 1.74, 6)

# Keyword Arguments Using keyword arguments lifts the restriction on argument order. Each keyword argument explicitly
# designates a specific parameter by name, so you can specify them in any order and Python will still know which
# argument goes with which parameter:

f(price=2.3, quantity=9, item='mango')

# You can call a function using both positional and keyword arguments
# When positional and keyword arguments are both present, all the positional arguments must come first

f(4, price=44, item='grape')


# Default (optional) parameters

def f(quantity, item, price=100):
    print(f'{quantity} {item} cost ${price:.2f}')


f(1, "vodka")

#### Argument Passing

# Argument passing in Python can be summarized as follows. Passing an immutable object, like an int, str, tuple,
# or frozenset, to a Python function acts like pass-by-value. The function can’t modify the object in the calling
# environment.

x = 10
print("x before function call = ", x)


def pass_by_value_function(x):
    x = x + 200
    print("x in function call = ", x)


pass_by_value_function(x)
print("x after function call = ", x)

# Passing a mutable object such as a list, dict, or set acts somewhat—but not exactly—like pass-by-reference. The
# function can’t reassign the object wholesale, but it can change items in place within the object, and these changes
# will be reflected in the calling environment.

l = [1, 2, 3]
print("l before function call = ", l)


def pass_by_ref_function(l):
    l.append([4, 5, 6])
    print("l in function call = ", l)


pass_by_ref_function(l)
print("l after function call = ", l)


def return_mult_values():
    return 1, 2, 'foo'


print(return_mult_values())


## Variable-Length Argument Lists

# Argument Tuple Packing

# When a parameter name in a Python function definition is preceded by an asterisk (*), it indicates argument tuple
# packing. Any corresponding arguments in the function call are packed into a tuple that the function can refer to by
# the given parameter name.

def f(*args):
    print(args)

    for arg in args:
        print(arg)


f(1, 'foo')


def avg(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)


print(avg(1, 5, 6))
print(avg(1, 2, 3, 4, 5))


# Argument Tuple Unpacking

# An analogous operation is available on the other side of the equation in a Python function call. When an argument
# in a function call is preceded by an asterisk (*), it indicates that the argument is a tuple that should be
# unpacked and passed to the function as separate values

def f(x, y, z):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')


f(1, 2, 3)

t = ('foo', 'bar', 'baz')
f(*t)


# Argument Dictionary Packing

# # Python has a similar operator, the double asterisk (**), which can be used with Python function parameters and
# arguments to specify dictionary packing and unpacking. Preceding a parameter in a Python function definition by a
# double asterisk (**) indicates that the corresponding arguments, which are expected to be key=value pairs,
# should be packed into a dictionary:


def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
        print(key, '->', val)


f(foo=1, bar=2, baz=3)


# Keyword-Only Arguments

def concat(*args):
    print(f'-> {".".join(args)}')


concat('a', 'b', 'c')


# problem with positional argument in this case
def concat(prefix='-> ', *args):
    print(f'{prefix}{".".join(args)}')


concat('a', 'b', 'c')


# Keyword-only parameters help solve this dilemma. In the function definition, specify *args to indicate a variable
# number of positional arguments, and then specify prefix after that:

def concat(*args, prefix='-> ', sep='.'):
    print(f'{prefix}{sep.join(args)}')


concat('a', 'b', 'c')
concat('a', 'b', 'c', prefix='//')
concat('a', 'b', 'c', prefix='//', sep='-')


def oper(x, y, *, op='+'):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
        return x / y
    else:
        return None


print(oper(3, 4, op='+'))

print(oper(3, 4, op='/'))


# >>> oper(3, 4, "I don't belong here")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: oper() takes 2 positional arguments but 3 were given
#
# >>> oper(3, 4, '+')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: oper() takes 2 positional arguments but 3 were given


# Positional-Only Arguments
# As of Python 3.8, function parameters can also be declared positional-only, meaning the corresponding arguments must be supplied positionally and can’t be specified by keyword.
#
# To designate some parameters as positional-only, you specify a bare slash (/) in the parameter list of a function
# definition. Any parameters to the left of the slash (/) must be specified positionally. For example,
# in the following function definition, x and y are positional-only parameters, but z may be specified by keyword

def f(x, y, /, z):
    print(f'x: {x}')
    print(f'y: {y}')
    print(f'z: {z}')


f(1, 2, 3)
f(1, 2, z=4)
