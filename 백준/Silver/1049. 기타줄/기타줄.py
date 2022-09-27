N, M = map(int, input().split())

min_set = min_one = 1000

for _ in range(M):
	set, one = map(int, input().split())
	if min_set > set:
		min_set = set
	if min_one > one:
		min_one = one

if N % 6 == 0:
	print(min(N // 6 * min_set, min_one * N))	
else:
	if N > 6:
		print(
			min(
				min_one * N, 
				min_set * (N // 6 + 1), 
				(min_set * (N // 6)) + (N % 6) * min_one
			)
		)
	else:
		print(min(N % 6 * min_one, min_set))
		
		