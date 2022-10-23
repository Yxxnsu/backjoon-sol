T = int(input())

for idx in range(1, T+1):
	N = int(input())
	open_list = list(map(int, input().split()))
	start = [i for i in range(7) if open_list[i] == 1]
	
	for i, v in enumerate(start):
		day = 0
		tmp_N = N
		for j in range(v,7):
			if open_list[j] == 1:
				tmp_N -= 1
				if tmp_N == 0:
					day += 1
					break
			day += 1
		while tmp_N:
			for j in range(7):
				if open_list[j] == 1:
					tmp_N -= 1
					if tmp_N == 0:
						day += 1
						break
				day += 1
		start[i] = day	
	print(f'#{idx} {min(start)}')	