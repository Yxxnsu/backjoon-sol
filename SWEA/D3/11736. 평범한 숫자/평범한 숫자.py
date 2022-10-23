T = int(input())

for idx in range(1, T+1):

	N = int(input())
	num_list = list(map(int, input().split()))

	cnt = 0
	for i in range(1,N-1):
		s = num_list[i-1:i+2]
		if s[1] not in (max(s),min(s)):
			cnt += 1		
	
	print(f'#{idx} {cnt}')