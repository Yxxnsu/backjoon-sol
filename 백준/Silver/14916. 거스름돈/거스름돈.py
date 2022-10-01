n = int(input())
cnt = 0

if n % 5 == 0:
	print(n // 5)	
else:
	if (n % 5) % 2 == 0:
		print((n // 5) + ((n % 5) // 2))
	else:
		result = []
		i = 0
		while True:
			cnt = i
			if n < 0: 
				break
			if n % 2 == 0:
				cnt += (n // 2)
				result.append(cnt)
			n -= 5
			i += 1
		print(min(result)) if len(result) else print(-1)
			
	
	