T = int(input())

for _ in range(T):
	N, M = map(int, input().split())
	priority = list(map(int, input().split()))
	
	temp = priority.copy()
	temp[M] = -1
	cnt = 0

	while priority:
		if len(priority) == 1:
			cnt += 1	
			break
		if max(priority[1:]) > priority[0]:
			x = priority.pop(0)
			priority.append(x)
			x = temp.pop(0)
			temp.append(x)
		else:
			if temp[0] == -1:
				cnt += 1
				break
			else:
				priority.pop(0)
				temp.pop(0)
				cnt += 1
	print(cnt)