## Python References

* Objects
* The *Class* keyword
* Instance attributes / fields / data members
* Class object attributes
* Methods / member functions
* Bound and unbound method calls
* Static and class method

&nbsp;
&nbsp;
&nbsp;

OOP refers to object oriented programming. This paragidm in programming allows for a greater level of abstraction, modularity and encapsulation in your code. Method is function that is associatied with a class. Attributes are the data given to a class.

&nbsp;

### Objects

Everything in python is an object. Try typing and run the following.

```python
import sys

def function():
    pass

print(type(1))
print(type(""))
print(type([]))
print(type({}))
print(type(()))
print(type(object))
print(type(function))
print(type(sys))
```

&nbsp;


### The *Class* keyword
```python
class First():
    pass

fr = First()

print(type(fr))
print(type(First))
```

&nbsp;

### Instance attributes / fields / data members

```python
class Student:
    def __init__(self, name):
        delf.name = name

muna = Student("Muna")

print(muna)
print(muna.name)
```
```python
class Dynamic:
    pass

d = Dynamic()
d.name = "Dynamic"
print d.name
```

&nbsp;

### Class object attributes

```python
class Student:
    school = "UMN" # attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age


muna = Student("Muna", 20)
sam = Student("Sam", 24)

print(muna.name, muna.age)
print(sam.name, sam.age)

print(Student.school)
print(muna.__class__.school)
print(sam.__class__.school)

```

&nbsp;

### Methods / member functions

```python
class Circle():

    pi = 3.141592

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius


c = Circle()

c.setRadius(5)
print(c.getRadius())
print(c.area())
```

&nbsp;

### Bound and unbound method calls

```python
class Methods():

    def __init__(self):
        self.name = 'Methods'

    def getName(self):
        return self.name


m = Methods()

print(m.getName())
print(Methods.getName(m))
```

&nbsp;

### Static and class method

```python

# static methods dont use the cls. or self.
# they don't take the instance or the class as method

class Circle():

    pi = 3.141592

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    @staticmethod
    def radian2degrees(rad):
        return rad * 180 / Circle.pi
        
    @classmethod
    def getPi(cls):
        return cls.pi

c = Circle()

c.setRadius(5)
print(c.getRadius())
print(c.area())
print(Circle.radian2degrees(1))
print(Circle.getPi())
```

&nbsp;
&nbsp;
&nbsp;
> http://zetcode.com/lang/python/oop/
