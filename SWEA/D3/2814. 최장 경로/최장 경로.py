T = int(input())


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


        def DFS(v, cnt):

            global visited, ans
            
            ans = max(cnt, ans)

            if visited[v] == True:
                return False

            visited[v] = True

            for k in graph[v]:
                if not visited[k]:
                    DFS(k, cnt + 1)
                    visited[k] = False
                                        
            return True
        
        ans = 0
        for i in range(1, N+1):
            visited = [False] * (N+1)
            DFS(i, 1)

        print(f'#{tc} {ans}')