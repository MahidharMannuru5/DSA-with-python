1. str(dic) :- This method is used to return the string, denoting all the dictionary keys with their values.

2. items() :- This method is used to return the list with all dictionary keys with values.

# Python code to demonstrate working of
# str() and items()

# Initializing dictionary
dic = { 'Name' : 'Nandini', 'Age' : 19 }

# using str() to display dic as string
print ("The constituents of dictionary as string are : ")
print (str(dic))

# using str() to display dic as list
print ("The constituents of dictionary as list are : ")
print (dic.items())

3. len() :- It returns the count of key entities of the dictionary elements.

4. type() :- This function returns the data type of the argument
  
# Python code to demonstrate working of
# len() and type()

# Initializing dictionary
dic = { 'Name' : 'Nandini', 'Age' : 19, 'ID' : 2541997 }

# Initializing list
li = [ 1, 3, 5, 6 ]

# using len() to display dic size
print ("The size of dic is : ",end="")
print (len(dic))

# using type() to display data type
print ("The data type of dic is : ",end="")
print (type(dic))

# using type() to display data type
print ("The data type of li is : ",end="")
print (type(li))

5. copy() :- This function creates the shallow copy of the dictionary into other dictionary.

6. clear() :- This function is used to clear the dictionary contents.
  
# Python code to demonstrate working of
# clear() and copy()

# Initializing dictionary
dic1 = { 'Name' : 'Nandini', 'Age' : 19 }

# Initializing dictionary
dic3 = {}

# using copy() to make shallow copy of dictionary
dic3 = dic1.copy()

# printing new dictionary
print ("The new copied dictionary is : ")
print (dic3.items())

# clearing the dictionary
dic1.clear()

# printing cleared dictionary
print ("The contents of deleted dictionary is : ",end="")
print (dic1.items())




