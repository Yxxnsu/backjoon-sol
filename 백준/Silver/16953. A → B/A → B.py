a ,b = map(int, input().split())
cnt = 0

while a < b:
	if b % 2 == 0:
		cnt += 1
		b //= 2
		# print(b, cnt)

	else:
		s = str(b)

		if s[-1] == "1":
			b = int(s[:len(s)-1])
		else:
			break
			
		cnt += 1
		# print(b, cnt)

print(cnt+1) if a == b else print(-1)
	
	
