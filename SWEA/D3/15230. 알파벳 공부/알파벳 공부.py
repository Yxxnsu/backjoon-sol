T = int(input())

for idx in range(1, T+1):
	s = list(input())
	if ord(s[0]) != ord('a'):
		print(f'#{idx} 0')
	else:
		ascii = ord('a')
		cnt = 0
		for v in s:
			if ord(v) == ascii:
				cnt += 1
				ascii = ord(v) + 1
			else:
				break
		print(f'#{idx} {cnt}')


			