T = int(input())

for idx in range(1, T+1):

	N, D = map(int, input().split())

	if N % (2 * D + 1) == 0:
		print(f'#{idx} {N // (2 * D + 1)}')
	else:
		print(f'#{idx} {N // (2 * D + 1) + 1}')