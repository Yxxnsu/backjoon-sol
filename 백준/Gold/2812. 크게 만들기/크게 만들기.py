from sys import stdin
input = stdin.readline

N, K = map(int,input().split())
num = list(map(int,input().strip()))
end = N - K

result = []

for i in range(N):
    while K > 0 and result:
        if result[-1] < num[i]:
            result.pop()
            K -= 1
        else:
            break
    result.append(num[i])
    
for i in range(end):
    print(result[i], end="")
