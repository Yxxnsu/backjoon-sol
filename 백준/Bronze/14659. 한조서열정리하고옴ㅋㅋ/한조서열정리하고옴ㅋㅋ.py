import sys

n = int(input())
archor = list(map(int,sys.stdin.readline().split()))

m = cnt = 0

for i in range(0, n):
	if archor[i] < archor[i-1] and i != 0:
		continue
	else:
		cnt = 0
		for j in range(i+1, n):
			if archor[i] < archor[j]:
				break
			else:
				cnt += 1
		m = max(m, cnt)
print(m)		