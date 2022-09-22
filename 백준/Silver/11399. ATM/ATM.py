person = int(input())
times = list(map(int, input().split()))

times.sort() 
sum = times[0]

for i in range(1,len(times)):
	times[i] = times[i-1] + times[i]
	sum += times[i]
print(sum)
	
	
