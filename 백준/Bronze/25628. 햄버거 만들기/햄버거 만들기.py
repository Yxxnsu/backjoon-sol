a, b = map(int, input().split())

cnt = 0
while True:
	if a >= 2 and b >= 1:
		cnt += 1
		a -= 2
		b -= 1
	else:
		break
print(cnt)	