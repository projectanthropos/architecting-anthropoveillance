## Python References

* Python basic types / Variables

&nbsp;
&nbsp;
&nbsp;

### Variables

Formally, Python is an interpreted language. Meaning, the interpreter receives the command, evaluates that command, and reports the result of that command. The programmer typically defines a series of commands in advance and saves those commands in a plain text file known as source code. For Python, the source code is conventionally stored in a file named with the .py suffix. On most operating systems, the Python interpreter can be started by typing `python` from the shell/command linе. If you have multiple versions installed `python3` or `python2` depending on the version.

In programming variable is simply a name for something, like "Johnny Depp" is a name for "a human being who wears scarfs". Variables are just containers which store information and data. Start your shell (or the python IDLE whichever you prefer more). If you're in terminal or PowerShell type python and you should see `>>>` meaning you've started the python interpreter. Now enter this.`johnny_depp = "a human being who wears scarfs"` hit enter and type `number_of_scarfs = 100` hit enter. In this case, `johnny_depp` and `number_of_scarfs` are the names of your variables, you've declared them as variables by using `=` syntax. Now type in the variable name and hit enter to see what's contained in it. In all programming languages, there are many different types of variables.

&nbsp;

**The basic types of variables in python.**

Class | Description | Immutable?
------|-------------|----------
`bool`| Boolean value | ✓
`int` | integer (arbitrary magnitude) | ✓
`float` | floating-point number | ✓
`list` | mutable sequence of objects |
`tuple` | immutable sequence of objects | ✓
`str` | character string | ✓
`set` | unordered set of distinct objects |
`frozenset` | immutable form of set class | ✓
`dict` | associative mapping (dictionary) | 

Boolean values can be either `True` or `False`. Integer variables are just whole numbers `number_of_scarfs` was that kind of variable, floats are decimal numbers. String variables are any text information, basic collection of character objects, you declare them in quotation marks, e.g. `johnny_depp` was a string variable. In contrast to many other programming languages, in python, you don't have to know the type of a variable you're creating, you simply declare it with `=` syntax. But it's better you remember the type of the variable you've created. If you type in your shell `type(johnny_depp)` it'll tell you it's a string, and if you type in `type(number_of_scarfs)` it'll tell you it's an integer. If you type in `johnny_depp + number_of_scarfs` it'll give you an error, but if you type in `number_of_scarfs + 1` or `johnny_depp + " while sleeping"` it'll return a result.

Lists (also referred to as arrays), sets, tuples, and dictionaries are some of the basic data structures in python. These are basically ways of storing multiple values behind a single variable. If a python object is immutable it means you can't change it after you've created it, e.g., you can't remove/add new items to a `tuple` but you can remove/add them to a `list` or `dict` etc.. Lists can contain multiple types of variables, including other lists. e.g. (ignore the `>>>` symbol, you don't have to type it in), but type in the rest to get the hang of it.

```python
>>> my_list = [10, 2, 144, 4, 5, 77]
>>> other_list = [1, "apple", 4.56, True]
```

With square bracket notation, you create lists, and you separate values contained in it by a comma. With regular bracket notation e.g. `name_of_tuple = (1, 2, 3, "orange", 3.4)` you create tuples. Each one of the items in a list or a tuple is assigned an index by default. The first item is at index number 0, e.g. 

```python
>>> my_list = [10, 2, 144, 4, 5, 77]
>>> my_list[0]
10
>>>
```
if you request an item that's not on the list, it'll give you an error

```python
>>> my_list[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```
you can find out the length of a list for example like this
```python
>>> len(my_list)
6
>>>
```
and this way you can find out the last value of a list
```python
>>> my_list[len(my_list) - 1]
77
>>>
```
or you can simply type `my_list[-1]` and it'll go to the last value

Dictionaries are similar to lists, only in dictionaries, you don't access what's contained in it by an index number; each value in a dictionary has a key that you can assign to it. e.g.,

```python
>>> scarfbook_of_depp = {"scarf 1":"blue", "scarf 2":"mahogany", "total":569, "thirsty":True, "drink":"whiskey"}
>>> scarfbook_of_depp
{'scarf 1': 'blue', 'scarf 2': 'mahogany', 'total': 569, 'thirsty': True, 'drink': 'whiskey'}
>>> type(scarfbook_of_depp)
<class 'dict'>
>>>
```

to access a value in a dictionary you use the same notation as with lists, but instead of an index you enter the key, e.g.,

```python
>>> scarfbook_of_depp['scarf 2']
'mahogany'
>>>
```

&nbsp;
&nbsp;
&nbsp;



> Goodrich, M., Tamassia, R., & Goldwasser, M. (2013). Data structures and algorithms in Python. Hoboken, NJ: Wiley.

