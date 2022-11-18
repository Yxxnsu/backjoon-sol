T = int(input())

def DFS(i):

    global ans

    if i == N:
        s = ''
        for i in range(N):
            if visited[i]:
                s += li[i]
        cnt = 0
        for c in alpha:
            if c in s:
                cnt += 1
        if cnt == 26:
            ans += 1
        return 
        
    visited[i] = True
    DFS(i+1)
    visited[i] = False
    DFS(i+1)

for tc in range(1, T+1):
    N = int(input())
    li = [input() for _ in range(N)]
    
    visited = [False] * N
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    ans = 0
    DFS(0)
    print(f'#{tc} {ans}')
