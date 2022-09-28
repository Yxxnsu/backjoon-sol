N, L = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

start = 0
cnt = 1
for i in range(1, len(pos)):
	if pos[i] + 0.5 - (pos[start] - 0.5) <= L:
		continue
	else:
		cnt += 1
		start = i

print(cnt)


		

		
		
	




	
	