T = int(input())

def DFS(i, taste, kcal):
    global ans

    if kcal > L:
        return
    
    ans = max(ans, taste)
    
    if i == N:
        return 
    
    t, k = li[i]

    DFS(i+1, taste, kcal)
    DFS(i+1, taste + t, kcal + k)
     
for tc in range(1, T+1):
    N, L = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    ans = 0    
    DFS(0, 0, 0)
    
    print(f'#{tc} {ans}')