from itertools import permutations
from sys import stdin
import time
import heapq


n = stdin.readline().rstrip()

# start = time.time()

l = [int(x) for x in n] ## O(N)

if 0 not in l:
	print(-1)
else:
	if sum(l) % 3 != 0:
		print(-1)
	else:
		l.sort(reverse = True) ## O(N)
		for x in l:            ## O(N)
			print(x, end = "")

print()
# end = time.time()
# print(f'sec : {end-start:.5f}')

