times = int(input())
timeTable = [list(map(int, input().split())) for _ in range(times)]
timeTable.sort(key = lambda x:x[0])
timeTable.sort(key = lambda x:x[1])

next = 0
cnt = 1
for i in range(1, len(timeTable)):
	# 끝시간과 첫시간 비교
	if timeTable[next][1] <= timeTable[i][0]:
		# 다음 회의시간 카운트
		cnt += 1
		# temp에 다음 회의 저장		
		next = i
	else:
		continue
print(cnt)

	
	
		
		
		

	
	
