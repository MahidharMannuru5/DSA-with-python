Implentation of stacks using array or lists

# Python program to
# demonstrate stack implementation
# using list


stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

Implementation of stack using linked list
# Python program to demonstrate
# stack implementation using a linked list.
# node class
class Node:
def __init__(self, value):
	self.value = value
	self.next = None

class Stack:
	
# Initializing a stack.
# Use a dummy node, which is
# easier for handling edge cases.
def __init__(self):
	self.head = Node("head")
	self.size = 0

# String representation of the stack
def __str__(self):
	cur = self.head.next
	out = ""
	while cur:
		out += str(cur.value) + "->"
		cur = cur.next
	return out[:-3]

# Get the current size of the stack
def getSize(self):
	return self.size




conversion of given infinix expression to postfix expression

# Python program to convert infix expression to postfix

# Class to convert the expression
class Conversion:
	
	# Constructor to initialize the class variables
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		# This array is used a stack
		self.array = []
		# Precedence setting
		self.output = []
		self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
	
	# check if the stack is empty
	def isEmpty(self):
		return True if self.top == -1 else False
	
	# Return the value of the top of the stack
	def peek(self):
		return self.array[-1]
	
	# Pop the element from the stack
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"
	
	# Push the element to the stack
	def push(self, op):
		self.top += 1
		self.array.append(op)

	# A utility function to check is the given character
	# is operand
	def isOperand(self, ch):
		return ch.isalpha()

	# Check if the precedence of operator is strictly
	# less than top of stack or not
	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False
			
	# The main function that
	# converts given infix expression
	# to postfix expression
	def infixToPostfix(self, exp):
		
		# Iterate over the expression for conversion
		for i in exp:
			# If the character is an operand,
			# add it to output
			if self.isOperand(i):
				self.output.append(i)
			
			# If the character is an '(', push it to stack
			elif i == '(':
				self.push(i)

			# If the scanned character is an ')', pop and
			# output from the stack until and '(' is found
			elif i == ')':
				while( (not self.isEmpty()) and
								self.peek() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()

			# An operator is encountered
			else:
				while(not self.isEmpty() and self.notGreater(i)):
					self.output.append(self.pop())
				self.push(i)

		# pop all the operator from the stack
		while not self.isEmpty():
			self.output.append(self.pop())

		print "".join(self.output)

# Driver program to test above function
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)





	
# Check if the stack is empty
def isEmpty(self):
	return self.size == 0
	
# Get the top item of the stack
def peek(self):
	
	# Sanitary check to see if we
	# are peeking an empty stack.
	if self.isEmpty():
		raise Exception("Peeking from an empty stack")
	return self.head.next.value

# Push a value into the stack.
def push(self, value):
	node = Node(value)
	node.next = self.head.next
	self.head.next = node
	self.size += 1
	
# Remove a value from the stack and return.
def pop(self):
	if self.isEmpty():
		raise Exception("Popping from an empty stack")
	remove = self.head.next
	self.head.next = self.head.next.next
	self.size -= 1
	return remove.value

# Driver Code
if __name__ == "__main__":
stack = Stack()
for i in range(1, 11):
	stack.push(i)
print(f"Stack: {stack}")

for _ in range(1, 6):
	remove = stack.pop()
	print(f"Pop: {remove}")
print(f"Stack: {stack}")

