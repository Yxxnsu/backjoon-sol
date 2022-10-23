def rotate_matrix_90_degree(matrix, N):
	new_matrix = [[0] * N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			new_matrix[j][N-i-1] = matrix[i][j]
	return new_matrix

T = int(input())

for idx in range(1, T+1):

	N = int(input())

	matrix = [list(map(int, input().split())) for _ in range(N)]

	matrix_90_degree = rotate_matrix_90_degree(matrix,N)
	matrix_180_degree = rotate_matrix_90_degree(matrix_90_degree,N)
	matrix_270_degree = rotate_matrix_90_degree(matrix_180_degree,N)
	
	print(f'#{idx}')
	for i in range(N):
		print(*matrix_90_degree[i], sep = '', end = ' ')
		print(*matrix_180_degree[i], sep = '', end = ' ')
		print(*matrix_270_degree[i], sep = '', end = ' ')
		print()