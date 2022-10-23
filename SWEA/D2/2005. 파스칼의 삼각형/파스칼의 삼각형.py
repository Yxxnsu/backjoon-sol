T = int(input())

for idx in range(1, T+1):
	N = int(input())
	pascal = [[1] * x for x in range(1, N+1)]
	
	if N > 2:
		for i in range(2, N):
			for j in range(1, i):
				pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
	print(f'#{idx}')
	for i in range(N):
		for v in pascal[i]:
			print(v, end = ' ')
		print()