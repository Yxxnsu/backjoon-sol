T = int(input())

for idx in range(1, T+1):
	s = list(input())
	s_len = len(s)

	if s_len <= 7 or s.count('o') >= 8:
		print(f'#{idx} YES')
	else:
		if 15 - s_len >= 8 - s.count('o'):
			print(f'#{idx} YES')
		else:
			print(f'#{idx} NO')