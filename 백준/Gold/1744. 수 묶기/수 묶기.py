import heapq

def solution():
	
	positive = list()
	negative = list()
	zero = set()
	ans = list()

	for _ in range(N):

		num = int(input())

		if N == 1:
			return num

		if num > 0:
			positive.append(num) 
		elif num < 0:
			negative.append(num)
		else:
			zero.add(0)

	positive.sort(reverse = True)
	negative.sort()

	if len(positive):
		if len(positive) % 2 != 0:
			end = positive.pop(len(positive)-1)
			ans.append(end)
		for i in range(0, len(positive), 2):
			if positive[i+1] == 1:
				ans.append(positive[i] + positive[i+1])
			else:	
				ans.append(positive[i] * positive[i+1])

	if len(negative):
		if len(negative) % 2 != 0:
			if len(zero):
				negative.pop(len(negative)-1)
			else:
				ans.append(negative.pop(len(negative)-1))
		for i in range(0, len(negative), 2):
			ans.append(negative[i] * negative[i+1])
	
	return sum(ans) if len(ans) else 0
					
N = int(input())
result = solution()		
print(result)
	

		
