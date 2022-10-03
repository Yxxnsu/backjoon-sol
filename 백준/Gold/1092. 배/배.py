from collections import deque
from sys import stdin

input = stdin.readline
N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

crane.sort(reverse = True)
box.sort(reverse = True)

if box[0] > crane[0]:
	print(-1)
else:
	cnt = 0
	while box:
		for c in crane:
			for b in box:
				if c >= b:
					box.remove(b)
					break
		cnt += 1
	print(cnt)

