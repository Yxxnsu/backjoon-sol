T = int(input())

for idx in range(1, T+1):

	N = [2,3,5,7,11]
	result = [0] * 5 
	num = int(input())
	
	i = 0
	while num != 1:
		if num % N[i] != 0:
			i += 1
		else:
			num //= N[i]
			result[i] += 1
	print(f'#{idx}', end = ' ')
	for v in result:
		print(v, end = ' ')
	print()