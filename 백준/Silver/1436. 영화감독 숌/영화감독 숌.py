num = int(input())
i, cnt = 666, 0
while True:
	if "666" in str(i):
		cnt += 1
		if cnt == num:
			print(i)
			break
		else:
			i = i + 1
	else:
		i = i + 1
	
		
	
	