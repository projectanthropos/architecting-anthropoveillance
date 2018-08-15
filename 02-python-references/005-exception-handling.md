## Python References

* Common exception types
* Raising an exception
* Catching an exception

&nbsp;
&nbsp;
&nbsp;

"Exceptions are unexpected events that occur during the execution of a program. An exception might result from a logical error or an unanticipated situation."

### Common exception types

 Class | Description
-------|------------
 `Exception` | A base class for most error types
 `AttributeError` | Raised by syntax obj.foo, if obj has no member named foo
 `EOFError` | Raised if “end of file” reached for console or file input
 `IOError` | Raised upon failure of I/O operation (e.g., opening file)
 `IndexError` | Raised if index to sequence is out of bounds
 `KeyError` | Raised if nonexistent key requested for set or dictionary
 `KeyboardInterrupt` | Raised if user types ctrl-C while program is executing
 `NameError` | Raised if nonexistent identifier used
 `StopIteration` | Raised by next(iterator) if no element; see Section 1.8
 `TypeError` | Raised when wrong type of parameter is sent to a function
 `ValueError` | Raised when parameter has invalid value (e.g., sqrt(−5))
 `ZeroDivisionError` | Raised when any division operator used with 0 as divisor
 
 
&nbsp;

### Raising an exception

```python
def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError( x must be numeric ) 
    elif x < 0:
        raise ValueError( x cannot be negative ) 
    # do the real work here...
```
&nbsp;

### Catching an exception

```python
try:
    ratio = x / y
except ZeroDivisionError: 
... do something else ...
```
```python
try:
    fp = open( sample.txt )
except IOError as e:
    print( Unable to open the file: , e)
```
```python
age = −1 # an initially invalid choice 
while age <= 0:
    try:
        age = int(input( Enter your age in years:   )) 
        if age <= 0:
            print( Your age must be positive ) 
    except (ValueError, EOFError):
        print( Invalid response )
```
```python
age = −1 # an initially invalid choice 
while age <= 0:
    try:
        age = int(input( Enter your age in years:   )) 
        if age <= 0:
            print( Your age must be positive ) 
    except ValueError:
        print( That is an invalid age specification ) 
    except EOFError:
        print( There was an unexpected error reading input. ) 
        raise # let s re-raise this exception
```

&nbsp;

catching an exception `finally` syntax
```python
try:
    file = open(filePath, 'w')
    file.write("Hello World!")
exept IOError:
    print("Unable to create file on disk.")
finally:
    file.close()
```

&nbsp;
&nbsp;
&nbsp;


> Goodrich, M., Tamassia, R., & Goldwasser, M. (2013). Data structures and algorithms in Python. Hoboken, NJ: Wiley.

