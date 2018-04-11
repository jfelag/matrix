import numpy as np

def numpy_to_latex(A):
	
	output = r'\begin{pmatrix}'
	output += '\n'
	
	x,y = A.shape
	
	for i in range(x):
		for j in range(y):
			output += str(A[i][j])
			if j == y-1:
				output += r'\\'
				output += '\n'
			else:
				output += ' & '
	
	output += r'\end{pmatrix}'
	
	return output