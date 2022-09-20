N, f = map(int, input().split())
cnt = 0
for i in range(N+1):
	for j in range(60):
		for k in range(60):
			time = f'{str(i).zfill(2)}:{str(j).zfill(2)}:{str(k).zfill(2)}'
			if time.count(f'{f}') > 0:
				cnt += 1
print(cnt)