T = int(input())

for idx in range(1, T+1):
	N = int(input())
	num_list = set()

	i = 1
	while len(num_list) != 10:
		K = N * i
		for v in str(K):
			num_list.add(v)
		i += 1
	print(f'#{idx} {N * (i-1)}')