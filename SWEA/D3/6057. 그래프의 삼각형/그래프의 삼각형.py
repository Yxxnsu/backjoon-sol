T = int(input())

def sol():

    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for i in range(M):
        x, y = map(int, input().split())

        graph[x].append(y)
        graph[y].append(x)
    
    ans = 0
    for i in range(1, N+1):
        for g in graph[i]:
            for v in graph[g]:
                if v in graph[i]:
                    ans += 1

    return ans // 6

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')