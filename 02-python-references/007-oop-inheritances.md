## Python References

* Inheritance
* Multiple Inheritance
* Diamond problem
* *super* keyword
* Private methods
* Polymorphism
* Special methods

&nbsp;
&nbsp;
&nbsp;

### Inheritance

```python
class Human:
    def __init__(self):
        print("Human created!")

    def who_am_i(self):
        print("Human")

    def wear(self):
        print("I'm putting on something")


class JohnnyDepp(Human):
    def __init__(self):
        Human.__init__(self)
        print("Johnny Depp is created!")

    def who_am_i(self):
        print("Johnny Depp")

    def wear(self):
        print("I'm wearing my scarf!")

    def drink(self):
        print("whiskey")


j = JohnnyDepp()
j.who_am_i()
j.wear()
j.drink()
```

&nbsp;

### Multiple Inheritance

```python
from clock import Clock
from calendar import Calendar

class CalendarClock(Clock, Calendar):
    pass
```

&nbsp;

### Diamond problem

```python
class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
    
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    pass
```

&nbsp;

### *super* keyword

```python
class A:
    def __init__(self):
        print("A.__init__")

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()
    
class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()


class D(B,C):
    def __init__(self):
        print("D.__init__")
        super().__init__()
```

&nbsp;

### Private methods, attributes and name mangling

```python
class A:
    def __init__(self):
        self.__answer = "42"

    def get_answer(self):
        print(self.__answer)

    def __private_method(self):
        print("I am private!")


class B(A):
    pass


a = A()
print(a.__answer)  # this won't work
dir(a)
print(a.__private_method())  # won't work either
d = B()
print(b.get_answer())
```

&nbsp;

### Polymorphism

```python
a = "alfa"
b = (1, 2, 3, 4)
c = ['o', 'm', 'e', 'g', 'a']

print(a[2])
print(b[1])
print(c[3])

```

&nbsp;

### Special methods

```python
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, author: {}, pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


book = Book("Citizen Muna", "Muna", 304)

print(book)
print(len(book))
del book

```
&nbsp;
&nbsp;
&nbsp;



> https://www.python-course.eu/python3_multiple_inheritance.php
