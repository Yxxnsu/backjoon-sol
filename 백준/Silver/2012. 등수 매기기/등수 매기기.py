from sys import stdin
input = stdin.readline

N = int(input().rstrip())
predict = [int(input().rstrip()) for _ in range(N)]
predict.sort()

sum = 0
for i in range(N):
	sum += abs(predict[i] - (i+1))
print(sum)	