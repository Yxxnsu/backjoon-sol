T = int(input())

for idx in range(1, T+1):

	s = list(input())

	cnt = 0
	for i,v in enumerate(s):
		if v == '(':
			if i+1 < len(s):
				if s[i+1] in (')','|'):
					cnt += 1
			else:
				break
		elif v == ')':
			if i-1 >= 0:
				if s[i-1] in ('|'):
					cnt += 1
				
	print(f'#{idx} {cnt}')