T = int(input())
ontimes = []

for idx in range(1, T+1):
	a, b, c, d = map(int,input().split())
	on = min(b,d) - max(a,c)
	on = on if on > 0 else 0
	ontimes.append(on)

for i, ontime in enumerate(ontimes):
	print('#', end = '')
	print(i+1, ontime)