## Python References

* Recursion
* Fibonacci with recursion

&nbsp;
&nbsp;
&nbsp;

### Recursion

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
print(factorial(6))
```

The recursive algorithm breaks the problem down into smaller problems and refers to itself, or calls itself from within each time its iterating. To quote from the source below "This function does not use any explicit loops. Repetition is provided by the repeated recursive invocations of the function. There is no circularity in this definition, because each time the function is invoked, its argument is smaller by one, and when a base case is reached, no further recursive calls are made."

&nbsp;

### Fibonacci with recursion

```python
def bad_fibonacci(n):
"""Return the nth Fibonacci number."""
if n <= 1:
    return n
else:
    return bad_fibonacci(n-2) + bad_fibonacci(n-1)
```
```python
def good_fibonacci(n):
"""return pair of Fibonacci numbers, F(n) and F(n-1)."""
if n <= 1:
    return (n,0)
else:
    (a, b) = good_fibonacci(n-1)
    return (a+b, a)
```

&nbsp;

For additional useful information on functions look up Big-Oh notation `O(n)`. That particular function is about how much time an algorithm takes to finish in the worst case scenario.

&nbsp;
&nbsp;
&nbsp;



> Goodrich, M., Tamassia, R., & Goldwasser, M. (2013). Data structures and algorithms in Python. Hoboken, NJ: Wiley.
