N, M = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

negative = sorted([x for x in pos if x < 0])
positive = sorted([x for x in pos if x > 0])

walk = 0
for i in range(0,len(negative),M):
	walk += abs(negative[i]) * 2
for i in range(len(positive)-1,-1,-M):
	walk += positive[i] * 2

if abs(pos[0]) < abs(pos[-1]):
	walk -= abs(pos[-1])
else:
	walk -= abs(pos[0])

print(walk)