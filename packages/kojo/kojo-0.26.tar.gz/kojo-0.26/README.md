`kojo` is a tool to help to transform, validate, and filter data. It has two main components:

1. `Process` allows to filter and map data items in a chainable interface for better readability.
2. `Item` allows to add log entries and meta data to each data item individually.

The rest of `kojo` is “nice to have”.

# Process

## Motivation

If we want to transform a number of dictionary items we can e.g. use a generator comprehension.

```py
def onedigit():
    for i in range(10):
        yield i

iterator = onedigit()
iterator = (i * i for i in iterator)
print(list(iterator))
# > [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Let's pretend we need all square numbers, that do not contain the digit 6:

```py
def onedigit():
    for i in range(10):
        yield i

iterator = onedigit()
iterator = (i * i for i in iterator)
iterator = (i for i in iterator if "6" not in str(i))
print(list(iterator))
# > [0, 1, 4, 9, 25, 49, 81]
```

This approach works fine when there are only some easy steps. When migrating data however there are often
a lot of steps and maybe even several input files.

Let's presume, we have two inputs and the transformations are too complex to use comprehensions. We use a
transformation function and to keep the code dry and call range directly:

```py
def square(i):
    return i * i

def no6(i):
    return "6" not in str(i)

def transform(iterator):
    iterator = (square(i) for i in iterator)
    iterator = (i for i in iterator if no6(i))
    return iterator

iterator = transform(range(10))
print(list(iterator))
# > [0, 1, 4, 9, 25, 49, 81]

iterator = transform(range(10, 20))
print(list(iterator))
# > [100, 121, 144, 225, 289, 324]
```

This code has two issues:

1. The transformation process needs data as input and is therefore not completely decoupled
1. Readability is bad when there are a lot of transformation steps

## Basic usage

```py
from kojo import Process, apply

def square(i):
    return i * i

def no6(i):
    return "6" not in str(i)

process = Process().map(square).filter(no6)

iterator = apply(range(10), process)
print(list(iterator))
# all square numbers of 0-9 that do not contain the digit 6
# > [0, 1, 4, 9, 25, 49, 81]

iterator = apply(range(10, 20), process)
print(list(iterator))
# all square numbers of 10-20 that do not contain the digit 6
# > [100, 121, 144, 225, 289, 324]

def digit_sum(i):
    return sum(int(digit) for digit in str(i))

post_process = Process().map(digit_sum)

iterator = apply(range(10, 20), process, post_process)
print(list(iterator))
# the digit sum of all square numbers of 10-20 that do not contain the digit 6
# > [1, 4, 9, 9, 19, 9]
```

The `Process` class is used to define a new process. It has two methods: `filter` and `map`. These methods can
be chained.

The `apply` function takes an Iterable and 1…n processes as arguments. It returns an Iterator that generates a list
of transformed and mapped items.

# Item

## Motivation

When migrating data it happens, that input data has issues. To handle these issues one need to know, which item
has which issues.

Instead of using logging that contains a reference to the item the `Item` class follows another approach by having
an own log. `Item` extends Pythons `dict` class and provides a log system, which is independent from the dictionary.

## Basic usage

```py
from kojo import Item

item = Item(meaningOfLife=54)
print(item)
# > {'meaningOfLife': 54}

if item["meaningOfLife"] != 42:
    item.log.warning("That's not the meaning of life")

print(item)
# > {'meaningOfLife': 54}

print(item.log.level)
# > 30 # (logging.WARNING)

print(len(item.log))
# > 1

print(item.log[0].message)
# > That's not the meaning of life

item.log.info("Please review")

print(len(item.log))
# > 2
```
