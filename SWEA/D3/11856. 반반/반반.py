T = int(input())

for idx in range(1, T+1):
	s = input()

	c_s = [c for c in set(s)]

	if len(c_s) != 2:
		print(f'#{idx} No')
	else:
		yes = True
		for v in c_s:
			if s.count(v) != 2:
				yes = False
				break
		print(f'#{idx} {"Yes" if yes else "No"}')