day = int(input())
consult = [list(map(int, input().split())) for _ in range(day)]

def recursion(start, end):
	if start > end:
		return 0

	else: 
#		print(f'start is {start}')
		temp = []
		while start <= end:
			if start + consult[start][0] - 1 > end:
				start += 1
				continue
			else:
				temp.append(recursion(consult[start][0] + start, end) + consult[start][1])
				start += 1
		return 0 if(len(temp) == 0) else max(temp)
				 
max_profit = 0

for i in range(day):
	profit = recursion(i, day - 1)
	if max_profit < profit:
		max_profit = profit

print(max_profit)
	
	
	
