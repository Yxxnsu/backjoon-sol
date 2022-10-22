from itertools import permutations

T = int(input())

for idx in range(1, T+1):

	N = list(input())

	if int(''.join(N)) == 1:
		print(f'#{idx} impossible')
	else:
		permute_N = [x for x in permutations(N)]
	
		possible = False
		for v in permute_N:
			s = ''.join(v)
			if int(s) % int(''.join(N)) == 0 and int(s) != int(''.join(N)):
				possible = True
				print(f'#{idx} possible')
				break
		if not possible:
			print(f'#{idx} impossible')