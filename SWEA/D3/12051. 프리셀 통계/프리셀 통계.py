T = int(input())
def sol():
	N, P_D, P_G = map(int, input().split())
	if (P_G == 0 or P_G == 100) and P_D != P_G:
		return 'Broken'
	for i in range(1, N+1):
		if (i * P_D) % 100 == 0:
			return 'Possible'
	return 'Broken'
for tc in range(1, T+1):
	print(f'#{tc} {sol()}')