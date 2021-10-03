# Python3 program for explaining
# use of list, tuple, set and
# dictionary

# Lists
l = []

# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)

# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()

# Set
s = set()

# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)

# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()

# Tuple
t = tuple(l)

# Tuples are immutable
print("Tuple", t)
print()

# Dictionary
d = {}

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)

# Removing key-value pair
del d[10]
print("Dictionary", d)


tuple basics
>>> t = ('math', 101, 'grade', 98, )
>>> t[0]
math
>>> t[1]
101
>>> t[-1]
98
>>> new = t[2:]
>>> new
grade 98
>>> t           # check the original t unchanged
('math', 101, 'grade', 98, )
>>>
>>> t2 = ('letter grade', 'A',)
>>> t3 = t + t2
>>> t3
('math', 101, 'grade', 98, 'letter grade', 'A', )
>>>
>>> t4 = ('Hello',) *3
>>> t4
('Hello', 'Hello', 'Hello',)
>>>
>>> lst = ['good', 'morning']
>>> myTuple = tuple(lst)      # turn a list into a tuple
>>> myTuple
('good', 'morning')
>>> t5 = tuple('bear')     # turn a string into a tuple
>>> t5
('b', 'e', 'a', 'r')
>>>


check on tuples

>>> t = ('red','green','blue','yellow','blue','blue',)
>>> len(t)
4
>>> t.index('blue')        # returns the first time the item appears
2
>>> t.count('blue')
3
>>> 'yellow' in t           # check membership
True
>>>
>>> t[3]
'yellow'
>>> t[2] = 'pink'       # see if we can change element's value?
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
t.append('white')     # see if we can add a new element
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>>

sets basics

>>> mySet = {1,2,3,4,5,5,5,6,7,8}
>>> len(mySet)
8               # why not 10??
>>> mySet       # duplicate will be removed
{1,2,3,4,5,6,7,8}
>>> 
>>> lst = [8,9,6,7,6,8]
>>> s2 = set(lst)    # create a set from a list
>>> s2
{6,8,9,7}           # no duplicate, no order
>>>
>>> m = set('hello')    # turns a string into a set of unique letters
>>> print(m)
{'o', 'h', 'l', 'e'}
>>>
>>> s0 = set()      # call set() function with no argument will return an empty set
>>> s0
set()         # a set with no items, empty set is not {}
>>>
Some methods that works on sets:

Add items to an existing set: add(aItem) and update(anotherSet) methods.

Remove items from a set: remove(aItem) pop() will remove a random item from the set and return it's value. clear() methods will remove all items from a set.

Ex. 9.2-2 set methods

>>> farm = {'chicken', 'duck'}
>>> farm.add('goose')         # add one item at a time
>>> farm
{'chicken', 'goose', 'duck'}
>>>
>>> farm.update({'cow', 'sheep', 'chicken', 'elephant'})    
>>> farm
{'chicken', 'goose', 'cow', 'elephant', 'duck','sheep' }
>>> 'elephant' in farm   # fast membership testing
True
>>>
>>> farm.remove('elephant')
{'chicken', 'duck', 'goose', 'cow', 'sheep' }
>>>
>>> farm.pop()     # remove a random item and return it's value
'duck'
>>> farm
{'chicken', 'goose', 'cow', 'sheep' }
>>>
>>> farm.clear()    
>>> farm
set()        # All gone! The farm is quiet now.
>>>
Make a copy: copy() methods will return a copy of the original set as a new set. This is different than just assigning value.

set copy

>>> records = {'Math', 98, 'A+', 'Science', 90, 'A'}
>>> rec_copy1 = records
>>> rec_copy2 = records.copy()
>>>
>>> records.clear()
>>>
>>> records
set()
>>> rec_copy1   # rec_copy1 and records refer to the same object
set()
>>> rec_copy2
{'Math', 98, 'A+', 'Science', 90, 'A'}    # Thank God! We have a backup copy!
>>>
Some useful set operations:set operations

>>> s = {'H', 'I', 'J', 'K', 1,2,3}
>>> t = { 'o', 'p', 'e', 'n', 1,2,3}
>>>
>>> s - t         # in s but not in t
{'H', 'I', 'J', 'K'}
>>> s.difference(t)
{'H', 'I', 'J', 'K'}

>>> s & t         # in both s and t
{1, 2, 3}
>>> s.intersection(t)
{1, 2, 3}

>>> s | t        # all unique items from both s and t
{'H', 'I', 'J', 'K',1,2,3, 'p', 'e', 'n','o'}
>>> s.union(t)
{'H', 'I', 'J', 'K', 'o', 'p', 'e', 'n',1,2,3}
Similarly to list comprehensions, we can use set comprehensions to create a set:

set comprehension

>>>
>>> a = {x for x in 'abcdefg' if x not in 'abc'}
>>> a
{'g', 'd', 'e', 'f'}
