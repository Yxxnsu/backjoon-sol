n = int(input())
distance = list(map(int,input().split()))
oil = list(map(int,input().split()))
oil.pop()

cost = i = 0
cheap = min(oil)

while i < n:

	if oil[i] == cheap:
		cost += sum(distance[i:]) * oil[i]
		break
		
	else:
		# 다음 주유소까지의 거리 + 
		cost += distance[i] * oil[i]

		for j in range(i+1, n):
		
			# 다음 주유소가 더 비싸면 
			if oil[i] < oil[j]:				
				cost += distance[j] * oil[i]
			# 현재 주유소가 다음 주유소보다 비싸면
			else:
				i = j
				break

print(cost)
	
	
