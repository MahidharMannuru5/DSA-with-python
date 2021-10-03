Creation of BST and inorder Traversal of BST


# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A utility function to insert
# a new node with the given key


def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

# A utility function to do inorder tree traversal


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
# 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inoder traversal of the BST
inorder(r)


# A O(n) program for construction of BST from preorder traversal

INT_MIN = float("-infinity")
INT_MAX = float("infinity")

# A Binary tree node


class Node:

	# Constructor to created a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Methods to get and set the value of static variable
# constructTreeUtil.preIndex for function construcTreeUtil()


def getPreIndex():
	return constructTreeUtil.preIndex


def incrementPreIndex():
	constructTreeUtil.preIndex += 1

# A recursive function to construct BST from pre[].
# preIndex is used to keep track of index in pre[]


def constructTreeUtil(pre, key, mini, maxi, size):

	# Base Case
	if(getPreIndex() >= size):
		return None

	root = None

	# If current element of pre[] is in range, then
	# only it is part of current subtree
	if(key > mini and key < maxi):

		# Allocate memory for root of this subtree
		# and increment constructTreeUtil.preIndex
		root = Node(key)
		incrementPreIndex()

		if(getPreIndex() < size):

			# Construct the subtree under root
			# All nodes which are in range {min.. key} will
			# go in left subtree, and first such node will
			# be root of left subtree
			root.left = constructTreeUtil(pre,
										pre[getPreIndex()],
										mini, key, size)
		if(getPreindex() < size):

			# All nodes which are in range{key..max} will
			# go to right subtree, and first such node will
			# be root of right subtree
			root.right = constructTreeUtil(pre,
										pre[getPreIndex()],
										key, maxi, size)

	return root

# This is the main function to construct BST from given
# preorder traversal. This function mainly uses
# constructTreeUtil()


def constructTree(pre):
	constructTreeUtil.preIndex = 0
	size = len(pre)
	return constructTreeUtil(pre, pre[0], INT_MIN, INT_MAX, size)


# A utility function to print inorder traversal of Binary Tree
def printInorder(node):

	if node is None:
		return
	printInorder(node.left)
	print node.data,
	printInorder(node.right)


# Driver code
pre = [10, 5, 1, 7, 40, 50]

# Function call
root = constructTree(pre)

print "Inorder traversal of the constructed tree: "
printInorder(root)



