# Memoiz

A thread-safe memoization decorator for functions and methods.

## Introduction

Memoiz provides a function decorator that can be used in order to augment functions or methods with memoization capabilties.  It makes reasonable assumptions about how and if to cache the return value of a function or method based on the arguments passed to it. The decorator can be used on both free and bound functions.

## Features

- A thread-safe cache
- Use the Memoiz decorator on free and bound functions
- Support for parameter and return type hints
- Cache invalidation

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Bound Functions (methods)](#bound-functions-methods)
  - [Free Functions](#free-functions)
- [Limitations](#limitations)
- [API](#api)
- [Test](#test)

## Installation

```bash
pip install memoiz
```

## Usage

### Bound Functions (methods)

In this example you will use Memoiz to memoize the return value of the `greeter.greet` method and print the greeting.

```py
from memoiz import Memoiz

# `cache` is a Python decorator and a callable.
cache = Memoiz()


class Greeter:

    def __init__(self):
        self.adv = "Very"

    @cache # Use the `cache` decorator in order to add memoization capabilities to the `greet` method.
    def greet(self, adj: str) -> str:
        return f"Hello, {self.adv} {adj} World!"


greeter = Greeter()

print("1:", cache._cache)

greeting = greeter.greet("Happy")

print("2:", greeting)
```

```bash
1: {}
2: Hello, Very Happy World!
```

As a continuation of the example, you will selectively invalidate cached articles using the `cache.invalidate` method.

```python
greeter = Greeter()

print("1:", cache._cache)

greeting = greeter.greet("Happy")

print("2:", greeting)

greeting = greeter.greet("Cautious")

print("3:", greeting)

# The cache has memoized the two method calls.
print("4:", cache._cache)

# Invalidate the call to `greeter.greet` with the "Happy" argument.
#                               ⮶ instance
cache.invalidate(greeter.greet, greeter, "Happy")
#                         ⮴ method       ⮴ args

print("5:", cache._cache)

# Invalidate the call to `greeter.greet` with the `Cautious` argument.
cache.invalidate(greeter.greet, greeter, "Cautious")

# The cache is empty.
print("6:", cache._cache)
```

```bash
1: {}
2: Hello, Very Happy World!
3: Hello, Very Cautious World!
4: {<bound method Greeter.greet of <__main__.Greeter object at 0x7fa5e7f837f0>>: {((<__main__.Greeter object at 0x7fa5e7f837f0>, 'Happy'), ()): 'Hello, Very Happy World!', ((<__main__.Greeter object at 0x7fa5e7f837f0>, 'Cautious'), ()): 'Hello, Very Cautious World!'}}
5: {<bound method Greeter.greet of <__main__.Greeter object at 0x7fa5e7f837f0>>: {((<__main__.Greeter object at 0x7fa5e7f837f0>, 'Cautious'), ()): 'Hello, Very Cautious World!'}}
6: {}
```

### Free Functions

In this example you will use Memoiz to memoize the return value of the `greet` function and print the greeting.

```py
from memoiz import Memoiz

cache = Memoiz()


@cache
def greet(adj: str) -> str:
    return f"Hello, {adj} World!"


print("1:", cache._cache)

greeting = greet("Happy")

print("2:", greeting)
```

```bash
1: {}
2: Hello, Happy World!
```

As a continuation of the example, you will selectively invalidate cached articles using the `cache.invalidate` method.

```python
print("1:", cache._cache)

greeting = greet("Happy")

print("2:", greeting)

greeting = greet("Cautious")

print("3:", greeting)

print("4:", cache._cache)

#                       ⮶ args
cache.invalidate(greet, "Happy")
#                ⮴ function

# The call using the "Happy" argument is deleted; however, the call using the
# "Cautious" is still present.
print("5:", cache._cache)

#                       ⮶ args
cache.invalidate(greet, "Cautious")
#                ⮴ function

# The cache is now empty.
print("6:", cache._cache)
```

```bash
1: {}
2: Hello, Happy World!
3: Hello, Cautious World!
4: {<function greet at 0x7fa5cefb8430>: {(('Happy',), ()): 'Hello, Happy World!', (('Cautious',), ()): 'Hello, Cautious World!'}}
5: {<function greet at 0x7fa5cefb8430>: {(('Cautious',), ()): 'Hello, Cautious World!'}}
6: {}
```

## Limitations

Memoization relies on the behavior of pure functions; given the same input the function produces the same output. It isn't safe to assume that a callable is pure in Python; hence, discretion must be used when applying the decorator to a given callable.

Memoiz uses a Python dictionary in order to cache the arguments and respective return value of the callable. Memoiz will attempt to transform a callable's arguments into a hashable representation. If it succeeds, the hashable representation of the callable's arguments is used as the dictionary key in order to store and look up the cached return value. If it fails, Memoiz will call the decorated function or method and return the result.

Memoiz employs a few strategies to produce a hashable lookup key. Memoiz will recursively iterate through `dict`, `list`, `set`, and `tuple` type arguments, transforming mutable objects into hashable representations. See the [Type Transformation](#type-transformation) table for type transformations. When a primitive is encountered (e.g., `int`, `float`, `complex`, `bool`, `str`, `None`), it is left as is. If `allow_hash` is set to `True` (the default), Memoiz will additionally attempt to discern if an object is hashable using Python's `hash` function.

Effectively what this all means is that if you are using common Python iterables and primitives as arguments to your callable, and if your callable doesn't have side effects, Memoiz should be able to accurately apply memoization to your callable.

### Type Transformation

| Type  | Hashable Type   |
| ----- | --------------- |
| dict  | tuple of tuples |
| list  | tuple           |
| tuple | tuple           |
| set   | tuple           |

## API

### The Memoiz Class

**memoiz.Memoiz(immutables, sequentials, allow_hash, deep_copy)**

- immutables `Tuple[type, ...]` An optional tuple of types that are assumed to be immutable. **Default:** `(int, float, complex, bool, str, type(None))`
- sequentials `Tuple[type, ...]` An optional tuple of types that are assumed to be sequence-like. **Default** `(list, tuple, set)`
- mapables `Tuple[type, ...]` An optional tuple of types that are assumed to be dict-like. **Default** `(dict,)`
- allow_hash `bool` An optional flag that indicates if an object's hash is sufficient for indexing the callable's arguments. **Default:** `True`
- deep_copy `bool` Optionally return the cached return value using Python's `copy.deepcopy`. This can help prevent mutations of the cached return value. **Default:** `True`.

**memoiz.\_\_call\_\_(callable)**

- callable `typing.Callable` The function or method for which you want to add memoization.

A `Memoiz` instance ([see above](#the-cache-class)) is a callable. This is the `@cache` decorator that is used in order to add memoization to a callable. Please see the above [usage](#usage) for how to use this decorator.

**memoiz.invalidate(callable, \*args, \*\*kwargs)**

- callable `typing.Callable` The callable.
- args `Any` The arguments passed to the callable.
- kwargs `Any` The keyword arguments passed to the callable.

Invalidates the cache for the specified callable and arguments. See the [usage](#usage) for for how to invalidate the cache.

> **NB** The first argument of a method (i.e., a bound function) is the object instance e.g., the `self` in the method definition.

**memoiz.invalidate_all()**

Resets the cache making items in the old cache potentially eligible for garbage collection.

## Test

Clone the repository.
```bash
git clone https://github.com/faranalytics/memoiz.git
```
Change directory into the root of the repository.
```bash
cd memoiz
```
Run the tests.
```bash
python tests/test.py -v
```