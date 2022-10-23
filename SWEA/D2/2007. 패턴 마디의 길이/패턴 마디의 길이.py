T = int(input())

for idx in range(1, T+1):
	s = list(input())
	cnt = 1
	for i,v in enumerate(s):
		if s[0] == v and i != 0:
			if s[0:i] == s[i:i+i]:
				print(f'#{idx} {i}')
				break