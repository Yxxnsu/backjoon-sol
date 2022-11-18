T = int(input())
res = []

for tc in range(1, T+1):

    N, M = map(int, input().split())

    if M == 0:
        print(f'#{tc} 1')
    else:
        graph = [[] for _ in range(N+1)]
        
        for _ in range(M):
            x, y = map(int, input().split())
            graph[x].append(y)
            graph[y].append(x)

        def DFS(v, s):
            global ans
            ans = max(ans, len(s))
            
            for k in graph[v]:
                if k not in s:
                    DFS(k, s + [v])        
            
        ans = 0
        for i in range(1, N+1):
            DFS(i, [i])

        res.append(f'#{tc} {ans}')

print(*res,sep='\n')
