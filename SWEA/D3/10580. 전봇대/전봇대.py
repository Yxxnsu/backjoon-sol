T = int(input())

def sol():

    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i, N):
            ai, bi = li[i]
            aj, bj = li[j]
            if (ai < aj and bi > bj) or (ai > aj and bi < bj):
                ans += 1
    return ans
    
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')