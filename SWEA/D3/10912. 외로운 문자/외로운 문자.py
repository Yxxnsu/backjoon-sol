T = int(input())

def sol():
	s = input()

	if len(s) == len(set(s)):
		n_s = ''.join(sorted(s))
		return n_s
	else:
		ans = []
		for v in s:
			if v in ans:
				continue
			else:
				v_cnt = s.count(v)
				if v_cnt >= 2:
					if v_cnt % 2 != 0:
						ans.append(v)
				else:
					ans.append(v)
		if len(ans) == 0:
			return 'Good'
		else:
			ans.sort()
			return ''.join(ans)
for tc in range(1, T+1):
	print(f'#{tc} {sol()}')