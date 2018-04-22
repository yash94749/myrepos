Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:40:30) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: D:\python-class\hypotenuse.py ===================
enter ther value of x1. 4
enter ther value of y1. 5
6.40312423743
>>> 6.40312423743
6.40312423743
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s = "This is a temporary text"
>>> s
'This is a temporary text'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(s.rjust)
Help on built-in function rjust:

rjust(...)
    S.rjust(width[, fillchar]) -> string
    
    Return S right-justified in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> s.rjust(40, '#')
'################This is a temporary text'
>>> s.rjust(20, '#')
'This is a temporary text'
>>> s.rjust(25, '#')
'#This is a temporary text'
>>> s.rjust(40)
'                This is a temporary text'
>>> help(s.rpartition)
Help on built-in function rpartition:

rpartition(...)
    S.rpartition(sep) -> (head, sep, tail)
    
    Search for the separator sep in S, starting at the end of S, and return
    the part before it, the separator itself, and the part after it.  If the
    separator is not found, return two empty strings and S.

>>> s
'This is a temporary text'
>>> s.rpartition('is')
('This ', 'is', ' a temporary text')
>>> help(s.partition)
Help on built-in function partition:

partition(...)
    S.partition(sep) -> (head, sep, tail)
    
    Search for the separator sep in S, and return the part before it,
    the separator itself, and the part after it.  If the separator is not
    found, return S and two empty strings.

>>> s.rpartition('ls')
('', '', 'This is a temporary text')
>>> s.partition('ls')
('This is a temporary text', '', '')
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(s.rsplit)
Help on built-in function rsplit:

rsplit(...)
    S.rsplit([sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string S, using sep as the
    delimiter string, starting at the end of the string and working
    to the front.  If maxsplit is given, at most maxsplit splits are
    done. If sep is not specified or is None, any whitespace string
    is a separator.

>>> s.rsplit()
['This', 'is', 'a', 'temporary', 'text']
>>> s.rsplit('a')
['This is ', ' tempor', 'ry text']
>>> s.rsplit('a', 4)
['This is ', ' tempor', 'ry text']
>>> s.rsplit('a', 1)
['This is a tempor', 'ry text']
>>> s.rsplit('a', 2)
['This is ', ' tempor', 'ry text']
>>> s.rsplit('t', 2)
['This is a temporary ', 'ex', '']
>>> help(s.rstrip)
Help on built-in function rstrip:

rstrip(...)
    S.rstrip([chars]) -> string or unicode
    
    Return a copy of the string S with trailing whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> s.rstrip()
'This is a temporary text'
>>> s = 'This is a temporary     text'
>>> s.rstrip()
'This is a temporary     text'
>>> s = '     This is a temporary text     "
SyntaxError: EOL while scanning string literal
>>> s = "     This is a temporary text     "
>>> s.rstrip()
'     This is a temporary text'
>>> s = '     This is a temporary text"
SyntaxError: EOL while scanning string literal
>>> s = "     This is a temporary text"
>>> s.rstrip()
'     This is a temporary text'
>>> s.rstrip('a')
'     This is a temporary text'
>>> s = "     This is a temporary text     "
>>> s.rstrip('a')
'     This is a temporary text     '
>>> str = "88888888this is string example....wow!!!8888888";
>>> str.rstrip('8')
'88888888this is string example....wow!!!'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(s.split)
Help on built-in function split:

split(...)
    S.split([sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are removed
    from the result.

>>> s
'     This is a temporary text     '
>>> s.split()
['This', 'is', 'a', 'temporary', 'text']
>>> s = "This is a test string"
>>> s.split('s')
['Thi', ' i', ' a te', 't ', 'tring']
>>> s.split('s', 1)
['Thi', ' is a test string']
>>> s = '     This is a temporary text     '
>>> s.rsplit('s', 1)
['     This i', ' a temporary text     ']
>>> s.rsplit()
['This', 'is', 'a', 'temporary', 'text']
>>> help(s.splitlines)
Help on built-in function splitlines:

splitlines(...)
    S.splitlines(keepends=False) -> list of strings
    
    Return a list of the lines in S, breaking at line boundaries.
    Line breaks are not included in the resulting list unless keepends
    is given and true.

>>> s = "this is a text string. its good for testing"
>>> s.splitlines()
['this is a text string. its good for testing']
>>> s.splitlines(keepends=true)

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s.splitlines(keepends=true)
NameError: name 'true' is not defined
>>> s.splitlines(keepends=True)

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s.splitlines(keepends=True)
TypeError: splitlines() takes no keyword arguments
>>> s.splitlines('.')

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.splitlines('.')
TypeError: an integer is required
>>> s.splitlines(21)
['this is a text string. its good for testing']
>>> s = "this is a text string\nits good for testing"
>>> s.splitlines()
['this is a text string', 'its good for testing']
>>> s.splitlines(1)
['this is a text string\n', 'its good for testing']
>>> s = "this is a text string\nits good for testing\nwe need to improve it\n if required"
>>> s.splitlines(0)
['this is a text string', 'its good for testing', 'we need to improve it', ' if required']
>>> s.splitlines(1)
['this is a text string\n', 'its good for testing\n', 'we need to improve it\n', ' if required']
>>> s.splitlines(2)
['this is a text string\n', 'its good for testing\n', 'we need to improve it\n', ' if required']
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> type(s)
<type 'str'>
>>> ver = ((1, datetime.datetime(2016, 12, 26, 17, 59, 30)), (1, datetime.datetime(2016, 12, 29, 17, 59, 30)))

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    ver = ((1, datetime.datetime(2016, 12, 26, 17, 59, 30)), (1, datetime.datetime(2016, 12, 29, 17, 59, 30)))
NameError: name 'datetime' is not defined
>>> s
'this is a text string\nits good for testing\nwe need to improve it\n if required'
>>> 
>>> s = "this is a text string"
>>> s
'this is a text string'
>>> help(s.startswitgh)

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    help(s.startswitgh)
AttributeError: 'str' object has no attribute 'startswitgh'
>>> help(s.startswith)
Help on built-in function startswith:

startswith(...)
    S.startswith(prefix[, start[, end]]) -> bool
    
    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.

>>> s.startswith('s')
False
>>> s.startswith('i', 0, 20)
False
>>> s.startswith('t')
True
>>> 
>>> 
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> strip

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    strip
NameError: name 'strip' is not defined
>>> 
>>> help(s.strip)
Help on built-in function strip:

strip(...)
    S.strip([chars]) -> string or unicode
    
    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> s.strip()
'this is a text string'
>>> s="     this is a text string         "
>>> s.strip()
'this is a text string'
>>> s="     this is a text string"
>>> s.strip()
'this is a text string'
>>> s.strip('i')
'     this is a text string'
>>> help(s.sqapcase)

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    help(s.sqapcase)
AttributeError: 'str' object has no attribute 'sqapcase'
>>> help(s.swapcase)
Help on built-in function swapcase:

swapcase(...)
    S.swapcase() -> string
    
    Return a copy of the string S with uppercase characters
    converted to lowercase and vice versa.

>>> s = "This Is A Text File"
>>> s.swapcase()
'tHIS iS a tEXT fILE'
>>> s ='A'
>>> s.swapcase()
'a'
>>> help(s.title)
Help on built-in function title:

title(...)
    S.title() -> string
    
    Return a titlecased version of S, i.e. words start with uppercase
    characters, all remaining cased characters have lowercase.

>>> s = "this is a Text File"
>>> s.title()
'This Is A Text File'
>>> s = "This is a text file"
>>> s.title()
'This Is A Text File'
>>> 
>>> help(s.translate)
Help on built-in function translate:

translate(...)
    S.translate(table [,deletechars]) -> string
    
    Return a copy of the string S, where all characters occurring
    in the optional argument deletechars are removed, and the
    remaining characters have been mapped through the given
    translation table, which must be a string of length 256 or None.
    If the table argument is None, no translation is applied and
    the operation simply removes the characters in deletechars.

>>> s
'This is a text file'
>>> intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

>>> print s.translate(trantab)

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    print s.translate(trantab)
NameError: name 'trantab' is not defined
>>> intab = "aeiou"
>>> from string import maketrans
>>> intab = "aeiou"
>>> outtab = "12345"
>>> trantab = maketrans(intab, outtab)
>>> print s.translate(trantab)
Th3s 3s 1 t2xt f3l2
>>> print s.translate(trantab, 'xt')
Th3s 3s 1 2 f3l2
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(s.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string
    
    Return a copy of the string S converted to uppercase.

>>> s.upper()
'THIS IS A TEXT FILE'
>>> s
'This is a text file'
>>> s.upper()
'THIS IS A TEXT FILE'
>>> help(s.zfill)
Help on built-in function zfill:

zfill(...)
    S.zfill(width) -> string
    
    Pad a numeric string S with zeros on the left, to fill a field
    of the specified width.  The string S is never truncated.

>>> s.zfill(45)
'00000000000000000000000000This is a text file'
>>> s.zfill(40)
'000000000000000000000This is a text file'
>>> s.zfill()

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    s.zfill()
TypeError: zfill() takes exactly 1 argument (0 given)
>>> s.zfill(5)
'This is a text file'
>>> 

>>> 
>>> 
>>> list1 = ['yash', 'vikash', 'rabish', 'vijay', 'manish', 'vaibhav']
>>> list1
['yash', 'vikash', 'rabish', 'vijay', 'manish', 'vaibhav']
>>> type(list1)
<type 'list'>
>>> print list[3 - 2]

Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    print list[3 - 2]
TypeError: 'type' object has no attribute '__getitem__'
>>> print list1[3 - 2]
vikash
>>> list2 = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
>>> list2
['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
>>> len(list2)
4
>>> len(list2)
4
>>> i = 1
>>> while i <= len(list2):
	print list2[-i]
	print len(list2[-i])
	i=i+1

	
[1, 2, 3]
3
['Brie', 'Roquefort', 'Pol le Veq']
3
1

Traceback (most recent call last):
  File "<pyshell#145>", line 3, in <module>
    print len(list2[-i])
TypeError: object of type 'int' has no len()
>>> len (list2[1])

Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    len (list2[1])
TypeError: object of type 'int' has no len()
>>> len (list2[0])
5
>>> len (list2[2])
3
>>> len (list2[1])

Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    len (list2[1])
TypeError: object of type 'int' has no len()
>>> len (str(list2[1]))

Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    len (str(list2[1]))
TypeError: 'str' object is not callable
>>> len (str(list2[1]))

Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    len (str(list2[1]))
TypeError: 'str' object is not callable
>>> len (str(list2[0]))

Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    len (str(list2[0]))
TypeError: 'str' object is not callable
>>> len (list2[0]))
SyntaxError: invalid syntax
>>> len list2[0]
SyntaxError: invalid syntax
>>> len (list2[0])
5
>>> 
>>> 
>>> 
>>> 
>>> list2 = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> list2
['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
>>> list1 = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
>>> id(list1)
55127048L
>>> id(list2)
49267464L
>>> a = "apple"
>>> b ="apple"
>>> id(a)
45453920L
>>> id(b)
45453920L
>>> 

>>> 
>>> 
>>> 
>>> 
>>> s = 'banana'
>>> s.split('a')
['b', 'n', 'n', '']
>>> list1
['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
>>> string.join(list1)

Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    string.join(list1)
NameError: name 'string' is not defined
>>> import string
>>> string.join(list1)

Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    string.join(list1)
  File "C:\Python27\lib\string.py", line 320, in join
    return sep.join(words)
TypeError: sequence item 1: expected string, int found
>>> list1 = ['yash', 'yashwant', 'vikash', 'vaibhav']
>>> string.join(list1)
'yash yashwant vikash vaibhav'
>>> list1
['yash', 'yashwant', 'vikash', 'vaibhav']
>>> song = "The rain in Spain..."
>>> string.split(song)
['The', 'rain', 'in', 'Spain...']
>>> song = "The rain in Spain..."
>>> string.split(song)
['The', 'rain', 'in', 'Spain...']
>>> song
'The rain in Spain...'
>>> string.split(song, 'ai')
['The r', 'n in Sp', 'n...']
>>> list = ['The', 'rain', 'in', 'Spain...']
>>> string.join(list)
'The rain in Spain...'
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(list.append)
Help on built-in function append:

append(...)
    L.append(object) -- append object to end

>>> list.append = ['vinay', 'vijay']

Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    list.append = ['vinay', 'vijay']
AttributeError: 'list' object attribute 'append' is read-only
>>> list.append('vinay', 'vijay')

Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    list.append('vinay', 'vijay')
TypeError: append() takes exactly one argument (2 given)
>>> list.append('vinay')
>>> list
['The', 'rain', 'in', 'Spain...', 'vinay']
>>> list.append(['vinay', 'vijay'])
>>> list
['The', 'rain', 'in', 'Spain...', 'vinay', ['vinay', 'vijay']]
>>> list = ['yash', 'yashwant', 'vikash', 'vaibhav']
>>> list
['yash', 'yashwant', 'vikash', 'vaibhav']
>>> help(list.count)
Help on built-in function count:

count(...)
    L.count(value) -> integer -- return number of occurrences of value

>>> list.count('vikash')
1
>>> 

>>> 
>>> 
>>> list[4] = ['ajay']

Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    list[4] = ['ajay']
IndexError: list assignment index out of range
>>> list.append('ajay')
>>> list
['yash', 'yashwant', 'vikash', 'vaibhav', 'ajay']
>>> list.append('vikash')
>>> list
['yash', 'yashwant', 'vikash', 'vaibhav', 'ajay', 'vikash']
>>> list.count('vikash')
2
>>> help(list.extend)
Help on built-in function extend:

extend(...)
    L.extend(iterable) -- extend list by appending elements from the iterable

>>> list.extend('vikash')
>>> list
['yash', 'yashwant', 'vikash', 'vaibhav', 'ajay', 'vikash', 'v', 'i', 'k', 'a', 's', 'h']
>>> abc = ['shiva', 'shubham']
>>> list.extend(abc)
>>> list
['yash', 'yashwant', 'vikash', 'vaibhav', 'ajay', 'vikash', 'v', 'i', 'k', 'a', 's', 'h', 'shiva', 'shubham']
>>> del list[6:12]
>>> list
['yash', 'yashwant', 'vikash', 'vaibhav', 'ajay', 'vikash', 'shiva', 'shubham']
>>> index

Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    index
NameError: name 'index' is not defined
>>> 
>>> 
>>> 
>>> 
>>> help(list.index)
Help on built-in function index:

index(...)
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> list.index('vikash')
2
>>> list.index('vikash' 3, 8)
SyntaxError: invalid syntax
>>> list.index('vikash', 3, 8)
5
>>> list.index('shiva', 1, 6)

Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    list.index('shiva', 1, 6)
ValueError: 'shiva' is not in list
>>> list.index('shiva', 1, 8)
6
>>> help(list.insert)
Help on built-in function insert:

insert(...)
    L.insert(index, object) -- insert object before index

>>> #list.index(2, 'mithilesh')
>>> list
['yash', 'yashwant', 'vikash', 'vaibhav', 'ajay', 'vikash', 'shiva', 'shubham']
>>> list.index(2, 'mithilesh')

Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    list.index(2, 'mithilesh')
TypeError: slice indices must be integers or None or have an __index__ method
>>> list.insert(2, 'mithilesh')
>>> list
['yash', 'yashwant', 'mithilesh', 'vikash', 'vaibhav', 'ajay', 'vikash', 'shiva', 'shubham']
>>> 
>>> help(list.pop)
Help on built-in function pop:

pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.

>>> list.pop()
'shubham'
>>> list
['yash', 'yashwant', 'mithilesh', 'vikash', 'vaibhav', 'ajay', 'vikash', 'shiva']
>>> list.pop(5)
'ajay'
>>> list
['yash', 'yashwant', 'mithilesh', 'vikash', 'vaibhav', 'vikash', 'shiva']
>>> list.pop(7)

Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    list.pop(7)
IndexError: pop index out of range
>>> 
>>> help(list.remove)
Help on built-in function remove:

remove(...)
    L.remove(value) -- remove first occurrence of value.
    Raises ValueError if the value is not present.

>>> list
['yash', 'yashwant', 'mithilesh', 'vikash', 'vaibhav', 'vikash', 'shiva']
>>> list.remove('vikash')
>>> list
['yash', 'yashwant', 'mithilesh', 'vaibhav', 'vikash', 'shiva']
>>> list.remove('vinay')

Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    list.remove('vinay')
ValueError: list.remove(x): x not in list
>>> list.remove()

Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    list.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> 
>>> 
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> 
>>> help(list.
     
KeyboardInterrupt
>>> help(list.reverse)
Help on built-in function reverse:

reverse(...)
    L.reverse() -- reverse *IN PLACE*

>>> list
['yash', 'yashwant', 'mithilesh', 'vaibhav', 'vikash', 'shiva']
>>> list.reverse()
>>> list
['shiva', 'vikash', 'vaibhav', 'mithilesh', 'yashwant', 'yash']
>>> list[2] = list[4]
>>> list
['shiva', 'vikash', 'yashwant', 'mithilesh', 'yashwant', 'yash']
>>> help(list.sort)
Help on built-in function sort:

sort(...)
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1

>>> list.sort()
>>> list
['mithilesh', 'shiva', 'vikash', 'yash', 'yashwant', 'yashwant']
>>> list.sort(cmp=None, key=None, reverse=True)
>>> list
['yashwant', 'yashwant', 'yash', 'vikash', 'shiva', 'mithilesh']
>>> list.sort(cmp=a, key=None, reverse=True)

Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    list.sort(cmp=a, key=None, reverse=True)
TypeError: 'str' object is not callable
>>> L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1

>>> list.sort()
>>> list
['mithilesh', 'shiva', 'vikash', 'yash', 'yashwant', 'yashwant']
>>> list.sort(cmp=None, key=None, reverse=True)
>>> list
['yashwant', 'yashwant', 'yash', 'vikash', 'shiva', 'mithilesh']
>>> list.sort(cmp=a, key=None, reverse=True)

Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    list.sort(cmp=a, key=None, reverse=True)
TypeError: 'str' object is not callable
>>>
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> a = [1, 2, 3]
>>> b = [3, 4, 5]
>>> a.append(b)
>>> a
[1, 2, 3, [3, 4, 5]]
>>> del a(3)
SyntaxError: can't delete function call
>>> del a[2:]
>>> a
[1, 2]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5]
>>> tuple = 'a', 'b', 'c', 'd', 'e'
>>> type(tuple)
<type 'tuple'>
>>> t1 = ('yash',)
>>> type(t1)
<type 'tuple'>
>>> 





>>> 

>>> t2 = 'a', 'b', 'c', 'd'
>>> type(t2)
<type 'tuple'>
>>> tuple[0]
'a'
>>> t3 = 'A", + t2[1:]
SyntaxError: EOL while scanning string literal
>>> t3 = 'A', + t2[1:]

Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    t3 = 'A', + t2[1:]
TypeError: bad operand type for unary +: 'tuple'
>>> t3 = ('A',) + t2[1:]
>>> t3
('A', 'b', 'c', 'd')
>>> a, b = d, e

Traceback (most recent call last):
  File "<pyshell#302>", line 1, in <module>
    a, b = d, e
NameError: name 'd' is not defined
>>> 
KeyboardInterrupt
>>> a, b = 3, 4
>>> a
3
>>> b
4
>>> type(a)
<type 'int'>
>>> s1 = ('yash', 'vikash', 'vinay', 'vijendra', 'vaibhav')
>>> s2 = ('vaibhav', 'vaishanav', 'ram', 'vishnu', 'vimal')
>>> type(s1)
<type 'tuple'>
>>> type(s2)
<type 'tuple'>
>>> s1
('yash', 'vikash', 'vinay', 'vijendra', 'vaibhav')
>>> s2
('vaibhav', 'vaishanav', 'ram', 'vishnu', 'vimal')
>>> s1, s2 = s2, s1
>>> s2
('yash', 'vikash', 'vinay', 'vijendra', 'vaibhav')
>>> s1
('vaibhav', 'vaishanav', 'ram', 'vishnu', 'vimal')
>>> 
>>> import random
>>> for i in range(10):
    x = random.random()
    print x

    
0.857682321022
0.35993687486
0.862235381849
0.478994206195
0.871872125272
0.13092687314
0.422803612228
0.262560152794
0.891576098577
0.127908827142
>>> range[1:10]

Traceback (most recent call last):
  File "<pyshell#320>", line 1, in <module>
    range[1:10]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> 
