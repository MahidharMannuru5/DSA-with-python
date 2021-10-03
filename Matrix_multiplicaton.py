# Program to multiply two matrices using nested loops

# take a 3x3 matrix
A = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]
	
result = [[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]]

# iterating by row of A
for i in range(len(A)):

	# iterating by column by B
	for j in range(len(B[0])):

		# iterating by rows of B
		for k in range(len(B)):
			result[i][j] += A[i][k] * B[k][j]

for r in result:
	print(r)

  
  USING NUMPY
  import numpy as np
# two dimensional arrays
m1 = np.array([[1,4,7],[2,5,8]])
m2 = np.array([[1,4],[2,5],[3,6]])
m3 = np.dot(m1,m2) 
print(m3) 

# three dimensional arrays
m1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3]) 
m2 = ([3, 4, 6],[5, 6, 7],[6,56, 7]) 
m3 = np.dot(m1,m2) 
print(m3) 
