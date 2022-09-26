import sys, time

#start = time.time()

T = int(input())

for _ in range(T):

	N = int(input())

	candidate = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

	success = 0
	cnt = 1
	
	candidate.sort(key = lambda x:x[0])

	for i in range(1, N):
		if candidate[success][1] > candidate[i][1]:
			success = i
			cnt += 1
		else:
			continue
	
	print(cnt)

#end = time.time()

#print(f"{end - start:.5f} sec")
