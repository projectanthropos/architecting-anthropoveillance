## Python References

* Iterators
* Generators
* Generator expressions

&nbsp;
&nbsp;
&nbsp;

### Iterators

```python
class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """create an iterator for the given sequence."""
        # keep a reference to the underlying data
        self.__seq = sequence
        # will increment to 0 on first call to next
        self.__k = -1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self.__k < len(self.__seq):  # return the data element
            return(self.__seq[self.__k])
        else:
            raise StopIteration()  # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self
```

&nbsp;

### Generators

```python
def factorial(n):
    count = 1
    fact = 1
    while count <= n:
        yield fact
        count = count + 1
        fact = fact * count
        
for x in factorial(4):
    print(x)
```
```python
def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result

print take(5, squares()) # prints [1, 4, 9, 16, 25]
```

&nbsp;

### Generator expressions

```python
from generators import integers, take

s = (x*x for x in range(10)

print(type(s))
print(sum(s))

pyt = ((x, c, z) for z in integers()
                for y in range(1, z)
                for x in range(1, y)
                if x*x + y*y == z*z
                )
print(take(10, pyt))
```

&nbsp;
&nbsp;
&nbsp;

> https://anandology.com/python-practice-book/iterators.html
