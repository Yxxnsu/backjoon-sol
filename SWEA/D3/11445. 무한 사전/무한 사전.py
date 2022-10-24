T = int(input())
def sol():
	p = input().strip()
	q = input().strip()
	
	p_len = len(p)

	if p == q[:p_len] and q[p_len:] == 'a':
		return 'N'
	return 'Y'
				
for tc in range(1, T+1):
	print(f'#{tc} {sol()}')