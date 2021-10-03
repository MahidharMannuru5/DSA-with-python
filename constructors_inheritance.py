Inheritance is the capability of one class to derive or inherit the properties from another class. The benefits of inheritance are: 
It represents real-world relationships well.
It provides reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
Below is a simple example of inheritance in Python 
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Person(object):
	
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True

# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())


constructors:
  Prerequisites: Object-Oriented Programming in Python, Object-Oriented Programming in Python | Set 2 
Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class 
when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.
Syntax of constructor declaration : 
  
  Syntax of constructor declaration : 

def __init__(self):
    # body of the constructor
Types of constructors : 

default constructor: The default constructor is a simple constructor which doesn’t accept any arguments.
  Its definition has only one argument which is a reference to the instance being constructed.
parameterized constructor: constructor with parameters is known as parameterized constructor. 
  The parameterized constructor takes its first argument as a reference to the instance being constructed known as self 
  and the rest of the arguments are provided by the programmer.
Example of default constructor : 
  class GeekforGeeks:

	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()


Simple program to understand better of constructors

class Addition:
	first = 0
	second = 0
	answer = 0
	
	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s
	
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()

  
