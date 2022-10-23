T = int(input())

for idx in range(1, T+1):
	
	s = input()
	
	a = b = 1
	for v in s:
		if v == 'L':
			b = a + b
		else:
			a = a + b
	print(f'#{idx} {a} {b}')