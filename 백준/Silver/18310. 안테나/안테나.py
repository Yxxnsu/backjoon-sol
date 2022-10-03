N = int(input())
pos = list(map(int, input().split()))
pos.sort()

if N % 2 != 0:
	print(pos[N // 2])
else:
	print(pos[(N // 2) - 1])