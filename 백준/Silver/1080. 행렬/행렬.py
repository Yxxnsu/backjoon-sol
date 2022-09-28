n, m = map(int , input().split())

a = [[int(x) for x in input()] for _ in range(n)]
b = [[int(x) for x in input()] for _ in range(n)]

def convert_matrix(i,j):
	for n in range(i, i+3):
		for m in range(j, j+3):
			a[n][m] = 1 - a[n][m]

cnt = 0
for i in range(n-3+1):
	for j in range(m-3+1):
		if a[i][j] != b[i][j]:
			cnt += 1
			convert_matrix(i,j)
		else:
			continue

print(cnt) if a == b else print(-1)
		
	




	
	