T = int(input())

for idx in range(1, T+1):
	a, b = map(int, input().split())

	if a + b > 24:
		print(f'#{idx} {a + b - 24}')
	else:
		if a + b == 24:
			print(f'#{idx} 0')
		else:
			print(f'#{idx} {a+b}')