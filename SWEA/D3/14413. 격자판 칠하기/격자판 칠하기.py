T = int(input())

for idx in range(1, T+1):

	N, M = map(int, input().split())

	matrix = [list(input()) for _ in range(N)]

	one_grid = [[0] * M for _ in range(N)]
	two_grid = [[0] * M for _ in range(N)]
	
	c = ['#','.']	
	for i in range(N):
		one_start = i % 2
		for j in range(M):
			one_grid[i][j] = c[one_start]
			one_start = (one_start + 1) % 2
			two_grid[i][j] = c[(one_start + 2) % 2]
			two_start = (one_start + 2) % 2

	one_condition = True
	two_condition = True
	for i in range(N):		
		for j in range(M):
			if matrix[i][j] != '?' and matrix[i][j] != one_grid[i][j]:
				one_condition = False
				break
		for j in range(M):
			if matrix[i][j] != '?' and matrix[i][j] != two_grid[i][j]:
				two_condition = False
				break
	print(f'#{idx} {"possible" if one_condition or two_condition else "impossible"}')