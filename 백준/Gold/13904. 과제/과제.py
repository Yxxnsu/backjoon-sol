'''
List or queue 등에서 특정 원소 제거하려고 할 때는
1. enumerate
2. for x in list
'''
from collections import deque

N = int(input())
task = [list(map(int, input().split())) for _ in range(N)]
task.sort(key = lambda x:x[1], reverse = True)
score = [0] * 1001

for x in task:
	d, w = x[0], x[1]

	if score[d] == 0:
		score[d] = w
	else:
		while d > 0:
			d -= 1
			if d == 0:
				break
			if score[d] == 0:
				score[d] = w
				break
			else:
				continue
print(sum(score))		