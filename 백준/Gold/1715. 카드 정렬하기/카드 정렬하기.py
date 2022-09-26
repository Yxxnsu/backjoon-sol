import sys, heapq

n = int(sys.stdin.readline())
card = [int(sys.stdin.readline()) for _ in range(n)]
heapq.heapify(card)

sum = 0

if n == 1:
	print(0)

else:
	while len(card) >= 2:
		
		min1 = heapq.heappop(card)
		min2 = heapq.heappop(card)

		sum += min1 + min2
		
		heapq.heappush(card, min1 + min2)

	print(sum)
