## Python References

* Lambda
* Map
* Filter
* Reduce

&nbsp;
&nbsp;
&nbsp;

### Lambda

```python
plus = lambda x, y: x + y
minus = lambda x, y: x - y
print(plus(1, 4))
print(minus(5, 3))
```

&nbsp;

### Map

```python
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5, 39)

F = map(fahrenheit, temp)
C = map(celsius, F)

# same with lambdas

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print(Fahrenheit)
C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print(C)
```
```python
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]

print(map(lambda x,y:x+y, a,b))

print(map(lambda x,y,z:x+y+z, a,b,c))

print(map(lambda x,y,z:x+y-z, a,b,c))
```

&nbsp;

### Filter

```python
fib = [0,1,1,2,3,5,8,13,21,34,55]
odd = filter(lambda x: x % 2 == 1, fib)
print(odd)
even = filter(lambda x: x % 2 == 0, fib)
print(even)
```

&nbsp;

### Reduce

```python
from functools import reduce
print(reduce(lambda x, y: x + y, [41, 11, 42, 13]))
```

&nbsp;
&nbsp;
&nbsp;

> https://www.python-course.eu/lambda.php
