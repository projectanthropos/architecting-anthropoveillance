## Python References

* Functions are first class objects
* Nested Functions
* Returning functions (function factory)
* Decorators
* Different applications
  * timer
  * sleep decorator
  * logger
  * login requiered decorator

&nbsp;
&nbsp;
&nbsp;

## Functions are first class objects

"This means that functions can be passed around, and used as arguments, just like any other value (e.g, string, int, float)."

```python
def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)

print(call_foo_with_arg(foo, 3))
```

&nbsp;

## Nested Functions

Because of the first-class nature of functions in Python, you can define functions inside other functions. Such functions are called nested functions.

```python
def parent():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())
```

&nbsp;

## Returning functions (function factory)

```python
def surround_with(surrounding):
    """Return a function that takes a single argument and."""
    def surround_with_value(word):
        return '{}{}{}'.format(surrounding, word, surrounding)
    return surround_with_value

def transform_words(content, targets, transform):
    """Return a string based on *content* but with each occurrence 
    of words in *targets* replaced with
    the result of applying *transform* to it."""
    result = ''
    for word in content.split():
        if word in targets:
            result += ' {}'.format(transform(word))
        else:
            result += ' {}'.format(word)
    return result

markdown_string = 'My name is Jeff Knupp and I like Python but I do not own a Python'
markdown_string_italicized = transform_words(markdown_string, ['Python', 'Jeff'],
        surround_with('*'))
print(markdown_string_italicized)
```

&nbsp;

## Decorators

```python
def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)

just_some_function()
```

&nbsp;

## Different applications

**timer**
```python
import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())
```
**sleep decorator**
```python
from time import sleep


def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_number(num))
```
**logger**
```python
from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass
```
**login requiered decorator**
```python
from functools import wraps
from flask import g, request, redirect, url_for

def login_requiered(f):
    @wraps(d)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next = request.url))
        return f(*args, **kwargs)
    return decorated_function
    
@app.route('/secre')
@login_requiered
def secret():
    pass
```

&nbsp;
&nbsp;
&nbsp;
> https://realpython.com/primer-on-python-decorators/

> https://jeffknupp.com/blog/2013/11/29/improve-your-python-decorators-explained/

> http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

> https://www.thecodeship.com/patterns/guide-to-python-function-decorators/
