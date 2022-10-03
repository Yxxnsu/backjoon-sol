T = int(input())

for _ in range(T):

	N = int(input())
	l = list(map(int, input().split()))
	l.sort()

	result = 0
	for i in range(2, N):
		result = max(result, l[i] - l[i-2])
	print(result)