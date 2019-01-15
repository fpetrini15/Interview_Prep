#1.8 Write an algorithm such that if an element in a MxN matrix
#is 0, its entire row and column are set to 0

'''
1	1	1	0	1	0	0	1

0	1	1	1	1	1	1	1

0	1	1	0	1	1	1	1

1	0	1	0	0	0	0	1

''' 

def zero_matrix(matrix, M, N):
	rows = set()
	cols = set()
	for i in range(M):
		for j in range(N):
			if matrix[i][j] == 0:
				rows.add(i)
				cols.add(j)
	for col in cols:
		for j in range(M):
			matrix[col][j] = 0

	for row in rows:
		for j in range(N):
			matrix[row][j] = 0

	return matrix

matrix = [[1,1,1,1], [1,1,1,1], [0,1,0,1], [1,1,1,1]]
print(zero_matrix(matrix, 4, 4))