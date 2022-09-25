k = int(input())
lope = [int(input()) for _ in range(k)]
lope.sort()

for i in range(k):
	lope[i] = lope[i] * (k-i)

print(max(lope))

