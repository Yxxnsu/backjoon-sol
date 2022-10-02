import heapq

def solution(card, m):
	if len(card) == 1:
		return card[0]
	else:
		heap = []
		for x in card:
			heapq.heappush(heap,x)
		
		for _ in range(m):
			first = heapq.heappop(heap)
			second = heapq.heappop(heap)
			for _ in range(2):
				heapq.heappush(heap,first+second)
		sum = 0
		for i in range(len(heap)):
			sum += heap[i]
		return sum
	
n ,m = map(int, input().split())
card = list(map(int, input().split()))
result = solution(card, m)
print(result)
	







