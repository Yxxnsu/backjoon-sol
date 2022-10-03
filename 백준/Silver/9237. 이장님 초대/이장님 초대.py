N = int(input())
T = list(map(int, input().split()))
T.sort(reverse = True)

day = []
one = 1
for i in range(N):
	day.append(T[i] + one + 1)
	one += 1
print(max(day))
	