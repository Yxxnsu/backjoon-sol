T = int(input())

def sol():
	s = input()

	if len(s) == len(set(s)):
		n_s = ''.join(sorted(s))
		return n_s
	else:
		ans = [v for v in s if s.count(v) % 2 == 1]
		ans = list(set(ans))
		return ''.join(sorted(ans)) if len(ans) != 0 else 'Good'
		
for tc in range(1, T+1):
	print(f'#{tc} {sol()}')