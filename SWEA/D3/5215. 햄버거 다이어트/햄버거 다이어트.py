T = int(input())

def DFS(i):
    global ans
     
    if i == N:
        taste, kcal = 0, 0
        for i in range(N):
            if visited[i]:
                t, k = li[i]
                taste += t
                kcal += k
        if kcal > L:
            return
        ans = max(ans, taste)
        return 

    visited[i] = True
    DFS(i+1)
    visited[i] = False
    DFS(i+1)
    
for tc in range(1, T+1):
    N, L = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    visited = [False] * N

    DFS(0)
    print(f'#{tc} {ans}')