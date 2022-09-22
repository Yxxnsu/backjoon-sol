n = int(input())
m = [int(input()) for _ in range(n)]

dasom = m[0]

if n == 1:
	print(0)
else:
	cnt = 0
	m.pop(0)
	while dasom <= max(m):
		dasom += 1
		max_idx = m.index(max(m))
		m[max_idx] -= 1
		cnt += 1
	print(cnt)