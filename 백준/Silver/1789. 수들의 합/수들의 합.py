s = int(input())

cnt = sum = 0

if s < 10:
	for i in range(1, s+1):
		sum += i
		cnt += 1

		if sum == s:
			print(cnt)
			break
		else:
			if s - sum < i:
				if s == 5:
					print(2)
				elif s == 7 or s == 8 or s== 9:
					print(3)
				else:
					print(1)
				break
				
else:
	for i in range(1, s+1):

		sum += i
		cnt += 1

		if sum == s:
			print(cnt)
			break
		else:
			if s - sum < i:
				print(cnt)
				break
	
		
	
		