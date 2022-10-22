T = int(input())

for idx in range(1, T+1):
	N = int(input())
	l = [list(input().split()) for _ in range(N)]

	print(f'#{idx}')
	i = 0
	for v in l:
		for _ in range(int(v[1])):
			print(v[0], end = '')
			i += 1
			if i == 10:
				print()
				i = 0
	print()