## Python References

* Input
* Read files
* Write files

&nbsp;
&nbsp;
&nbsp;

I O refers to input and output. Print function, for example, is used to generate a standard output to the console. Below are some code samples dealing with input and output.

### Input
```python
name = input("What is your name?\n")
surname = input("what is your surname?\n")
print("Welcome {0} {1}!".format(name, surname))
```
```python
reply = input("Enter base and power, separated by spaces: ")
pieces = reply.split()
x = float(pieces[0])
y = float(pieces[1])
print("Power is equal {}".format(x**y))
```

&nbsp;

### Reading from a file
```python
file = open("input.py")
for line in file:
    print(line)

file.close()

with open("input2.py) as f:
    for line in f:
        print(line)
```

&nbsp;

### Writing to a file
```python
with open("new.py", "w") as f:
    f.write('print("hello world")')

with open("new.py) as f:
    code = f.read()
    exec(code)
```

&nbsp;

File processing. Behaviors for interacting with a text file via a file proxy (named fp).

 Calling Syntax | Description
---------------|------------
 `fp.read( )` | Return the (remaining) contents of a readable file as a string.
 `fp.read(k)` | Return the next k bytes of a readable file as a string.
 `fp.readline( )` | Return (remainder of ) the current line of a readable file as a string.
 `fp.readlines( )` | Return all (remaining) lines of a readable file as a list of strings.
 `for line in fp:` | Iterate all (remaining) lines of a readable file.
 `fp.seek(k)` | Change the current position to be at the kth byte of the file.
 `fp.tell( )` | Return the current position, measured as byte-offset from the start.
 `fp.write(string)` | Write given string at current position of the writable file.
 `fp.writelines(seq)` | Write each of the strings of the given sequence at the current position of the writable file. This command does not insert any newlines, beyond those that are embedded in the strings.
 `print(..., file=fp)` | Redirect output of print function to the file.


&nbsp;
&nbsp;
&nbsp;


> Goodrich, M., Tamassia, R., & Goldwasser, M. (2013). Data structures and algorithms in Python. Hoboken, NJ: Wiley.
