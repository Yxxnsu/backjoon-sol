N, M = map(int, input().split())
dna = [input() for _ in range(N)]
result = ""
cnt = 0
for i in range(M):
	store = []
	max_cnt = 0
	
	for j in range(N):
		store.append(dna[j][i])
	store.sort()

	tmp = ''
	for x in store:
		if store.count(x) > max_cnt:
			max_cnt = store.count(x)
			tmp = x
	cnt += (N - max_cnt)
	result += tmp
print(f'{result}\n{cnt}')
		
	
		
		
