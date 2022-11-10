T = int(input())

def sol():

    N = int(input())

    return li[N]

ans = []
li = [0] * 101
li[1], li[2], li[3], li[4], li[5] = 1,1,1,2,2
for i in range(6, 101):
    li[i] = li[i-5] + li[i-1]
for tc in range(1, T+1):
    ans.append(f'#{tc} {sol()}')
print(*ans, sep='\n')