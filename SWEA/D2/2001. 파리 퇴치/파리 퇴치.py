T = int(input())

for idx in range(1, T+1):
	N, M = map(int, input().split())
	matrix = [list(map(int, input().split())) for _ in range(N)]
	max = 0
	for i in range(N-(M-1)):	
		for j in range(N-(M-1)):
			kill = 0
			for k in range(M):
				kill += sum(matrix[i+k][j:j+M])
			if max < kill:
				max = kill
	print(f'#{idx} {max}')