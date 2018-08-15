## Python References

* Expressions and operators
* Conditionals / flow control
* Loops
* Functions

&nbsp;
&nbsp;
&nbsp;


### Expressions and operators
**Python expressions and operators in precedence**

p |Type | Symbols|
--|-----|-----------------------
1 | member access | `expr.member`
2 | function/method calls | `expr(...)`
2 | cibtauber subscripts/slices | `expr[...]`
3 | exponentation | `**`
4 | unary operators | `+expr, -expr, ~expr`
5 | multiplication, division | `*`, `/`, `//`, `%`
6 | addition, subtraction | `+`, `-`
7 | bitwise shifting | `<<`, `>>`
8 | bitwise-and | ` & `
9 | bitwise-xor | ` ^ `
10 | bitwise-or |  `¦`
11 | comparisons | `is`, `is not`, `==`, `!=`, `<`, `<=`, `>`, `>=`
11 | containment | `in`, `not in`
12 | logical-not | `not expr`
13 | logical-and | `and`
14 | Logical-or | `or`
15 | conditional | `val1 if cond else val2`
16 | assignments | `=`, `+=`, `-=`, `*=`, etc.

To test some of these you can assign values to random variables and try some basic arithmetic e.g. `a = 10` hit enter, then `b = 20`, `c = 30`, then try `a * b`, `a ** b`, `a = b`, `a = b or b < a`, `a < b and b < c` etc.. 

&nbsp;

**Expressions and operators continued**

```python
s[j]  
#element at index j

s[start:stop]  
#slice including indices [start,stop)

s[start:stop:step]  
#slice including indices start, start + step, start + `2*step`,..., up to but not equal or stop

s + t  
#concatenation of sequences

k * s  
#shorthand for s + s + s + ... (k times)

val in s  
#containment check

val not in s 
#non-containment check

d[key]  
#value associated with fiven key

d[key] = value
#set (or reset) the value associated with a given key

del d[key]
#remove key and its associated value from dictionary

key in d
#containment check

key not in d
#non-contaminment check

d1 == d2
#d1 is equivalent to d2

d1 != d2
#d1 is not equivalent to d2
```

&nbsp;

### Conditionals

Conditionals are a way for you to control the flow of the code execution in your script. 

If you're working from the default IDLE go to File > New File. If you're still in your shell, and the python interpreter is open (meaning you still see >>>) type `quit()` to exit the interpreter, and type `atom` to open Atom editor. Save your file with a .py extension (e.g. conditionals.py) then type in this and save it. 

```python
grade = 82

if grade >= 90:
    if grade == 100:
        print('A+')
    else:
        print('A')
        
elif grade >= 80:
    print("B")

elif grade >= 70:
    print("C")
    
else:
    print("F")
```

Note the syntax, whenever you start a conditional you always end it with `:`. Same is true for loops, functions. You've probably noticed that besides autocompleting when you hit enter after a conditional, it also indents for you (it adds white space in front of the next line). This indentation matters in python, it basically tells the interpreter what belongs where. When you're writing code in an editor that doesn't indent automatically, to indent manually, you hit the space four times, not the tab.

Now run your script in the interpreter. If you're using the idle and the default interpreter go Run > Run module. To do this from the shell first navigate to the folder where you've saved your file and type in `python conditionals.py`. It'll execute the script and return `B`. Go back to the editor, change the value of `grade` save it and run it again, do so a few times, or write different other flows to get the hang of it. By the way, in your shell, when you hit upwards arrow key it brings the last command you've typed.

&nbsp;

### Loops

Loops are a way of repeating certain lines of code multiple times.

**While loop**
```python
x = 0
while x < 100:
    print(x)
    x += 1
```
Basically, to read in human language, while x is less than 100 print x and every time you do so add 1 to x. So it makes a list of numbers from 0 to 100 and loops over it. By the way, `x += ` is the same as writing `x = x + 1`. If you didn't add something like this at the end your script would run endlessly because x will always be less than 100, so your computer would crash at the end.

**For loop**
```python
for x in range(10):
    print(x)
```
```python
fruits = ['apple', 'orrange', 'passion fruit']

for fruit in fruits:
    print fruit
````
```python
scarfbook_of_depp = {
"scarf 1":"blue", "scarf 2":"mahogany", "total":569, "thirsty":True, "drink":"whiskey"
}

for key, value in scarfbook_of_depp.items():
    print('% s: % s' % (key, value))
```

&nbsp;

### Functions

Function will take an input, do a certain number of operations within itself, and return a value. You start a function by typing in the `def` key word, ending with `()` and `:`. You call a function by typin in its name followed by `()`.  This is a basic syntax for functions.

```python
def my_function():
    """Function Documentation"""
    print("Hello World")
```
By the way, anything that's within three quotation marks `""" ... """` or is after the `#` sign is just a comment for us, humans, the interpreter will ignore those lines. These are some examples of functions with arguments.

```python
# Positional
def add(x, y):
    return x + y
    
# keyword
def shout(phrase='Yipee'):
    print(phrase)
    
# Position + Keyword
def echo(text, prefix=''):
    print('%s%s' % (prefix, text)
```
Functions with arbitrary arguments.
```python
def some_method(*args, **kwargs):
    for arg in args:
        print arg
    
    for key, value in kwargs.items():
        print key
        
some_method(1, 2, 3, name = 'Numbers')
```

&nbsp;
&nbsp;
&nbsp;



> Goodrich, M., Tamassia, R., & Goldwasser, M. (2013). Data structures and algorithms in Python. Hoboken, NJ: Wiley.
