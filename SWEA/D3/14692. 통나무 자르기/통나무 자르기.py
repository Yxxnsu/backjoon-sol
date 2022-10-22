T = int(input())

for idx in range(1, T+1):

	N = int(input())
			
	print(f'#{idx} {"Alice" if N % 2 == 0 else "Bob"}')