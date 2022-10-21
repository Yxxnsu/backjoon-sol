T = int(input())

for idx in range(1, T+1):
	N = int(input())
	curr_v = dist = 0
	for i in range(N):
		try:
			command, v = map(int, input().split())
		except ValueError:
			command, v = 0, 0
		
		if command == 1:
			curr_v += v
		elif command == 2:
			curr_v -= v
			if curr_v < 0:
				curr_v = 0
		dist += curr_v
	print(f'#{idx} {dist}')	
	